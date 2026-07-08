# Escenario 10: Interpretación y Análisis de Causa Raíz

## 1. Resultados Clave del Dashboard

| Indicador | Valor | Meta | Estado |
|-----------|-------|------|--------|
| Tiempo promedio HCE | 8.13 s | ≤ 8.0 s | 🟡 AMARILLO |
| P90 tiempo HCE | 14.80 s | ≤ 12.0 s | 🟡 AMARILLO |
| NPS promedio | 5.43/10 | ≥ 7.0 | 🟡 AMARILLO |
| CSAT promedio | 2.93/5 | ≥ 4.0 | 🟡 AMARILLO |
| Tasa de éxito HCE | 96.92% | ≥ 95% | 🟢 VERDE |
| Incidentes Libertad de Riesgo | 5.10% | < 3% | 🟡 AMARILLO |
| Incidentes Eficiencia | 10.77% | < 8% | 🟡 AMARILLO |
| Variabilidad por sede (σ) | 1.18 s | ≤ 2.0 s | 🟢 VERDE |
| Tasa no recomendación | 29.65% | < 15% | 🔴 ROJO |

## 2. Análisis de Causa Raíz

### 🔴 ROJO: Tasa de no recomendación (29.65%)

**Causas identificadas:**
- Sede Manta presenta NPS significativamente más bajo (por conectividad limitada)
- CSAT promedio de 2.93 indica insatisfacción generalizada
- La experiencia del paciente es deficiente en el módulo de Portal Citas y Teleconsulta

**Causa raíz probable:** La combinación de tiempos de respuesta lentos en HCE (8.13 s promedio, hasta 14.8 s en P90) + problemas de usabilidad en Portal Citas genera una experiencia negativa que los pacientes no recomiendan.

### 🟡 AMARILLO: Tiempo promedio HCE (8.13 s)

**Causas identificadas:**
- Horas pico (10:00-12:00) incrementan el tiempo entre 1.5× y 3×
- Sede Manta tiene tiempos superiores al promedio por infraestructura limitada
- El P90 de 14.8 s indica que el 10% de las transacciones son extremadamente lentas

**Causa raíz probable:** Sin escalamiento horizontal en horas pico ni optimización de consultas a base de datos, el sistema se degrada bajo carga.

### 🟡 AMARILLO: NPS bajo (5.43) y CSAT bajo (2.93)

**Causas identificadas:**
- Pacientes reportan formularios confusos (Satisfacción)
- Portal Citas concentra incidentes de usabilidad
- Sede Manta penaliza el NPS general

**Causa raíz probable:** El diseño UX/UI del portal no fue validado con usuarios reales; la capacitación insuficiente del personal agrava el problema.

### 🟡 AMARILLO: Incidentes de Libertad de Riesgo (5.10%)

**Causas identificadas:**
- Datos de pacientes visibles a usuarios no autorizados
- Alertas de interacciones medicamentosas no desplegadas
- Duplicidad de códigos en Farmacia

**Causa raíz probable:** Controles de acceso y validaciones clínicas implementados de forma parcial, sin auditoría de seguridad.

## 3. Priorización de Acciones

| Prioridad | Acción | Impacto | Esfuerzo |
|-----------|--------|---------|----------|
| 1 | Revisar infraestructura de Manta y horas pico | Alto | Medio |
| 2 | Rediseñar UX de Portal Citas | Alto | Alto |
| 3 | Implementar controles de acceso RBAC | Alto | Medio |
| 4 | Campaña de capacitación a usuarios | Medio | Bajo |
| 5 | Optimización de consultas HCE | Medio | Alto |
