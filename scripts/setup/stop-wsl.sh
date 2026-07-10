#!/usr/bin/env bash
set -euo pipefail
ROOT="/mnt/c/Users/mesia/Desktop/Universidad/Calidad/3P/Taller/1/medisalud-calidad-uso"
cd "$ROOT"
docker compose --env-file apps/infrastructure/docker/.env -f apps/infrastructure/docker/compose.yaml down
