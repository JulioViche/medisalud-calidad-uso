from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INCIDENTS_PATH = ROOT / "data" / "incidentes_2025.csv"
CLASSIFICATIONS_PATH = ROOT / "data" / "clasificacion" / "incidentes_clasificados.csv"
METRICS_PATH = ROOT / "reportes" / "evidencias" / "resultados" / "metricas_resumen.json"
OUTPUT_PATH = ROOT / "dashboards" / "dashboard-data.js"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


def parse_date(value: str) -> datetime:
    for pattern in ("%m/%d/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, pattern)
        except ValueError:
            continue
    raise ValueError(f"Fecha no reconocida: {value}")


def ordered_counts(values: list[str]) -> dict[str, int]:
    return dict(Counter(values).most_common())


def main() -> None:
    incidents = read_csv(INCIDENTS_PATH)
    classifications = read_csv(CLASSIFICATIONS_PATH)
    classification_by_id = {row["id"]: row for row in classifications}

    if len(incidents) != 3000 or len(classifications) != 3000:
        raise ValueError("Se esperaban exactamente 3.000 incidentes y 3.000 clasificaciones")
    if len(classification_by_id) != len(classifications):
        raise ValueError("La clasificación contiene identificadores duplicados")

    joined = []
    for incident in incidents:
        classification = classification_by_id.get(incident["id"])
        if classification is None:
            raise ValueError(f"Falta clasificación para el incidente {incident['id']}")
        date = parse_date(incident["fecha"])
        joined.append(
            {
                "id": incident["id"],
                "date": date.strftime("%Y-%m-%d"),
                "month": date.strftime("%Y-%m"),
                "module": incident["modulo"],
                "description": incident["descripcion"],
                "role": incident["rol_usuario"],
                "site": incident["sede"],
                "characteristic": classification["caracteristica"],
                "justification": classification["justificacion"],
            }
        )

    with METRICS_PATH.open(encoding="utf-8") as source:
        metric_summary = json.load(source)

    payload = {
        "generatedFrom": [
            "data/incidentes_2025.csv",
            "data/clasificacion/incidentes_clasificados.csv",
            "reportes/evidencias/resultados/metricas_resumen.json",
        ],
        "incidentCount": len(joined),
        "dateRange": {
            "start": min(row["date"] for row in joined),
            "end": max(row["date"] for row in joined),
        },
        "metrics": metric_summary["metrics"],
        "metricSeed": metric_summary["seed"],
        "metricPeriod": metric_summary["period"],
        "distributions": {
            "characteristic": ordered_counts([row["characteristic"] for row in joined]),
            "module": ordered_counts([row["module"] for row in joined]),
            "site": ordered_counts([row["site"] for row in joined]),
            "role": ordered_counts([row["role"] for row in joined]),
            "month": dict(sorted(Counter(row["month"] for row in joined).items())),
        },
        "incidents": joined,
    }
    content = "window.dashboardData = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n"
    OUTPUT_PATH.write_text(content, encoding="utf-8")
    print(f"Dashboard: {len(joined)} incidentes y {len(payload['metrics'])} métricas -> {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
