import pandas as pd
import re

df = pd.read_csv("data/incidentes_2025.csv")

keywords = {
    "Efectividad": [
        "no logra", "no permite", "error al", "falla", "no responde",
        "no se sincroniza", "no carga", "no aparece", "no se actualiza",
        "no se valida", "no se descuenta", "no descuenta", "no reconoce",
        "no refleja", "no se aplica", "no se genera", "no se visualizan",
        "no redirige", "no se almacena", "no se adjunta",
        "no devuelve resultados", "duplicado", "duplicidad",
        "doble reserva", "doble cobro", "cayo", "se cae",
        "tarea fallida", "falla de forma", "desactualizada impide",
        "se cierra inesperadamente", "no muestra", "no se muestra",
        "resultados no se visualizan", "no envía", "no envia",
        "sesion expira", "boton no responde", "perdida de la nota",
        "no se refleja tras completarlo", "sin mostrar el motivo",
    ],
    "Eficiencia": [
        "tarda", "retraso", "lentitud", "tiempo de carga", "tiempo de espera",
        "tiempo de respuesta", "supera los", "consume muchos datos",
        "consume elevado", "supera los minutos",
    ],
    "Satisfaccion": [
        "formulario confuso", "abandono de registro", "confuso",
        "pese a tener buena conexion", "calidad de video muy baja",
        "notificaciones push no llegan",
    ],
    "Libertad de Riesgo": [
        "datos de otro paciente visibles", "dosis incorrecta",
        "informacion sensible", "exposición", "datos visibles",
        "fuga", "privacidad", "seguridad", "alergias no carga",
        "codigo de barras no es reconocido", "alerta no se despliega",
        "interaccion medicamentosa", "bloquea la dispensacion",
    ],
    "Cobertura de Contexto": [
        "dispositivos moviles", "tablet", "app", "android", "ios",
        "movil", "moviles", "version desactualizada",
        "conexion limitada", "audio desincronizado",
        "videollamada se corta", "calidad de video muy baja",
        "no funciona en", "movil", "biometria falla",
    ],
}

def classify_incident(desc):
    desc_lower = desc.lower()
    for characteristic, patterns in keywords.items():
        for pattern in patterns:
            if re.search(pattern, desc_lower):
                return characteristic
    return "Efectividad"

df["caracteristica"] = df["descripcion"].apply(classify_incident)

summary = df["caracteristica"].value_counts()
print("Distribución por característica ISO/IEC 25022:")
print(summary)
print()

report = df[["id", "modulo", "descripcion", "caracteristica"]]
report.to_csv("data/incidentes_clasificados.csv", index=False)

print("Muestra de clasificación:")
print(report.head(20).to_string(index=False))
