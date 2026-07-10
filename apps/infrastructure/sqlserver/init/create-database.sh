#!/usr/bin/env bash
set -euo pipefail

/opt/mssql-tools18/bin/sqlcmd \
  -S sqlserver \
  -U sa \
  -P "$SQLSERVER_PASSWORD" \
  -C \
  -Q "IF DB_ID('medisalud_finance') IS NULL CREATE DATABASE medisalud_finance"

