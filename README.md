# MediSalud HIS — Taller de Calidad en Uso ISO/IEC 25022

Evaluación de calidad en uso del sistema MediSalud HIS (historia clínica electrónica) aplicando el estándar **ISO/IEC 25022** sobre incidentes reales, logs de rendimiento y encuestas de satisfacción del período Ene–Feb 2025.

**Semáforo general:** *(ejecutar `python scripts/pipeline_medicion.py` para ver resultados)*

## Estructura

```
data/                  Datasets (originales y generados)
scripts/               Scripts Python (clasificación, pipeline, dashboard)
reportes/              Reportes en markdown (escenarios 2–12 + reto final)
dashboards/            Dashboard interactivo HTML (plotly)
docs/                  Análisis inicial e instrucciones del taller
```

## Entregables

| Archivo | Contenido |
|---------|-----------|
| [`docs/analisis_inicial.md`](docs/analisis_inicial.md) | Análisis del caso y 4 preguntas del taller |
| [`reportes/escenario02_clasificacion_incidentes.md`](reportes/escenario02_clasificacion_incidentes.md) | 3,000 incidentes clasificados en 5 características |
| [`reportes/escenario03_calidad_square.md`](reportes/escenario03_calidad_square.md) | Mapa SQuaRE y 3 niveles de calidad |
| [`reportes/escenario04_atributos_utc.md`](reportes/escenario04_atributos_utc.md) | 12 atributos UTC para MediSalud |
| [`reportes/escenario05_matriz_prioridades.md`](reportes/escenario05_matriz_prioridades.md) | Matriz tarea–característica–prioridad |
| [`reportes/escenario06_catalogo_metricas.md`](reportes/escenario06_catalogo_metricas.md) | Catálogo de 10 métricas ISO/IEC 25022 |
| [`reportes/escenario10_interpretacion_causa_raiz.md`](reportes/escenario10_interpretacion_causa_raiz.md) | Análisis de causa raíz |
| [`reportes/escenario11_presentacion_ejecutiva.md`](reportes/escenario11_presentacion_ejecutiva.md) | Resumen para dirección de TI |
| [`reportes/escenario12_plan_mejora_continua.md`](reportes/escenario12_plan_mejora_continua.md) | Ciclo PDCA con metas a Jul/Dic 2025 |
| [`reportes/reto_final_telemedicina_2_0.md`](reportes/reto_final_telemedicina_2_0.md) | Extensión Telemedicina (10 métricas + roadmap) |
| [`dashboards/dashboard_calidad_uso.html`](dashboards/dashboard_calidad_uso.html) | Dashboard interactivo con 7 KPI |

## Stack

- Python 3.12 + pandas, numpy, plotly
- ISO/IEC 25022 (SQuaRE — Quality in Use)
- Ciclo PDCA para mejora continua

## Instalación

```bash
python3 -m venv venv
source venv/bin/activate                  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución del pipeline

Los scripts deben ejecutarse en orden debido a las dependencias entre ellos:

| Orden | Comando | Genera |
|---|---|---|
| 1 | `python scripts/generar_datos_simulados.py` | `data/logs_hce.csv`, `data/encuestas_satisfaccion.csv` |
| 2 | `python scripts/clasificar_incidentes.py` | `data/incidentes_clasificados.csv` |
| 3 | `python scripts/pipeline_medicion.py` | `data/resultados_metricas.csv` |
| 4 | `python scripts/generar_dashboard.py` | `dashboards/dashboard_calidad_uso.html` |
