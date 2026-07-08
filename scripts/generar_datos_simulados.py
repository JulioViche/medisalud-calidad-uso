import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

fecha_inicio = datetime(2025, 1, 1)
fecha_fin = datetime(2025, 2, 28)
dias = (fecha_fin - fecha_inicio).days

sedes = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
roles = ["Medico", "Enfermeria", "Admision"]
horarios = ["manana", "tarde", "noche"]

logs = []
for i in range(5000):
    fecha = fecha_inicio + timedelta(
        days=np.random.randint(0, dias),
        hours=np.random.randint(7, 19),
        minutes=np.random.randint(0, 60),
        seconds=np.random.randint(0, 60)
    )
    sede = np.random.choice(sedes, p=[0.3, 0.25, 0.2, 0.15, 0.1])
    rol = np.random.choice(roles, p=[0.4, 0.35, 0.25])
    hora = fecha.hour
    es_pico = 10 <= hora <= 12
    tiempo_base = np.random.normal(6, 2)
    if es_pico:
        tiempo_base *= np.random.uniform(1.5, 3.0)
    if sede == "Manta":
        tiempo_base *= np.random.uniform(1.2, 1.5)
    tiempo = max(0.5, round(tiempo_base, 1))

    logs.append({
        "id_transaccion": f"TXN-{i+1:05d}",
        "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
        "sede": sede,
        "rol_usuario": rol,
        "modulo": "HCE",
        "accion": "registrar_nota_evolucion",
        "tiempo_segundos": tiempo,
        "es_hora_pico": es_pico,
        "exitosa": 1 if tiempo < 20 else 0
    })

df_logs = pd.DataFrame(logs)
df_logs.to_csv("data/logs_hce.csv", index=False)
print(f"logs_hce.csv: {len(df_logs)} registros")

encuestas = []
for i in range(2000):
    fecha = fecha_inicio + timedelta(days=np.random.randint(0, dias))
    sede = np.random.choice(sedes, p=[0.3, 0.25, 0.2, 0.15, 0.1])
    rol = np.random.choice(roles + ["Paciente"], p=[0.2, 0.15, 0.1, 0.55])
    nps = np.random.randint(1, 11)
    csat = np.random.randint(1, 6)
    if sede == "Manta":
        nps = max(1, nps - np.random.randint(1, 3))
        csat = max(1, csat - np.random.randint(1, 2))

    encuestas.append({
        "id_encuesta": f"ENC-{i+1:05d}",
        "fecha": fecha.strftime("%Y-%m-%d"),
        "sede": sede,
        "rol_usuario": rol,
        "nps": nps,
        "csat": csat,
        "recomendaria": "si" if nps >= 7 else "no" if nps <= 3 else "tal_vez"
    })

df_enc = pd.DataFrame(encuestas)
df_enc.to_csv("data/encuestas_satisfaccion.csv", index=False)
print(f"encuestas_satisfaccion.csv: {len(df_enc)} registros")

print("\nResumen logs HCE:")
print(df_logs["tiempo_segundos"].describe())
print("\nResumen encuestas:")
print(df_enc[["nps", "csat"]].describe())
