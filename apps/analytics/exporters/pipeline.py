from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from apps.analytics.classification.classifier import classify_activity_file, classify_file
from apps.analytics.common.io import read_csv, write_csv, write_json
from apps.analytics.metrics.calculator import MetricsCalculator
from apps.analytics.simulation.generator import generate_files
from apps.analytics.validation import validate_events, validate_incidents, validate_surveys


def write_workshop_datasets(
    root: Path,
    events: list[dict[str, str]],
    surveys: list[dict[str, str]],
) -> None:
    """Export the literal CSV contracts requested in workshop scenario 7."""
    hce_rows = []
    for index, event in enumerate(
        (row for row in events if row["event_type"] == "hce_save"), start=1
    ):
        hce_rows.append(
            {
                "evento_id": event["event_id"],
                "timestamp": event["occurred_at"],
                "sede": event["site"],
                "medico_id": f"MED-{event['site'][:3].upper()}-{((index - 1) % 12) + 1:02d}",
                "tiempo_segundos": event["duration_seconds"],
                "completada": 1 if event["successful"].casefold() == "true" else 0,
            }
        )
    survey_rows = [
        {
            "respuesta_id": row["survey_id"],
            "sede": row["site"],
            "rol": row["role"],
            "puntaje_csat": row["csat"],
            "comentario": "Respuesta sintetica reproducible; sin datos personales.",
        }
        for row in surveys
    ]
    write_csv(
        root / "data/logs_hce.csv",
        hce_rows,
        ["evento_id", "timestamp", "sede", "medico_id", "tiempo_segundos", "completada"],
    )
    write_csv(
        root / "data/encuesta_satisfaccion.csv",
        survey_rows,
        ["respuesta_id", "sede", "rol", "puntaje_csat", "comentario"],
    )


def write_dashboard_indicators(
    root: Path, seed: int, metrics: list, events: list[dict[str, str]]
) -> None:
    hce_by_site: dict[str, list[float]] = {}
    for row in events:
        if row["event_type"] == "hce_save":
            hce_by_site.setdefault(row["site"], []).append(float(row["duration_seconds"]))
    efficiency = [
        {"sede": site, "tiempo_promedio_segundos": round(sum(values) / len(values), 2)}
        for site, values in sorted(hce_by_site.items())
    ]
    write_json(
        root / "dashboards/indicadores.json",
        {
            "metadata": {
                "norma": "ISO/IEC 25022",
                "periodo": "2025-01-01/2025-12-31",
                "semilla": seed,
                "simulado": True,
            },
            "metricas": {metric.code: metric.to_dict() for metric in metrics},
            "eficiencia_por_sede": efficiency,
        },
    )


def run_pipeline(root: Path, seed: int = 25022) -> dict[str, object]:
    original = root / "apps/data/original/incidentes_2025.csv"
    simulated = root / "apps/data/simulated"
    processed = root / "apps/data/processed"
    evidence = root / "reportes/evidencias/resultados"

    classify_file(original, processed / "incidentes_clasificados.csv", evidence / "clasificacion_resumen.json")
    classify_activity_file(
        root / "data/incidentes_2025.csv",
        root / "data/clasificacion/incidentes_clasificados.csv",
    )
    generate_files(simulated, seed, 6000)

    events = read_csv(simulated / "events.csv")
    surveys = read_csv(simulated / "surveys.csv")
    incidents = read_csv(processed / "incidentes_clasificados.csv")
    validate_events(events)
    validate_surveys(surveys)
    validate_incidents(incidents)
    write_workshop_datasets(root, events, surveys)
    metrics = MetricsCalculator().calculate(events, surveys, incidents)
    rows = [metric.to_dict() for metric in metrics]
    write_csv(processed / "metricas.csv", rows, list(rows[0]))
    status = Counter(metric.status for metric in metrics)
    summary = {
        "seed": seed,
        "period": "2025-01-01/2025-12-31",
        "metrics": rows,
        "status_summary": dict(status),
    }
    write_json(evidence / "metricas_resumen.json", summary)
    write_dashboard_indicators(root, seed, metrics, events)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Pipeline ISO/IEC 25022 de MediSalud")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--seed", type=int, default=25022)
    args = parser.parse_args()
    summary = run_pipeline(args.root.resolve(), args.seed)
    print(f"Pipeline completo: {len(summary['metrics'])} metricas, semilla {args.seed}")


if __name__ == "__main__":
    main()
