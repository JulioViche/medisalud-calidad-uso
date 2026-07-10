#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
COMPOSE=(docker compose --env-file "$ROOT/apps/infrastructure/docker/.env" -f "$ROOT/apps/infrastructure/docker/compose.yaml")
OUTPUT="$ROOT/reportes/evidencias/calidad/sonarqube/metricas.json"

"${COMPOSE[@]}" --profile quality up -d sonar-db sonarqube

for _ in $(seq 1 90); do
  if curl -fsS http://localhost:9000/api/system/status | grep -q '"status":"UP"'; then
    break
  fi
  sleep 5
done
curl -fsS http://localhost:9000/api/system/status | grep -q '"status":"UP"'

TOKEN="${SONAR_TOKEN:-}"
GENERATED_TOKEN_NAME=""
if [[ -z "$TOKEN" ]]; then
  TOKEN_NAME="medisalud-local-$(date +%s)"
  RESPONSE="$(curl -fsS -u "${SONAR_ADMIN_USER:-admin}:${SONAR_ADMIN_PASSWORD:-admin}" -X POST "http://localhost:9000/api/user_tokens/generate?name=$TOKEN_NAME")"
  TOKEN="$(printf '%s' "$RESPONSE" | python3 -c 'import json,sys; print(json.load(sys.stdin)["token"])')"
  GENERATED_TOKEN_NAME="$TOKEN_NAME"
fi

SONAR_TOKEN="$TOKEN" "${COMPOSE[@]}" --profile quality run --rm -e SONAR_TOKEN="$TOKEN" sonar-scanner-billing
mkdir -p "$(dirname "$OUTPUT")"
rm -f "$OUTPUT"
METRICS_URL="http://localhost:9000/api/measures/component?component=medisalud-billing&metricKeys=complexity,cognitive_complexity,ncloc,code_smells,bugs,vulnerabilities,coverage,duplicated_lines_density"
for _ in $(seq 1 30); do
  RESPONSE="$(curl -fsS -u "$TOKEN:" "$METRICS_URL")"
  COUNT="$(printf '%s' "$RESPONSE" | python3 -c 'import json,sys; print(len(json.load(sys.stdin)["component"]["measures"]))')"
  if [[ "$COUNT" -gt 0 ]]; then
    printf '%s' "$RESPONSE" > "$OUTPUT"
    break
  fi
  sleep 2
done
[[ -s "$OUTPUT" ]] || { echo "SonarQube no publicó métricas" >&2; exit 1; }
python3 -m json.tool "$OUTPUT" "$OUTPUT.tmp"
mv "$OUTPUT.tmp" "$OUTPUT"
cat "$OUTPUT"
if [[ -n "$GENERATED_TOKEN_NAME" ]]; then
  curl -fsS -u "$TOKEN:" -X POST "http://localhost:9000/api/user_tokens/revoke?name=$GENERATED_TOKEN_NAME" >/dev/null || true
fi
