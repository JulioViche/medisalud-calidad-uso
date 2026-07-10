from __future__ import annotations

import argparse
import re
from pathlib import Path

from apps.analytics.common.io import read_csv, write_csv, write_json
from apps.analytics.common.models import Classification


RULES: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    (
        "Libertad de Riesgo",
        "El incidente puede causar dano clinico, financiero, de privacidad o seguridad.",
        (
            "otro paciente", "dosis incorrecta", "alergia", "interaccion", "privacidad",
            "datos visibles", "informacion sensible", "doble factur", "doble cobro",
            "factura duplicada", "nota de credito", "bloquea la dispensacion",
        ),
    ),
    (
        "Cobertura de Contexto",
        "El resultado depende del dispositivo, conectividad, sede o contexto de operacion.",
        (
            "android", "ios", "movil", "tablet", "biometr", "conexion limitada",
            "videollamada", "audio desincronizado", "version desactualizada", "manta",
        ),
    ),
    (
        "Satisfaccion",
        "La descripcion evidencia frustracion, confusion, abandono o baja percepcion del servicio.",
        (
            "confuso", "abandono", "no llegan", "calidad de video", "difícil",
            "dificil", "molesto", "incomprensible",
        ),
    ),
    (
        "Eficiencia",
        "La tarea consume mas tiempo o recursos de los esperados.",
        (
            "tarda", "lentitud", "retraso", "tiempo de", "demora", "supera los",
            "consume", "congela", "se congela",
        ),
    ),
    (
        "Efectividad",
        "El usuario no logra completar la tarea o el resultado es incorrecto.",
        (
            "no logra", "no permite", "falla", "error", "no responde", "no carga",
            "no aparece", "no se", "duplicad", "no muestra", "se cierra", "expira",
            "incorrect", "perdida", "no funciona",
        ),
    ),
)


class IncidentClassifier:
    """Deterministic classifier with risk-first precedence."""

    def classify(self, description: str) -> Classification:
        normalized = self._normalize(description)
        for characteristic, justification, patterns in RULES:
            for pattern in patterns:
                if pattern in normalized:
                    return Classification(characteristic, justification, pattern)
        return Classification(
            "Efectividad",
            "El incidente describe un resultado funcional que debe revisarse para completar la tarea.",
            "regla_por_defecto",
        )

    @staticmethod
    def _normalize(value: str) -> str:
        return re.sub(r"\s+", " ", value.strip().lower())


def classify_file(source: Path, target: Path, summary_target: Path) -> None:
    classifier = IncidentClassifier()
    output: list[dict[str, object]] = []
    summary: dict[str, int] = {}
    for incident in read_csv(source):
        result = classifier.classify(incident["descripcion"])
        row = {**incident, **result.to_dict()}
        output.append(row)
        summary[result.characteristic] = summary.get(result.characteristic, 0) + 1

    fields = [
        "id", "fecha", "modulo", "descripcion", "rol_usuario", "sede",
        "characteristic", "justification", "matched_rule",
    ]
    write_csv(target, output, fields)
    write_json(summary_target, {"total": len(output), "distribution": summary})


def classify_activity_file(source: Path, target: Path) -> None:
    """Build the three-column classification table required by the workshop."""
    classifier = IncidentClassifier()
    output: list[dict[str, str]] = []
    for incident in read_csv(source):
        description = incident["descripcion"]
        result = classifier.classify(description)
        output.append(
            {
                "id": incident["id"],
                "justificacion": _activity_justification(description, result.characteristic),
                "caracteristica": result.characteristic,
            }
        )

    write_csv(target, output, ["id", "justificacion", "caracteristica"])


def _activity_justification(description: str, characteristic: str) -> str:
    effect = {
        "Efectividad": "impide completar la tarea o produce un resultado funcional incorrecto",
        "Eficiencia": "obliga a emplear mas tiempo o recursos de los aceptables para completar la tarea",
        "Satisfaccion": "evidencia confusion, frustracion o abandono y reduce la disposicion de uso",
        "Libertad de Riesgo": "puede ocasionar dano clinico, financiero, de privacidad o de seguridad",
        "Cobertura de Contexto": "muestra que el resultado cambia segun dispositivo, conectividad o contexto de operacion",
    }[characteristic]
    return f'Se clasifica como {characteristic} porque "{description}" {effect}.'


def main() -> None:
    parser = argparse.ArgumentParser(description="Clasifica incidentes MediSalud segun ISO/IEC 25022")
    parser.add_argument("--source", type=Path, default=Path("apps/data/original/incidentes_2025.csv"))
    parser.add_argument("--target", type=Path, default=Path("apps/data/processed/incidentes_clasificados.csv"))
    parser.add_argument(
        "--summary",
        type=Path,
        default=Path("reportes/evidencias/resultados/clasificacion_resumen.json"),
    )
    parser.add_argument(
        "--activity-source",
        type=Path,
        default=Path("data/incidentes_2025.csv"),
    )
    parser.add_argument(
        "--activity-target",
        type=Path,
        default=Path("data/clasificacion/incidentes_clasificados.csv"),
    )
    args = parser.parse_args()
    classify_file(args.source, args.target, args.summary)
    classify_activity_file(args.activity_source, args.activity_target)


if __name__ == "__main__":
    main()
