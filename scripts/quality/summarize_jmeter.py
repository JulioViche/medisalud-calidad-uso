from __future__ import annotations

import csv
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path


def percentile(values: list[int], ratio: float) -> int:
    ordered = sorted(values)
    return ordered[min(len(ordered) - 1, math.ceil(len(ordered) * ratio) - 1)]


def main() -> None:
    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    with source.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise SystemExit("JMeter no produjo muestras")

    elapsed = [int(row["elapsed"]) for row in rows]
    successful = sum(row["success"].lower() == "true" for row in rows)
    started = min(int(row["timeStamp"]) for row in rows)
    finished = max(int(row["timeStamp"]) + int(row["elapsed"]) for row in rows)
    duration_seconds = max((finished - started) / 1000, 0.001)
    summary = {
        "test": "Portal de citas - 500 usuarios concurrentes",
        "started_at_utc": datetime.fromtimestamp(started / 1000, timezone.utc).isoformat(),
        "samples": len(rows),
        "successful": successful,
        "errors": len(rows) - successful,
        "error_rate_percent": round((len(rows) - successful) * 100 / len(rows), 2),
        "average_ms": round(sum(elapsed) / len(elapsed), 2),
        "min_ms": min(elapsed),
        "max_ms": max(elapsed),
        "p90_ms": percentile(elapsed, 0.90),
        "p95_ms": percentile(elapsed, 0.95),
        "throughput_requests_second": round(len(rows) / duration_seconds, 2),
        "duration_seconds": round(duration_seconds, 2),
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
