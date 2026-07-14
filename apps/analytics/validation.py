from __future__ import annotations

from datetime import datetime

from apps.analytics.simulation.generator import EVENT_TYPES, SITES


class DataValidationError(ValueError):
    """A dataset cannot support trustworthy ISO/IEC 25022 metrics."""


def _shape(rows: list[dict[str, str]], fields: set[str], name: str) -> None:
    if not rows:
        raise DataValidationError(f"{name}: conjunto vacio")
    missing = fields - set(rows[0])
    if missing:
        raise DataValidationError(f"{name}: faltan columnas {sorted(missing)}")
    for number, row in enumerate(rows, 2):
        empty = [key for key in fields if not str(row.get(key, "")).strip()]
        if empty:
            raise DataValidationError(f"{name}: fila {number} contiene vacios en {sorted(empty)}")


def _unique(rows: list[dict[str, str]], field: str, name: str) -> None:
    values = [str(row[field]).strip() for row in rows]
    if len(values) != len(set(values)):
        raise DataValidationError(f"{name}: {field} contiene duplicados")


def _number(value: str, field: str, name: str, number: int) -> float:
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise DataValidationError(f"{name}: {field} no numerico en fila {number}") from exc


def validate_events(rows: list[dict[str, str]]) -> None:
    fields = {
        "event_id", "occurred_at", "site", "role", "module", "event_type",
        "duration_seconds", "successful", "iso_characteristic", "seed", "simulated",
    }
    _shape(rows, fields, "eventos")
    _unique(rows, "event_id", "eventos")
    for number, row in enumerate(rows, 2):
        if row["site"] not in SITES or row["event_type"] not in EVENT_TYPES:
            raise DataValidationError(f"eventos: sede o tipo invalido en fila {number}")
        duration = _number(row["duration_seconds"], "duration_seconds", "eventos", number)
        if duration <= 0 or (row["event_type"] == "hce_save" and duration > 120):
            raise DataValidationError(f"eventos: duracion fuera de rango en fila {number}")
        if row["successful"].casefold() not in {"true", "false"}:
            raise DataValidationError(f"eventos: successful invalido en fila {number}")
        try:
            datetime.fromisoformat(row["occurred_at"])
        except ValueError as exc:
            raise DataValidationError(f"eventos: fecha invalida en fila {number}") from exc


def validate_surveys(rows: list[dict[str, str]]) -> None:
    fields = {
        "survey_id", "date", "site", "role", "csat", "nps", "completed", "seed", "simulated",
    }
    _shape(rows, fields, "encuestas")
    _unique(rows, "survey_id", "encuestas")
    for number, row in enumerate(rows, 2):
        if row["site"] not in SITES:
            raise DataValidationError(f"encuestas: sede invalida en fila {number}")
        csat = _number(row["csat"], "csat", "encuestas", number)
        nps = _number(row["nps"], "nps", "encuestas", number)
        if not 1 <= csat <= 5 or not 0 <= nps <= 10:
            raise DataValidationError(f"encuestas: puntaje fuera de rango en fila {number}")
        if row["completed"].casefold() not in {"true", "false"}:
            raise DataValidationError(f"encuestas: completed invalido en fila {number}")
        try:
            datetime.fromisoformat(row["date"])
        except ValueError as exc:
            raise DataValidationError(f"encuestas: fecha invalida en fila {number}") from exc


def validate_incidents(rows: list[dict[str, str]]) -> None:
    fields = {"id", "fecha", "modulo", "descripcion", "rol_usuario", "sede"}
    _shape(rows, fields, "incidentes")
    _unique(rows, "id", "incidentes")
    for number, row in enumerate(rows, 2):
        if row["sede"] not in SITES:
            raise DataValidationError(f"incidentes: sede invalida en fila {number}")
