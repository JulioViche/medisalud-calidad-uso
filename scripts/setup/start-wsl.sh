#!/usr/bin/env bash
set -euo pipefail

ROOT="/mnt/c/Users/mesia/Desktop/Universidad/Calidad/3P/Taller/1/medisalud-calidad-uso"
cd "$ROOT"

if [[ ! -f infrastructure/docker/.env ]]; then
  cp infrastructure/docker/.env.example infrastructure/docker/.env
fi

docker compose --env-file infrastructure/docker/.env -f infrastructure/docker/compose.yaml config >/dev/null
docker compose --env-file infrastructure/docker/.env -f infrastructure/docker/compose.yaml up --build -d
docker compose --env-file infrastructure/docker/.env -f infrastructure/docker/compose.yaml ps

