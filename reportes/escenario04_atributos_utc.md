# Escenario 4 — Identificación de Atributos de Calidad en Uso

## Modelo Usuario–Tarea–Contexto (UTC)

### 10 Atributos Identificados para MediSalud HIS

| # | Usuario | Tarea | Contexto | Atributo | Característica |
|---|---|---|---|---|---|
| 1 | Médico | Registrar nota de evolución clínica | Consulta externa, horario pico (10-12h), sede Quito | Tiempo promedio de registro (segundos) | Eficiencia |
| 2 | Médico | Revisar historial de alergias del paciente | Consulta externa, cualquier horario | Tasa de carga exitosa del historial (%) | Efectividad |
| 3 | Paciente | Agendar cita médica vía portal web | Noche, dispositivo móvil, conexión 4G | Tasa de abandono del formulario (%) | Satisfacción |
| 4 | Paciente | Realizar teleconsulta | Domicilio, conexión WiFi limitada | Tasa de caídas de videollamada por sesión (%) | Cobertura de Contexto |
| 5 | Admisión | Facturar consulta con seguro | Horario de cierre, fin de mes | Tasa de errores de facturación (%) | Efectividad |
| 6 | Admisión | Reagendar cita previamente confirmada | Cualquier horario, sistema en producción | Tasa de éxito de reagendamiento (%) | Efectividad |
| 7 | Farmacia | Dispensar medicamento controlado | Turno nocturno, urgencias | Incidentes de dispensación errónea por turno | Libertad de Riesgo |
| 8 | Enfermería | Registrar signos vitales desde tablet | Habitación de paciente, red hospitalaria | Tasa de sincronización con HCE (%) | Efectividad |
| 9 | Médico | Adjuntar imagen de herida desde tablet | Consulta externa, dispositivo móvil | Tasa de éxito de adjuntado (%) | Efectividad |
| 10 | Paciente | Iniciar sesión con biometría | App móvil, Android/iOS, cualquier ubicación | Tasa de fallo de autenticación biométrica (%) | Cobertura de Contexto |
| 11 | Médico | Generar receta electrónica | Post-consulta, desde consultorio | Tasa de recetas con dosis incorrecta (%) | Libertad de Riesgo |
| 12 | Paciente | Ver resultados de laboratorio | App móvil, fuera del horario laboral | Tasa de visualización exitosa de PDF (%) | Efectividad |

## Análisis

El modelo UTC permite descomponer la calidad en uso en elementos concretos:

- **Usuario**: Médico, Enfermería, Paciente, Admisión, Farmacia — cada perfil tiene necesidades distintas.
- **Tarea**: Acciones atómicas medibles (registrar, agendar, facturar, dispensar).
- **Contexto**: Variables que afectan el rendimiento (horario, dispositivo, ubicación, red).

Los 12 atributos identificados cubren las 5 características de ISO/IEC 25022, con énfasis en **Efectividad** y **Eficiencia** que son las más críticas según el análisis de incidentes del Escenario 2.
