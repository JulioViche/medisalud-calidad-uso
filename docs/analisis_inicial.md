# Análisis Inicial — Caso MediSalud Ecuador

## Matriz de análisis

| Pregunta guía | Respuesta del grupo |
|---|---|
| **¿Cuáles son los 3 procesos más críticos del negocio?** | 1. Atención médica y registro de Historia Clínica Electrónica (HCE) — impacto directo en la salud del paciente.<br>2. Facturación y gestión de seguros — afecta el flujo de caja y la relación con aseguradoras.<br>3. Agendamiento y admisión de pacientes — puerta de entrada al sistema, afecta la experiencia del paciente y la retención. |
| **¿Qué usuarios se ven más afectados por la problemática actual?** | **Médicos tratantes** (640 usuarios activos): lentitud del HCE en horas pico retrasa decisiones clínicas.<br>**Pacientes** (38.000+): abandonos en portal de citas, errores de facturación, teleconsultas interrumpidas.<br>**Personal de admisión** (210): doble facturación, errores de disponibilidad. |
| **¿Qué evidencia tiene hoy MediSalud sobre la calidad de su software?** | Solo disponibilidad de servidores (uptime). No hay métricas de experiencia de usuario, tiempos de respuesta reales, tasas de error ni satisfacción. Las decisiones se basan en percepción, no en datos. |
| **¿Qué evidencia le falta?** | Métricas objetivas de Calidad en Uso según ISO/IEC 25022: efectividad (tasa de éxito de tareas), eficiencia (tiempos de respuesta reales), satisfacción (NPS, abandono), libertad de riesgo (incidentes de seguridad/facturación) y cobertura de contexto (rendimiento por sede/horario/dispositivo). |

## Preguntas de discusión

### ¿Por qué la disponibilidad de servidores (uptime) no es suficiente para afirmar que un sistema tiene buena calidad en uso?

El uptime solo indica que la infraestructura permanece accesible. Un sistema puede estar disponible y, aun así, impedir que los usuarios completen sus tareas, responder con lentitud, producir resultados incorrectos, exponerlos a riesgos o generar insatisfacción. La calidad en uso debe valorar si usuarios específicos alcanzan sus objetivos con efectividad, eficiencia, satisfacción, libertad de riesgo y cobertura del contexto; por ello, la disponibilidad es una evidencia técnica útil, pero insuficiente.

### ¿Qué diferencia existe entre la calidad interna, la calidad externa y la calidad en uso de un producto software?

La **calidad interna** estudia propiedades estáticas del código y la arquitectura sin ejecutar el sistema, como la complejidad, duplicación o mantenibilidad. La **calidad externa** observa el comportamiento del software en ejecución dentro de un entorno controlado, mediante pruebas funcionales, de integración o rendimiento. La **calidad en uso** evalúa los resultados obtenidos por usuarios concretos al realizar tareas reales en un contexto determinado. En MediSalud, estos niveles se representan, respectivamente, mediante el análisis del código con SonarQube, las pruebas de carga del portal de citas con JMeter y la medición del tiempo que necesita un médico para registrar una nota clínica.

### En MediSalud, ¿qué stakeholder se beneficiaría más de un programa de medición de calidad en uso: el paciente, el médico o la gerencia? Justifique.

El **paciente** recibiría el beneficio final más importante, porque una atención más efectiva, oportuna y segura repercute directamente en su salud y en la continuidad del tratamiento. No obstante, ese beneficio depende de medir también la experiencia del médico: la lentitud, los errores o la información incompleta en la HCE afectan sus decisiones clínicas. La gerencia utiliza las métricas para priorizar recursos y acciones. Por tanto, el programa debe centrarse en el paciente, incorporar las tareas críticas del médico y proporcionar a la gerencia evidencia para decidir.

## Conclusión parcial

El diagnóstico demuestra que la evidencia exclusivamente técnica no permite conocer la experiencia real de los usuarios. MediSalud necesita complementar el uptime y los incidentes con resultados de tareas, tiempos, percepción y contexto, manteniendo trazabilidad entre cada problema, el usuario afectado y su impacto clínico u operativo.
