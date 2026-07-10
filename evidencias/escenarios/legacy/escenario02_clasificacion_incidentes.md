# Escenario 2 — Comprensión de ISO/IEC 25022

## Clasificación de Incidentes según las 5 Características

### Dataset: `data/incidentes_2025.csv`
- **Total de incidentes clasificados:** 3,000
- **Período:** Enero – Febrero 2025
- **Módulos cubiertos:** HCE, Portal Citas, Facturación, Farmacia, Telemedicina, App Móvil, Laboratorio, Imagenología, Reportes Gerenciales

### Distribución General

| Característica | Cantidad | % |
|---|---|---|
| Efectividad | 2,223 | 74.1% |
| Eficiencia | 323 | 10.8% |
| Cobertura de Contexto | 199 | 6.6% |
| Libertad de Riesgo | 153 | 5.1% |
| Satisfacción | 102 | 3.4% |
| **Total** | **3,000** | **100%** |

### Distribución por Módulo y Característica

| Módulo | Efectividad | Eficiencia | Satisfacción | Libertad de Riesgo | Cobertura Contexto |
|---|---|---|---|---|---|
| HCE | 505 | 111 | 0 | 153 | 0 |
| Portal Citas | 472 | 38 | 35 | 0 | 0 |
| Facturación | 365 | 35 | 0 | 0 | 25 |
| Farmacia | 224 | 34 | 0 | 0 | 0 |
| Telemedicina | 189 | 31 | 28 | 0 | 72 |
| App Móvil | 174 | 0 | 39 | 0 | 65 |
| Laboratorio | 136 | 30 | 0 | 0 | 0 |
| Imagenología | 86 | 28 | 0 | 0 | 37 |
| Reportes Gerenciales | 72 | 16 | 0 | 0 | 0 |

### Clasificación Detallada (Top 20 incidentes)

| ID | Módulo | Descripción | Característica | Justificación |
|---|---|---|---|---|
| 1210 | HCE | Historial de alergias no carga al abrir la ficha del paciente | **Efectividad** | El usuario no puede completar la tarea de revisar alergias |
| 1509 | Portal Citas | El sistema no envía la confirmación por correo electrónico | **Efectividad** | La tarea de confirmación no se completa |
| 1786 | Farmacia | Duplicidad de códigos entre dos presentaciones de un mismo fármaco | **Efectividad** | Error que impide la correcta identificación del medicamento |
| 2017 | Portal Citas | Formulario confuso, abandono de registro antes de completar la cita | **Satisfacción** | El usuario abandona por frustración con la interfaz |
| 2020 | Facturación | El sistema no reconoce el convenio con la aseguradora | **Efectividad** | No se puede completar la facturación del seguro |
| 2209 | Facturación | El sistema no permite anular una factura emitida por error | **Efectividad** | Tarea de anulación bloqueada |
| 2416 | HCE | Signos vitales no aparecen en la HCE del médico | **Efectividad** | Datos no disponibles para la consulta |
| 3137 | Telemedicina | El chat no permite enviar imágenes | **Efectividad** | Funcionalidad de chat incompleta |
| 3262 | Telemedicina | Audio desincronizado durante la teleconsulta | **Cobertura de Contexto** | El problema depende del contexto de red/dispositivo |
| 3291 | HCE | Pérdida de la nota de evolución tras cierre inesperado de sesión | **Efectividad** | Trabajo perdido, tarea no completada |
| 3846 | HCE | Datos de otro paciente visibles brevemente al abrir un expediente | **Libertad de Riesgo** | Exposición de datos sensibles de terceros |
| 1072 | Farmacia | Alerta de vencimiento de lote no se muestra | **Efectividad** | Alerta no visible, tarea de verificación afectada |
| 1134 | Imagenología | Tiempo de carga de estudios supera los 18s | **Eficiencia** | Recurso tiempo excede lo aceptable |
| 2008 | Facturación | El módulo de facturación se cae durante el cierre de caja | **Efectividad** | Sistema no disponible para tarea crítica |
| 3980 | HCE | Receta electrónica se genera con dosis incorrecta | **Libertad de Riesgo** | Riesgo de salud por dosificación errónea |
| 1020 | HCE | Datos de otro paciente visibles brevemente | **Libertad de Riesgo** | Exposición de datos sensibles |
| 1075 | HCE | Orden médica no se sincroniza con farmacia | **Efectividad** | Flujo de trabajo interrumpido |
| 1301 | Farmacia | Alerta de vencimiento de lote no se muestra | **Efectividad** | Función de alerta no operable |
| 1490 | Imagenología | Tiempo de carga supera los 19s | **Eficiencia** | Exceso de tiempo de respuesta |
| 1904 | Farmacia | Sistema no descuenta automáticamente medicamento dispensado | **Efectividad** | Tarea de inventario no completada |

### Análisis de Hallazgos

1. **Efectividad domina (74.1%):** La mayoría de incidentes reflejan que los usuarios **no pueden completar sus tareas**. Esto indica problemas graves de funcionalidad básica.

2. **Eficiencia (10.8%):** Principalmente en HCE e Imagenología — tiempos de carga altos que afectan la productividad clínica.

3. **Libertad de Riesgo (5.1%):** Concentrado en HCE — exposición de datos de pacientes y dosis incorrectas representan riesgos clínicos y regulatorios graves.

4. **Satisfacción (3.4%):** Baja en términos cuantitativos, pero cualitativamente crítica — abandonos por formularios confusos y notificaciones fallidas.

5. **Cobertura de Contexto (6.6%):** Telemedicina y App Móvil concentran problemas de funcionamiento en contextos específicos (red, dispositivo).

### Preguntas de Discusión

1. **¿Puede un sistema ser efectivo pero no eficiente?** Sí: el incidente 1134 (estudios de imagen tardan 18s) permite al médico ver la imagen (efectividad), pero el tiempo excesivo afecta la eficiencia en horas pico.

2. **¿Por qué la Cobertura de Contexto es relevante para una red con sedes en cinco ciudades?** Porque los incidentes de audio desincronizado (telemedicina) y fallas en app móvil varían según la calidad de conexión de cada sede (Quito vs. Manta), y el sistema debe funcionar igual en todos los contextos.
