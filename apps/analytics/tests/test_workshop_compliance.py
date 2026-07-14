from __future__ import annotations

import json
import unittest
from pathlib import Path

from apps.analytics.common.io import read_csv
from apps.analytics.simulation.generator import SITES


ROOT = Path(__file__).resolve().parents[3]


class RepositoryContractTests(unittest.TestCase):
    def test_scenario_1_repository_structure_exists(self) -> None:
        for folder in ("data", "scripts", "dashboards", "docs", "reportes"):
            self.assertTrue((ROOT / folder).is_dir(), folder)

    def test_scenario_1_analysis_answers_all_guide_questions(self) -> None:
        text = (ROOT / "docs/analisis_inicial.md").read_text(encoding="utf-8")
        for phrase in (
            "3 procesos más críticos", "usuarios se ven más afectados",
            "evidencia tiene hoy", "evidencia le falta", "Conclusión parcial",
        ):
            self.assertIn(phrase, text)

    def test_scenario_2_dataset_has_3000_unique_non_null_incidents(self) -> None:
        rows = read_csv(ROOT / "data/incidentes_2025.csv")
        self.assertEqual(3000, len(rows))
        self.assertEqual(3000, len({row["id"] for row in rows}))
        required = {"id", "fecha", "modulo", "descripcion", "rol_usuario", "sede"}
        self.assertTrue(required.issubset(rows[0]))
        self.assertTrue(all(all(str(row[field]).strip() for field in required) for row in rows))
        self.assertEqual(set(SITES), {row["sede"] for row in rows})

    def test_scenario_2_reference_classifications_and_justifications(self) -> None:
        rows = {row["id"]: row for row in read_csv(ROOT / "data/clasificacion/incidentes_clasificados.csv")}
        expected = {
            "1001": "Eficiencia", "1002": "Efectividad",
            "1003": "Libertad de Riesgo", "1004": "Cobertura de Contexto",
            "1005": "Libertad de Riesgo", "1006": "Satisfaccion",
        }
        self.assertEqual(3000, len(rows))
        for incident_id, characteristic in expected.items():
            with self.subTest(incident_id=incident_id):
                self.assertEqual(characteristic, rows[incident_id]["caracteristica"])
                self.assertGreater(len(rows[incident_id]["justificacion"]), 80)

    def test_scenario_2_classification_covers_all_five_characteristics(self) -> None:
        rows = read_csv(ROOT / "data/clasificacion/incidentes_clasificados.csv")
        self.assertEqual(
            {"Efectividad", "Eficiencia", "Satisfaccion", "Libertad de Riesgo", "Cobertura de Contexto"},
            {row["caracteristica"] for row in rows},
        )

    def test_scenario_3_map_is_available_as_raster_and_vector(self) -> None:
        for relative in (
            "docs/mapa-conceptual/mapa_conceptual_square.png",
            "docs/mapa-conceptual/mapa_conceptual_square.pdf",
        ):
            path = ROOT / relative
            self.assertTrue(path.is_file(), relative)
            self.assertGreater(path.stat().st_size, 10_000)

    def test_scenarios_4_to_6_are_fully_documented(self) -> None:
        text = (ROOT / "reportes/chapters/04-fases4-8.tex").read_text(encoding="utf-8")
        self.assertEqual(3, text.count("Ficha Usuario--Tarea--Contexto"))
        self.assertIn("seis tareas de prioridad 1", text)
        for code in ("M-EFE-01", "M-EFI-01", "M-SAT-02", "M-RIE-01", "M-CC-01"):
            self.assertIn(code, text)
        normalized = text.casefold()
        for field in ("propósito", "fórmula", "variables", "unidad", "fuente", "frecuencia", "responsable"):
            self.assertIn(field, normalized)

    def test_scenario_7_literal_csv_contracts_exist_and_are_clean(self) -> None:
        logs = read_csv(ROOT / "data/logs_hce.csv")
        surveys = read_csv(ROOT / "data/encuesta_satisfaccion.csv")
        self.assertGreater(len(logs), 0)
        self.assertGreaterEqual(len(surveys), 150)
        self.assertEqual(len(logs), len({row["evento_id"] for row in logs}))
        self.assertEqual(len(surveys), len({row["respuesta_id"] for row in surveys}))
        self.assertTrue(all(0 < float(row["tiempo_segundos"]) <= 120 for row in logs))
        self.assertTrue(all(1 <= int(row["puntaje_csat"]) <= 5 for row in surveys))

    def test_scenario_8_json_contract_contains_ten_metrics_and_context(self) -> None:
        payload = json.loads((ROOT / "dashboards/indicadores.json").read_text(encoding="utf-8"))
        self.assertEqual("ISO/IEC 25022", payload["metadata"]["norma"])
        self.assertEqual(10, len(payload["metricas"]))
        self.assertEqual(set(SITES), {row["sede"] for row in payload["eficiencia_por_sede"]})
        for metric in payload["metricas"].values():
            self.assertTrue({"code", "name", "characteristic", "value", "unit", "target", "status", "source"}.issubset(metric))

    def test_scenario_8_github_actions_is_scheduled_reproducible_and_publishes_artifacts(self) -> None:
        text = (ROOT / ".github/workflows/medicion-calidad.yml").read_text(encoding="utf-8")
        for phrase in (
            "schedule:", "workflow_dispatch:", "python-version: \"3.11\"",
            "apps.analytics.exporters.pipeline", "unittest discover",
            "actions/upload-artifact@v4", "dashboards/indicadores.json",
        ):
            self.assertIn(phrase, text)

    def test_final_report_and_execution_evidence_are_present(self) -> None:
        report = ROOT / "reportes/entrega/medisalud_iso25022.pdf"
        self.assertGreater(report.stat().st_size, 100_000)
        self.assertEqual(b"%PDF", report.read_bytes()[:4])
        evidence = json.loads(
            (ROOT / "reportes/evidencias/pruebas/resumen-ejecucion-2026-07-13.json").read_text(encoding="utf-8")
        )
        self.assertEqual(evidence["automated_tests"]["total"], evidence["automated_tests"]["passed"])
        self.assertEqual(500, evidence["jmeter"]["samples"])
        self.assertEqual(0, evidence["jmeter"]["errors"])


if __name__ == "__main__":
    unittest.main()
