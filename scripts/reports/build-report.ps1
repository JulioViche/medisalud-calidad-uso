$ErrorActionPreference = "Stop"
$root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$report = Join-Path $root "informe"
$build = Join-Path $report "build"
$delivery = Join-Path $report "entrega"
New-Item -ItemType Directory -Force -Path $build, $delivery | Out-Null
Push-Location $report
try {
    latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
    if ($LASTEXITCODE -ne 0) { throw "LaTeX compilation failed with exit code $LASTEXITCODE" }
    Copy-Item -LiteralPath "build\main.pdf" -Destination "entrega\medisalud_iso25022.pdf" -Force
} finally {
    Pop-Location
}
