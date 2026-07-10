from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from apps.analytics.classification.classifier import classify_activity_file, classify_file
from apps.analytics.common.io import read_csv, write_csv, write_json
from apps.analytics.metrics.calculator import MetricsCalculator
from apps.analytics.simulation.generator import generate_files


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

    metrics = MetricsCalculator().calculate(
        read_csv(simulated / "events.csv"),
        read_csv(simulated / "surveys.csv"),
        read_csv(processed / "incidentes_clasificados.csv"),
    )
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
