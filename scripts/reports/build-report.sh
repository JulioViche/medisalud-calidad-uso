#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT/reportes"
mkdir -p build entrega
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
cp build/main.pdf entrega/medisalud_iso25022.pdf

