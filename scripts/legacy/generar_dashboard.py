import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json

df_metricas = pd.read_csv("data/resultados_metricas.csv")
logs_hce = pd.read_csv("data/logs_hce.csv")
incidentes = pd.read_csv("data/incidentes_clasificados.csv")
encuestas = pd.read_csv("data/encuestas_satisfaccion.csv")

colors = {"VERDE": "#2ecc71", "AMARILLO": "#f1c40f", "ROJO": "#e74c3c"}

# ────────────────────────────────────────────
# KPI 1: Semáforo general de métricas
# ────────────────────────────────────────────
fig1 = go.Figure()
for _, row in df_metricas.iterrows():
    fig1.add_trace(go.Bar(
        x=[row["codigo"]],
        y=[row["valor"]],
        name=row["codigo"],
        marker_color=colors[row["estado"]],
        text=f"{row['valor']} ({row['meta']})",
        textposition="outside",
        hovertemplate=f"{row['metrica']}<br>Valor: {row['valor']}<br>Meta: {row['meta']}<br>Estado: {row['estado']}"
    ))

fig1.update_layout(
    title="KPI 1: Métricas de Calidad en Uso vs. Meta",
    xaxis_title="Métrica",
    yaxis_title="Valor",
    showlegend=False,
    height=400,
    template="plotly_white"
)

# ────────────────────────────────────────────
# KPI 2: Tiempo promedio HCE por sede
# ────────────────────────────────────────────
tiempo_sede = logs_hce.groupby("sede")["tiempo_segundos"].agg(["mean", "std"]).reset_index()
tiempo_sede.columns = ["sede", "promedio", "desviacion"]

fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=tiempo_sede["sede"],
    y=tiempo_sede["promedio"],
    marker_color=["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6"],
    error_y=dict(type="data", array=tiempo_sede["desviacion"], visible=True),
    text=tiempo_sede["promedio"].round(1),
    textposition="outside"
))
fig2.add_hline(y=8, line_dash="dash", line_color="red", annotation_text="Meta: 8s")
fig2.update_layout(
    title="KPI 2: Tiempo Promedio HCE por Sede",
    xaxis_title="Sede",
    yaxis_title="Tiempo (s)",
    height=400,
    template="plotly_white"
)

# ────────────────────────────────────────────
# KPI 3: Distribución de incidentes por característica
# ────────────────────────────────────────────
inc_counts = incidentes["caracteristica"].value_counts()
color_map_inc = {
    "Efectividad": "#3498db",
    "Eficiencia": "#2ecc71",
    "Cobertura de Contexto": "#f39c12",
    "Libertad de Riesgo": "#e74c3c",
    "Satisfaccion": "#9b59b6"
}

fig3 = go.Figure(data=[go.Pie(
    labels=inc_counts.index,
    values=inc_counts.values,
    marker_colors=[color_map_inc.get(c, "#95a5a6") for c in inc_counts.index],
    textinfo="label+percent",
    hole=0.4
)])
fig3.update_layout(
    title="KPI 3: Incidentes por Característica ISO/IEC 25022",
    height=400,
    template="plotly_white"
)

# ────────────────────────────────────────────
# KPI 4: NPS por sede
# ────────────────────────────────────────────
nps_sede = encuestas.groupby("sede")["nps"].mean().reset_index()
nps_sede.columns = ["sede", "nps_promedio"]

fig4 = go.Figure()
fig4.add_trace(go.Bar(
    x=nps_sede["sede"],
    y=nps_sede["nps_promedio"],
    marker_color=["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6"],
    text=nps_sede["nps_promedio"].round(1),
    textposition="outside"
))
fig4.add_hline(y=7, line_dash="dash", line_color="green", annotation_text="Meta: 7.0")
fig4.update_layout(
    title="KPI 4: NPS Promedio por Sede",
    xaxis_title="Sede",
    yaxis_title="NPS (1-10)",
    height=400,
    template="plotly_white"
)

# ────────────────────────────────────────────
# KPI 5: Tasa de éxito por hora pico
# ────────────────────────────────────────────
exito_pico = logs_hce.groupby("es_hora_pico")["exitosa"].mean().reset_index()
exito_pico["es_hora_pico"] = exito_pico["es_hora_pico"].map({True: "Hora Pico", False: "Fuera de Pico"})
exito_pico["exitosa"] = exito_pico["exitosa"] * 100

fig5 = go.Figure()
fig5.add_trace(go.Bar(
    x=exito_pico["es_hora_pico"],
    y=exito_pico["exitosa"],
    marker_color=["#e74c3c", "#2ecc71"],
    text=exito_pico["exitosa"].round(1).astype(str) + "%",
    textposition="outside"
))
fig5.add_hline(y=95, line_dash="dash", line_color="green", annotation_text="Meta: 95%")
fig5.update_layout(
    title="KPI 5: Tasa de Éxito por Hora Pico",
    xaxis_title="",
    yaxis_title="Tasa de éxito (%)",
    height=400,
    template="plotly_white"
)

# ────────────────────────────────────────────
# KPI 6: Incidentes por módulo
# ────────────────────────────────────────────
inc_modulo = incidentes["modulo"].value_counts().reset_index()
inc_modulo.columns = ["modulo", "cantidad"]

fig6 = go.Figure()
fig6.add_trace(go.Bar(
    x=inc_modulo["modulo"],
    y=inc_modulo["cantidad"],
    marker_color="#e74c3c",
    text=inc_modulo["cantidad"],
    textposition="outside"
))
fig6.update_layout(
    title="KPI 6: Incidentes por Módulo",
    xaxis_title="Módulo",
    yaxis_title="Cantidad de incidentes",
    height=400,
    template="plotly_white"
)

# ────────────────────────────────────────────
# KPI 7: Distribución CSAT
# ────────────────────────────────────────────
csat_dist = encuestas["csat"].value_counts().sort_index().reset_index()
csat_dist.columns = ["csat", "cantidad"]
csat_dist["csat"] = csat_dist["csat"].astype(str)

fig7 = go.Figure()
fig7.add_trace(go.Bar(
    x=csat_dist["csat"],
    y=csat_dist["cantidad"],
    marker_color=["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#27ae60"],
    text=csat_dist["cantidad"],
    textposition="outside"
))
fig7.update_layout(
    title="KPI 7: Distribución CSAT (1-5)",
    xaxis_title="Puntuación CSAT",
    yaxis_title="Cantidad de respuestas",
    height=400,
    template="plotly_white"
)

# ────────────────────────────────────────────
# COMPONER DASHBOARD
# ────────────────────────────────────────────
import plotly.io as pio

html_parts = [
    "<html><head><meta charset='utf-8'><title>Dashboard Calidad en Uso — MediSalud HIS</title>",
    "<link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap' rel='stylesheet'>",
    "<style>",
    "body { font-family: 'Inter', sans-serif; margin: 0; padding: 20px; background: #f8f9fa; }",
    "h1 { color: #2c3e50; font-weight: 700; }",
    ".subtitle { color: #7f8c8d; font-size: 14px; margin-bottom: 30px; }",
    ".grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }",
    ".card { background: white; border-radius: 12px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }",
    ".card-full { grid-column: 1 / -1; }",
    ".header { display: flex; justify-content: space-between; align-items: center; }",
    ".status { display: flex; gap: 15px; }",
    ".status-item { padding: 8px 16px; border-radius: 20px; font-weight: 600; font-size: 13px; }",
    ".status-verde { background: #d4edda; color: #155724; }",
    ".status-amarillo { background: #fff3cd; color: #856404; }",
    ".status-rojo { background: #f8d7da; color: #721c24; }",
    "@media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }",
    "</style></head><body>",
    "<div class='header'>",
    "<div><h1>MediSalud HIS — Calidad en Uso</h1>",
    "<div class='subtitle'>Dashboard ISO/IEC 25022 | Período: Ene-Feb 2025</div></div>",
    "<div class='status'>",
    f"<span class='status-item status-verde'>VERDE: {len(df_metricas[df_metricas['estado']=='VERDE'])}</span>",
    f"<span class='status-item status-amarillo'>AMARILLO: {len(df_metricas[df_metricas['estado']=='AMARILLO'])}</span>",
    f"<span class='status-item status-rojo'>ROJO: {len(df_metricas[df_metricas['estado']=='ROJO'])}</span>",
    "</div></div><div class='grid'>",
    "<div class='card card-full'>" + pio.to_html(fig1, full_html=False, include_plotlyjs='cdn') + "</div>",
    "<div class='card'>" + pio.to_html(fig2, full_html=False, include_plotlyjs=False) + "</div>",
    "<div class='card'>" + pio.to_html(fig3, full_html=False, include_plotlyjs=False) + "</div>",
    "<div class='card'>" + pio.to_html(fig4, full_html=False, include_plotlyjs=False) + "</div>",
    "<div class='card'>" + pio.to_html(fig5, full_html=False, include_plotlyjs=False) + "</div>",
    "<div class='card'>" + pio.to_html(fig6, full_html=False, include_plotlyjs=False) + "</div>",
    "<div class='card'>" + pio.to_html(fig7, full_html=False, include_plotlyjs=False) + "</div>",
    "</div></body></html>"
]

with open("dashboards/dashboard_calidad_uso.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html_parts))

print("Dashboard generado: dashboards/dashboard_calidad_uso.html")
