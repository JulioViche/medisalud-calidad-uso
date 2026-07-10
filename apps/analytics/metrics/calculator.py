from __future__ import annotations

import math
from collections import Counter, defaultdict
from statistics import mean, pstdev

from apps.analytics.common.models import Metric


def percentage(part: int, total: int) -> float:
    return round(part * 100 / total, 2) if total else 0.0


def percentile(values: list[float], percentile_value: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, math.ceil(percentile_value * len(ordered)) - 1)
    return round(ordered[index], 2)


class MetricsCalculator:
    def calculate(
        self,
        events: list[dict[str, str]],
        surveys: list[dict[str, str]],
        incidents: list[dict[str, str]],
    ) -> list[Metric]:
        by_type: dict[str, list[dict[str, str]]] = defaultdict(list)
        for event in events:
            by_type[event["event_type"]].append(event)

        hce = by_type["hce_save"]
        appointments = by_type["appointment"]
        billing = by_type["billing"]
        prescriptions = by_type["prescription"]
        imaging = by_type["imaging"]
        teleconsultations = by_type["teleconsultation"]
        hce_times = [float(row["duration_seconds"]) for row in hce]
        site_hce: dict[str, list[float]] = defaultdict(list)
        for row in hce:
            site_hce[row["site"]].append(float(row["duration_seconds"]))

        privacy_count = sum(
            1 for row in incidents if "otro paciente" in row["descripcion"].lower() or "privacidad" in row["descripcion"].lower()
        )
        csat = [int(row["csat"]) for row in surveys]
        incomplete_surveys = sum(row["completed"].lower() != "true" for row in surveys)

        return [
            self._metric("M-EFI-01", "P90 registro HCE", "Eficiencia", percentile(hce_times, 0.9), "segundos", "<= 8", "events:hce_save", 8, 12, lower=True),
            self._metric("M-EFE-01", "Exito de agendamiento", "Efectividad", self._success(appointments), "%", ">= 95", "events:appointment", 95, 85),
            self._metric("M-RIE-01", "Errores de facturacion", "Libertad de Riesgo", self._failure(billing), "%", "< 1", "events:billing", 1, 3, lower=True),
            self._metric("M-SAT-01", "Abandono de encuesta movil", "Satisfaccion", percentage(incomplete_surveys, len(surveys)), "%", "< 10", "surveys", 10, 20, lower=True),
            self._metric("M-CC-01", "Variabilidad HCE entre sedes", "Cobertura de Contexto", round(pstdev([mean(v) for v in site_hce.values()]), 2), "segundos", "<= 2", "events:hce_save", 2, 4, lower=True),
            self._metric("M-RIE-02", "Incidentes de privacidad", "Libertad de Riesgo", float(privacy_count), "incidentes", "= 0", "incidents", 0, 1, lower=True),
            self._metric("M-SAT-02", "CSAT promedio", "Satisfaccion", round(mean(csat), 2), "1-5", ">= 4", "surveys", 4, 3),
            self._metric("M-EFE-02", "Recetas correctas", "Efectividad", self._success(prescriptions), "%", "= 100", "events:prescription", 99.9, 98),
            self._metric("M-EFI-02", "P90 carga de imagen", "Eficiencia", percentile([float(row["duration_seconds"]) for row in imaging], 0.9), "segundos", "<= 10", "events:imaging", 10, 15, lower=True),
            self._metric("M-CC-02", "Caidas de teleconsulta", "Cobertura de Contexto", self._failure(teleconsultations), "%", "< 5", "events:teleconsultation", 5, 10, lower=True),
        ]

    @staticmethod
    def _success(rows: list[dict[str, str]]) -> float:
        return percentage(sum(row["successful"].lower() == "true" for row in rows), len(rows))

    @staticmethod
    def _failure(rows: list[dict[str, str]]) -> float:
        return percentage(sum(row["successful"].lower() != "true" for row in rows), len(rows))

    @staticmethod
    def _metric(
        code: str,
        name: str,
        characteristic: str,
        value: float,
        unit: str,
        target: str,
        source: str,
        green: float,
        yellow: float,
        lower: bool = False,
    ) -> Metric:
        if lower:
            status = "VERDE" if value <= green else "AMARILLO" if value <= yellow else "ROJO"
        else:
            status = "VERDE" if value >= green else "AMARILLO" if value >= yellow else "ROJO"
        return Metric(code, name, characteristic, value, unit, target, status, source)
