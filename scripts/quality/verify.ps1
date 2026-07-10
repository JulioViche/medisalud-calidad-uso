$ErrorActionPreference = "Stop"
$root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Push-Location $root
try {
    python -m unittest discover -s apps/analytics/tests -v
    python -m apps.analytics.exporters.pipeline --seed 25022
    python -m unittest discover -s apps/tests/integration -v

    Push-Location apps/web-his
    try { npm test; npm run build } finally { Pop-Location }

    Push-Location apps/mobile-patient
    try { flutter analyze; flutter build web --no-pub --no-wasm-dry-run } finally { Pop-Location }

    powershell -ExecutionPolicy Bypass -File scripts/reports/build-report.ps1
} finally {
    Pop-Location
}
