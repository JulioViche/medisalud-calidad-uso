# Escenario 5 — Mapeo de Características de Calidad

## Matriz de Priorización Tarea–Característica

Evaluación del impacto en el negocio y urgencia percibida para cada tarea crítica de MediSalud HIS.

### Matriz Completa

| Tarea | Efectividad | Eficiencia | Satisfacción | Libertad de Riesgo | Cobertura Contexto | Prioridad |
|---|---|---|---|---|---|---|
| Registrar nota de evolución HCE | **Alto** | **Alto** | Medio | **Alto** | Medio | **Crítica** |
| Agendar cita (portal web) | **Alto** | Medio | **Alto** | Bajo | Medio | **Alta** |
| Facturar consulta con seguro | **Alto** | Medio | Bajo | **Alto** | Bajo | **Crítica** |
| Realizar teleconsulta | Medio | Medio | **Alto** | Medio | **Alto** | **Alta** |
| Dispensar medicamento controlado | **Alto** | Bajo | Bajo | **Alto** | Bajo | **Crítica** |
| Registrar signos vitales (enfermería) | **Alto** | Medio | Bajo | Medio | Medio | **Alta** |
| Revisar historial de alergias | **Alto** | Medio | Bajo | **Alto** | Bajo | **Crítica** |
| Generar receta electrónica | **Alto** | Bajo | Bajo | **Alto** | Bajo | **Crítica** |
| Ver resultados de laboratorio (app) | **Alto** | Medio | Medio | Bajo | **Alto** | **Alta** |
| Iniciar sesión con biometría | Medio | Bajo | **Alto** | Medio | **Alto** | **Media** |

### Tareas Críticas (Prioridad Máxima)

| Tarea | Justificación |
|---|---|
| **Registrar nota de evolución HCE** | Impacta directamente la atención al paciente. Los incidentes muestran demoras de hasta 28s (RNF-01: debe ser ≤8s). Afecta a 640 médicos. |
| **Facturar consulta con seguro** | Errores de facturación duplicada >1% afectan el flujo de caja. Riesgo financiero y regulatorio. |
| **Dispensar medicamento controlado** | Error de dispensación = riesgo clínico grave. Incidentes como dosis incorrecta o duplicidad de códigos. |
| **Revisar historial de alergias** | Incidente #1210: historial de alergias no carga. Riesgo de prescribir un medicamento contraindicado. |
| **Generar receta electrónica** | Incidente #3980: dosis incorrecta al guardar. Riesgo directo a la salud del paciente. |

### Criterios de Priorización

1. **Impacto en el negocio**: evaluación del daño potencial (clínico, financiero, reputacional, regulatorio) si la tarea falla.
2. **Urgencia percibida por stakeholders**: basada en la frecuencia de incidentes reportados en `incidentes_2025.csv` y la criticidad del proceso.
