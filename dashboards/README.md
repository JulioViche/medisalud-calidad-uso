# Dashboard de Calidad en Uso

Entregable visual independiente del HIS para revisar las diez métricas calculadas
en el escenario de construcción de indicadores.

## Abrir

Abrir [`index.html`](index.html) directamente en un navegador. No requiere
Docker, React, conexión a Internet ni un servidor local.

## Contenido

- **Resumen ejecutivo:** diez KPI, metas, semáforo, distribución y prioridad.
- **Análisis de incidentes:** evolución mensual, módulos, características, filtros
  por sede, módulo, rol y clasificación, y tabla trazable.
- **Métricas y metodología:** fórmula, componentes `A` y `B`, fuente, procedencia
  y respuestas de discusión del escenario 9.

Los valores se corresponden con
`reportes/evidencias/resultados/metricas_resumen.json`. La aplicación HIS puede
producir evidencia, pero este dashboard constituye el entregable académico para
su análisis.

## Regenerar los datos

```bash
python scripts/reports/generate-dashboard-data.py
```

El generador une los 3.000 incidentes con sus 3.000 clasificaciones por `id`,
normaliza las fechas y crea `dashboard-data.js`. La ejecución se detiene si hay
identificadores duplicados, clasificaciones ausentes o cantidades inesperadas.
