from __future__ import annotations

import json
import unittest
from pathlib import Path

from apps.analytics.classification.classifier import IncidentClassifier, _activity_justification
from apps.analytics.common.io import read_csv
from apps.analytics.exporters.pipeline import run_pipeline
from apps.analytics.metrics.calculator import MetricsCalculator, percentage, percentile
from apps.analytics.simulation.generator import EVENT_TYPES, SITES, SimulationGenerator
from apps.analytics.validation import (
    DataValidationError,
    validate_events,
    validate_incidents,
    validate_surveys,
)


ROOT = Path(__file__).resolve().parents[3]


class ClassificationTests(unittest.TestCase):
    CASES = {
        "Nota de evolucion tarda 22s en guardarse": "Eficiencia",
        "Usuario no logra agendar tras 3 intentos": "Efectividad",
        "Factura duplicada al reintentar pago": "Libertad de Riesgo",
        "Videollamada se corta a los 4 minutos": "Cobertura de Contexto",
        "Datos de otro paciente visibles brevemente": "Libertad de Riesgo",
        "Formulario confuso, abandono de registro": "Satisfaccion",
    }

    def test_six_reference_incidents_match_table_2_2(self) -> None:
        classifier = IncidentClassifier()
        for description, expected in self.CASES.items():
            with self.subTest(description=description):
                self.assertEqual(expected, classifier.classify(description).characteristic)

    def test_risk_has_precedence_over_functional_failure(self) -> None:
        result = IncidentClassifier().classify("Historial de alergias no carga")
        self.assertEqual("Libertad de Riesgo", result.characteristic)

    def test_normalization_handles_case_and_whitespace(self) -> None:
        result = IncidentClassifier().classify("  NOTA   TARDA  demasiado ")
        self.assertEqual("Eficiencia", result.characteristic)

    def test_unknown_incident_uses_documented_default(self) -> None:
        result = IncidentClassifier().classify("Comportamiento pendiente de analizar")
        self.assertEqual("Efectividad", result.characteristic)
        self.assertEqual("regla_por_defecto", result.matched_rule)

    def test_activity_justification_is_specific_for_every_characteristic(self) -> None:
        for characteristic in {
            "Efectividad", "Eficiencia", "Satisfaccion", "Libertad de Riesgo",
            "Cobertura de Contexto",
        }:
            text = _activity_justification("Incidente controlado", characteristic)
            self.assertIn("Incidente controlado", text)
            self.assertIn(characteristic, text)


class FormulaTests(unittest.TestCase):
    def test_percentage_and_zero_denominator(self) -> None:
        self.assertEqual(25.0, percentage(1, 4))
        self.assertEqual(0.0, percentage(4, 0))

    def test_nearest_rank_percentile_boundaries(self) -> None:
        values = list(range(1, 11))
        self.assertEqual(1, percentile(values, 0.01))
        self.assertEqual(9, percentile(values, 0.9))
        self.assertEqual(10, percentile(values, 1.0))
        self.assertEqual(0.0, percentile([], 0.9))

    @staticmethod
    def _event(kind: str, duration: float, successful: bool, site: str = "Quito") -> dict[str, str]:
        return {
            "event_type": kind,
            "duration_seconds": str(duration),
            "successful": str(successful),
            "site": site,
        }

    def setUp(self) -> None:
        self.events = [
            self._event("hce_save", 4, True, "Quito"),
            self._event("hce_save", 8, True, "Quito"),
            self._event("hce_save", 12, True, "Manta"),
            self._event("hce_save", 16, False, "Manta"),
            self._event("appointment", 2, True),
            self._event("appointment", 2, False),
            *[self._event("billing", 2, True) for _ in range(99)],
            self._event("billing", 2, False),
            *[self._event("prescription", 2, True) for _ in range(10)],
            self._event("imaging", 5, True),
            self._event("imaging", 10, True),
            *[self._event("teleconsultation", 240, True) for _ in range(19)],
            self._event("teleconsultation", 240, False),
        ]
        self.surveys = [
            {"csat": "4", "completed": str(index < 9)} for index in range(10)
        ]
        self.incidents = [{"descripcion": "Datos de otro paciente visibles"}]
        self.metrics = {
            metric.code: metric
            for metric in MetricsCalculator().calculate(self.events, self.surveys, self.incidents)
        }

    def test_catalog_has_ten_unique_metrics_and_five_characteristics(self) -> None:
        self.assertEqual(10, len(self.metrics))
        self.assertEqual(
            {"Efectividad", "Eficiencia", "Satisfaccion", "Libertad de Riesgo", "Cobertura de Contexto"},
            {metric.characteristic for metric in self.metrics.values()},
        )

    def test_effectiveness_formulas(self) -> None:
        self.assertEqual(50.0, self.metrics["M-EFE-01"].value)
        self.assertEqual(100.0, self.metrics["M-EFE-02"].value)

    def test_efficiency_uses_p90_and_rnf_01_threshold(self) -> None:
        metric = self.metrics["M-EFI-01"]
        self.assertEqual(16.0, metric.value)
        self.assertEqual("<= 8", metric.target)
        self.assertEqual("ROJO", metric.status)

    def test_risk_rate_accepts_exact_one_percent_boundary(self) -> None:
        metric = self.metrics["M-RIE-01"]
        self.assertEqual(1.0, metric.value)
        self.assertEqual("<= 1", metric.target)
        self.assertEqual("VERDE", metric.status)

    def test_satisfaction_formulas_and_boundaries(self) -> None:
        self.assertEqual(10.0, self.metrics["M-SAT-01"].value)
        self.assertEqual("VERDE", self.metrics["M-SAT-01"].status)
        self.assertEqual(4.0, self.metrics["M-SAT-02"].value)
        self.assertEqual("VERDE", self.metrics["M-SAT-02"].status)

    def test_context_coverage_is_disaggregated(self) -> None:
        self.assertEqual(4.0, self.metrics["M-CC-01"].value)
        self.assertEqual("AMARILLO", self.metrics["M-CC-01"].status)
        self.assertEqual(5.0, self.metrics["M-CC-02"].value)
        self.assertEqual("VERDE", self.metrics["M-CC-02"].status)

    def test_metric_contract_is_complete(self) -> None:
        for metric in self.metrics.values():
            payload = metric.to_dict()
            self.assertEqual(
                {"code", "name", "characteristic", "value", "unit", "target", "status", "source"},
                set(payload),
            )
            self.assertIn(metric.status, {"VERDE", "AMARILLO", "ROJO"})


class SimulationAndValidationTests(unittest.TestCase):
    @staticmethod
    def _strings(row: dict[str, object]) -> dict[str, str]:
        return {key: str(value) for key, value in row.items()}

    def test_seed_is_reproducible_and_different_seeds_diverge(self) -> None:
        first = SimulationGenerator(42).generate(30)
        second = SimulationGenerator(42).generate(30)
        third = SimulationGenerator(43).generate(30)
        self.assertEqual(first, second)
        self.assertNotEqual(first, third)

    def test_generated_events_have_contract_roles_sites_and_types(self) -> None:
        rows = SimulationGenerator(25022).generate(6000)
        self.assertEqual(6000, len(rows))
        self.assertEqual(6000, len({row["event_id"] for row in rows}))
        self.assertEqual(set(EVENT_TYPES), {row["event_type"] for row in rows})
        self.assertEqual(set(SITES), {row["site"] for row in rows})
        expected_roles = {
            "hce_save": "Medico", "appointment": "Paciente", "billing": "Admision",
            "prescription": "Medico", "imaging": "Medico", "teleconsultation": "Paciente",
        }
        for row in rows:
            self.assertEqual(expected_roles[row["event_type"]], row["role"])
            self.assertGreater(row["duration_seconds"], 0)
            self.assertTrue(row["simulated"])

    def test_generated_surveys_have_valid_ranges(self) -> None:
        rows = SimulationGenerator(25022).surveys(500)
        self.assertEqual(500, len(rows))
        self.assertEqual(500, len({row["survey_id"] for row in rows}))
        self.assertTrue(all(1 <= row["csat"] <= 5 for row in rows))
        self.assertTrue(all(0 <= row["nps"] <= 10 for row in rows))

    def test_valid_generated_data_passes_quality_gate(self) -> None:
        generator = SimulationGenerator(25022)
        validate_events([self._strings(row) for row in generator.generate(100)])
        validate_surveys([self._strings(row) for row in generator.surveys(100)])

    def test_duplicate_event_id_is_rejected(self) -> None:
        rows = [self._strings(row) for row in SimulationGenerator(1).generate(2)]
        rows[1]["event_id"] = rows[0]["event_id"]
        with self.assertRaisesRegex(DataValidationError, "duplicados"):
            validate_events(rows)

    def test_hce_time_outside_logical_range_is_rejected(self) -> None:
        row = next(
            self._strings(item)
            for item in SimulationGenerator(1).generate(100)
            if item["event_type"] == "hce_save"
        )
        row["duration_seconds"] = "121"
        with self.assertRaisesRegex(DataValidationError, "duracion"):
            validate_events([row])

    def test_invalid_csat_is_rejected(self) -> None:
        row = self._strings(SimulationGenerator(1).surveys(1)[0])
        row["csat"] = "6"
        with self.assertRaisesRegex(DataValidationError, "puntaje"):
            validate_surveys([row])

    def test_duplicate_incident_id_is_rejected(self) -> None:
        row = {
            "id": "1001", "fecha": "2025-11-03", "modulo": "HCE",
            "descripcion": "Lentitud", "rol_usuario": "Medico", "sede": "Quito",
        }
        with self.assertRaisesRegex(DataValidationError, "duplicados"):
            validate_incidents([row, dict(row)])


class PipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = ROOT

    def tearDown(self) -> None:
        pass

    def test_pipeline_is_reproducible_and_exports_every_contract(self) -> None:
        first = run_pipeline(self.root, 25022)
        second = run_pipeline(self.root, 25022)
        self.assertEqual(first, second)
        self.assertEqual(10, len(first["metrics"]))
        for relative in (
            "apps/data/simulated/events.csv",
            "apps/data/simulated/surveys.csv",
            "apps/data/processed/incidentes_clasificados.csv",
            "apps/data/processed/metricas.csv",
            "data/logs_hce.csv",
            "data/encuesta_satisfaccion.csv",
            "dashboards/indicadores.json",
            "reportes/evidencias/resultados/metricas_resumen.json",
        ):
            self.assertTrue((self.root / relative).is_file(), relative)

    def test_compatibility_csvs_are_complete_clean_and_logical(self) -> None:
        run_pipeline(self.root, 25022)
        logs = read_csv(self.root / "data/logs_hce.csv")
        surveys = read_csv(self.root / "data/encuesta_satisfaccion.csv")
        self.assertGreater(len(logs), 0)
        self.assertEqual(2000, len(surveys))
        self.assertEqual(len(logs), len({row["evento_id"] for row in logs}))
        self.assertEqual(2000, len({row["respuesta_id"] for row in surveys}))
        self.assertTrue(all(0 < float(row["tiempo_segundos"]) <= 120 for row in logs))
        self.assertTrue(all(row["completada"] in {"0", "1"} for row in logs))
        self.assertTrue(all(1 <= int(row["puntaje_csat"]) <= 5 for row in surveys))
        self.assertEqual(set(SITES), {row["sede"] for row in logs})

    def test_dashboard_json_contains_metrics_metadata_and_five_sites(self) -> None:
        run_pipeline(self.root, 25022)
        payload = json.loads((self.root / "dashboards/indicadores.json").read_text(encoding="utf-8"))
        self.assertEqual("ISO/IEC 25022", payload["metadata"]["norma"])
        self.assertEqual(25022, payload["metadata"]["semilla"])
        self.assertEqual(10, len(payload["metricas"]))
        self.assertEqual(set(SITES), {row["sede"] for row in payload["eficiencia_por_sede"]})


if __name__ == "__main__":
    unittest.main()
