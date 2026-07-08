"""
Pipeline de Automatización de Medición de Calidad en Uso
Basado en ISO/IEC 25022 — Caso MediSalud HIS

Flujo:
  1. Extraer datos (logs, encuestas, incidentes)
  2. Calcular métricas del catálogo (Escenario 6)
  3. Generar reporte CSV con resultados
  4. Determinar semáforo (verde/amarillo/rojo) vs metas
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime

# ──────────────────────────────────────────────────────────
# 1. EXTRACCIÓN
# ──────────────────────────────────────────────────────────

print("=" * 60)
print("PIPELINE DE MEDICIÓN — CALIDAD EN USO ISO/IEC 25022")
print(f"Ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)

logs_hce = pd.read_csv("data/logs_hce.csv")
encuestas = pd.read_csv("data/encuestas_satisfaccion.csv")
incidentes = pd.read_csv("data/incidentes_clasificados.csv")

print(f"\n[OK] Logs HCE: {len(logs_hce)} registros")
print(f"[OK] Encuestas: {len(encuestas)} registros")
print(f"[OK] Incidentes: {len(incidentes)} registros")

# ──────────────────────────────────────────────────────────
# 2. CÁLCULO DE MÉTRICAS
# ──────────────────────────────────────────────────────────

metricas = []

# M-EFI-01: Tiempo promedio de registro HCE
tiempo_promedio = logs_hce["tiempo_segundos"].mean()
p90_tiempo = logs_hce["tiempo_segundos"].quantile(0.9)
metricas.append({
    "codigo": "M-EFI-01",
    "metrica": "Tiempo promedio registro HCE",
    "caracteristica": "Eficiencia",
    "valor": round(tiempo_promedio, 2),
    "unidad": "segundos",
    "meta": "<= 8.0",
    "estado": "VERDE" if tiempo_promedio <= 8 else "AMARILLO" if tiempo_promedio <= 12 else "ROJO"
})

# M-EFI-01b: Percentil 90 tiempo HCE
metricas.append({
    "codigo": "M-EFI-01b",
    "metrica": "P90 tiempo registro HCE",
    "caracteristica": "Eficiencia",
    "valor": round(p90_tiempo, 2),
    "unidad": "segundos",
    "meta": "<= 12.0",
    "estado": "VERDE" if p90_tiempo <= 12 else "AMARILLO" if p90_tiempo <= 18 else "ROJO"
})

# M-SAT-01: NPS promedio
nps_promedio = encuestas["nps"].mean()
metricas.append({
    "codigo": "M-SAT-01",
    "metrica": "NPS promedio",
    "caracteristica": "Satisfacción",
    "valor": round(nps_promedio, 2),
    "unidad": "puntos (1-10)",
    "meta": "≥ 7.0",
    "estado": "VERDE" if nps_promedio >= 7 else "AMARILLO" if nps_promedio >= 4 else "ROJO"
})

# M-SAT-02: CSAT promedio
csat_promedio = encuestas["csat"].mean()
metricas.append({
    "codigo": "M-SAT-02",
    "metrica": "CSAT promedio",
    "caracteristica": "Satisfacción",
    "valor": round(csat_promedio, 2),
    "unidad": "puntos (1-5)",
    "meta": "≥ 4.0",
    "estado": "VERDE" if csat_promedio >= 4 else "AMARILLO" if csat_promedio >= 2.5 else "ROJO"
})

# M-EFE-01: Tasa de éxito transacciones HCE
tasa_exito = (logs_hce["exitosa"].sum() / len(logs_hce)) * 100
metricas.append({
    "codigo": "M-EFE-01",
    "metrica": "Tasa de éxito transacciones HCE",
    "caracteristica": "Efectividad",
    "valor": round(tasa_exito, 2),
    "unidad": "%",
    "meta": "≥ 95%",
    "estado": "VERDE" if tasa_exito >= 95 else "AMARILLO" if tasa_exito >= 85 else "ROJO"
})

# M-RIE-01: Tasa de incidentes Libertad de Riesgo
total_incidentes = len(incidentes)
inc_riesgo = len(incidentes[incidentes["caracteristica"] == "Libertad de Riesgo"])
tasa_riesgo = (inc_riesgo / total_incidentes) * 100
metricas.append({
    "codigo": "M-RIE-01",
    "metrica": "Incidentes de Libertad de Riesgo",
    "caracteristica": "Libertad de Riesgo",
    "valor": round(tasa_riesgo, 2),
    "unidad": "% del total",
    "meta": "< 3%",
    "estado": "VERDE" if tasa_riesgo < 3 else "AMARILLO" if tasa_riesgo < 6 else "ROJO"
})

# Tasa de incidentes de Eficiencia
inc_eficiencia = len(incidentes[incidentes["caracteristica"] == "Eficiencia"])
tasa_eficiencia = (inc_eficiencia / total_incidentes) * 100
metricas.append({
    "codigo": "M-EFI-02",
    "metrica": "Incidentes de Eficiencia",
    "caracteristica": "Eficiencia",
    "valor": round(tasa_eficiencia, 2),
    "unidad": "% del total",
    "meta": "< 8%",
    "estado": "VERDE" if tasa_eficiencia < 8 else "AMARILLO" if tasa_eficiencia < 15 else "ROJO"
})

# M-CC-01: Variabilidad tiempo HCE por sede
tiempo_por_sede = logs_hce.groupby("sede")["tiempo_segundos"].mean()
variabilidad = tiempo_por_sede.std()
metricas.append({
    "codigo": "M-CC-01",
    "metrica": "Variabilidad tiempo HCE por sede (σ)",
    "caracteristica": "Cobertura de Contexto",
    "valor": round(variabilidad, 2),
    "unidad": "segundos",
    "meta": "<= 2.0",
    "estado": "VERDE" if variabilidad <= 2 else "AMARILLO" if variabilidad <= 4 else "ROJO"
})

# Tasa de abandono de teleconsulta (proxy desde encuestas)
tasa_abandono = (encuestas["recomendaria"].value_counts().get("no", 0) / len(encuestas)) * 100
metricas.append({
    "codigo": "M-SAT-03",
    "metrica": "Tasa de no recomendación (proxy abandono)",
    "caracteristica": "Satisfacción",
    "valor": round(tasa_abandono, 2),
    "unidad": "%",
    "meta": "< 15%",
    "estado": "VERDE" if tasa_abandono < 15 else "AMARILLO" if tasa_abandono < 25 else "ROJO"
})

# ──────────────────────────────────────────────────────────
# 3. REPORTE
# ──────────────────────────────────────────────────────────

df_metricas = pd.DataFrame(metricas)

print("\n" + "=" * 60)
print("RESULTADOS — MÉTRICAS DE CALIDAD EN USO")
print("=" * 60)
print(df_metricas.to_string(index=False))

df_metricas.to_csv("data/resultados_metricas.csv", index=False)
print(f"\n[OK] Reporte exportado: data/resultados_metricas.csv")

resumen_estado = df_metricas["estado"].value_counts()
print(f"\nResumen de semáforo:")
for estado, count in resumen_estado.items():
    print(f"  {estado}: {count} métricas")
