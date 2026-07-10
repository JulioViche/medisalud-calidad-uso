# ADR-001: fuentes y periodos de datos

## Decision

El directorio `docs/Documento Padre` es la fuente academica primaria. El archivo `data/original/incidentes_2025.csv` es una copia de trabajo verificada por hash y no se modifica. Los eventos y encuestas son ficticios, reproducibles y se identifican con `simulated=true` y una semilla.

## Periodos

- Incidentes originales: 2 de enero a 19 de diciembre de 2025.
- Simulacion: 1 de enero a 31 de diciembre de 2025.
- Cada salida declara periodo, procedencia y semilla.

El README y los reportes existentes son material secundario sujeto a auditoria.

