from __future__ import annotations

import hashlib
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

from apps.analytics.classification.classifier import classify_file
from apps.analytics.common.io import read_csv, write_csv, write_json
from apps.analytics.metrics.calculator import MetricsCalculator
from apps.analytics.simulation.generator import generate_files


class MeasurementService:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.original = root / "apps/data/original/incidentes_2025.csv"
        self.processed = root / "apps/data/processed"
        self.simulated = root / "apps/data/simulated"
        self.evidence = root / "reportes/evidencias/resultados"
        self.survey_log = root / "apps/data/simulated/patient_surveys.csv"

    def ensure_data(self) -> None:
        classified = self.processed / "incidentes_clasificados.csv"
        metrics = self.processed / "metricas.csv"
        if not classified.exists():
            classify_file(self.original, classified, self.evidence / "clasificacion_resumen.json")
        if not (self.simulated / "events.csv").exists():
            generate_files(self.simulated, 25022, 6000)
        if not metrics.exists():
            self._calculate_metrics()

    def incidents(
        self,
        site: str | None,
        module: str | None,
        role: str | None,
        characteristic: str | None,
        limit: int,
        offset: int,
    ) -> dict[str, object]:
        rows = read_csv(self.processed / "incidentes_clasificados.csv")
        filters = {"sede": site, "modulo": module, "rol_usuario": role, "characteristic": characteristic}
        for field, value in filters.items():
            if value:
                rows = [row for row in rows if row[field].casefold() == value.casefold()]
        return {"total": len(rows), "limit": limit, "offset": offset, "items": rows[offset : offset + limit]}

    def metrics(self) -> list[dict[str, str]]:
        return read_csv(self.processed / "metricas.csv")

    def dashboard(self) -> dict[str, object]:
        metrics = self.metrics()
        incidents = read_csv(self.processed / "incidentes_clasificados.csv")
        return {
            "period": "2025-01-01/2025-12-31",
            "source": "original incidents + academic simulation",
            "incident_count": len(incidents),
            "metrics": metrics,
            "status_summary": dict(Counter(row["status"] for row in metrics)),
            "incidents_by_characteristic": dict(Counter(row["characteristic"] for row in incidents)),
            "incidents_by_module": dict(Counter(row["modulo"] for row in incidents)),
        }

    def run_simulation(self, seed: int, event_count: int) -> dict[str, object]:
        simulation_id = hashlib.sha256(f"{seed}:{event_count}".encode()).hexdigest()[:12]
        run_dir = self.simulated / "runs" / simulation_id
        generate_files(run_dir, seed, event_count)
        result = {
            "simulation_id": simulation_id,
            "seed": seed,
            "event_count": event_count,
            "period": "2025-01-01/2025-12-31",
            "created_at": datetime.now(UTC).isoformat(),
            "status": "completed",
        }
        write_json(run_dir / "result.json", result)
        return result

    def simulation(self, simulation_id: str) -> dict[str, object] | None:
        result = self.simulated / "runs" / simulation_id / "result.json"
        if not result.exists():
            return None
        import json

        return json.loads(result.read_text(encoding="utf-8"))

    def register_survey(self, row: dict[str, object]) -> dict[str, object]:
        existing = read_csv(self.survey_log) if self.survey_log.exists() else []
        survey_id = f"MOB-{len(existing) + 1:05d}"
        record = {"survey_id": survey_id, "created_at": datetime.now(UTC).isoformat(), **row, "simulated": True}
        rows = [*existing, record]
        write_csv(self.survey_log, rows, list(record))
        return record

    def _calculate_metrics(self) -> None:
        metrics = MetricsCalculator().calculate(
            read_csv(self.simulated / "events.csv"),
            read_csv(self.simulated / "surveys.csv"),
            read_csv(self.processed / "incidentes_clasificados.csv"),
        )
        rows = [metric.to_dict() for metric in metrics]
        write_csv(self.processed / "metricas.csv", rows, list(rows[0]))
