#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
COMPOSE=(docker compose --env-file "$ROOT/apps/infrastructure/docker/.env" -f "$ROOT/apps/infrastructure/docker/compose.yaml")
RAW="$ROOT/reportes/evidencias/calidad/jmeter/raw/citas-500-usuarios.jtl"
LOG="$ROOT/reportes/evidencias/calidad/jmeter/raw/jmeter.log"
SUMMARY="$ROOT/reportes/evidencias/calidad/jmeter/resumen.json"

mkdir -p "$(dirname "$RAW")"
rm -f "$RAW" "$LOG"
"${COMPOSE[@]}" up -d --build api-gateway
"${COMPOSE[@]}" --profile quality build jmeter
"${COMPOSE[@]}" --profile quality run --rm jmeter
python3 "$ROOT/scripts/quality/summarize_jmeter.py" "$RAW" "$SUMMARY"
