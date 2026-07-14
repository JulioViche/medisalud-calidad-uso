# Acta AC-25022-2026-07-14

- Proyecto: MediSalud HIS, taller ISO/IEC 25022 parte 2.
- Fecha: 14 de julio de 2026, America/Guayaquil.
- Comando: `python -m unittest discover -s apps/analytics/tests -v`.
- Resultado: 36/36 casos aprobados; 0 fallos, 0 errores y 0 omitidos; 1,989 s.
- Pipeline previo: `python -m apps.analytics.exporters.pipeline --seed 25022`, aprobado con diez métricas.

## Cobertura detallada

La suite verifica los incidentes 1001--1006, precedencia de riesgo, normalización, fórmulas de efectividad, eficiencia, satisfacción, libertad de riesgo y cobertura de contexto, percentil P90, fronteras de aceptación, esquema de métricas, semilla reproducible, dominios, duplicados, rangos, contratos CSV/JSON, desagregación en cinco sedes, estructura del repositorio, mapa SQuaRE, fichas, catálogo, workflow y evidencia final.

## Consolidación

El catálogo consolidado contiene 50 casos: 36 analíticos actuales y 14 casos de API, Java, React, integración y Flutter preservados en el acta integral del 13 de julio. Todos constan como aprobados. Las fechas se conservan separadas para no presentar las suites históricas como reejecutadas el día 14.

## Dictamen

La suite ampliada cumple los controles de reproducción y trazabilidad de los escenarios 1--8. La aprobación se limita al prototipo y a los datos académicos identificados; no certifica un sistema clínico productivo.
