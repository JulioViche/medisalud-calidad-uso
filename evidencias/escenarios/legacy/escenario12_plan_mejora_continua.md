# Escenario 12: Plan de Mejora Continua

## Ciclo PDCA — ISO/IEC 25022 para MediSalud HIS

---

## Fase 1: PLAN (Planificar)

### Objetivos para Julio 2025

| Métrica | Línea Base (Feb 2025) | Meta Julio 2025 | Meta Dic 2025 |
|---------|----------------------|-----------------|---------------|
| Tiempo promedio HCE | 8.13 s | ≤ 6.0 s | ≤ 4.0 s |
| P90 tiempo HCE | 14.80 s | ≤ 10.0 s | ≤ 7.0 s |
| NPS promedio | 5.43 | ≥ 7.0 | ≥ 8.0 |
| CSAT promedio | 2.93 | ≥ 3.5 | ≥ 4.2 |
| Tasa de éxito HCE | 96.92% | ≥ 98% | ≥ 99% |
| Incidentes Libertad de Riesgo | 5.10% | ≤ 3% | ≤ 1% |
| Incidentes Eficiencia | 10.77% | ≤ 6% | ≤ 3% |
| Tasa no recomendación | 29.65% | ≤ 15% | ≤ 8% |

### Acciones Planificadas

| Código | Acción | Responsable | Plazo |
|--------|--------|-------------|-------|
| P-01 | Rediseñar formulario de registro de citas | UX Lead | 30 días |
| P-02 | Implementar caché de consultas HCE | Backend Lead | 45 días |
| P-03 | Migrar Manta a servidor local con réplica | Infra Lead | 60 días |
| P-04 | Implementar RBAC y auditoría | Seguridad Lead | 30 días |
| P-05 | Capacitar a 100% del personal en HCE | Capacitación | 15 días |
| P-06 | Automatizar pipeline de métricas (PDCA) | Calidad Lead | 90 días |

---

## Fase 2: DO (Ejecutar)

### Ciclo 1 — Abril 2025

| Semana | Actividades |
|--------|------------|
| 1 | Capacitación exprés a médicos (HCE + Portal Citas) |
| 2-3 | Hotfixes de usabilidad en Portal Citas (formulario + confirmación email) |
| 4 | Despliegue de RBAC básico |
| | **Hito:** Reunión de revisión quincenal con líderes de sede |

---

## Fase 3: CHECK (Verificar)

### Herramientas de Monitoreo

1. **Pipeline automatizado** (`scripts/pipeline_medicion.py`) se ejecuta semanalmente
2. **Dashboard** (`dashboards/dashboard_calidad_uso.html`) accesible para todo el equipo
3. **Alertas automáticas** cuando una métrica pasa a ROJO
4. **Encuesta rápida NPS** mensual (muestra de 500 pacientes)

### Indicadores de seguimiento

- Número de incidentes abiertos vs. cerrados por sprint
- Tendencia semanal de tiempo HCE por sede
- Evolución del NPS post-capacitación

---

## Fase 4: ACT (Actuar)

### Disparadores de Acción Correctiva

| Evento | Acción |
|--------|--------|
| Tiempo HCE > 10 s por 2 semanas consecutivas | Escalar a Lead Backend, revisar consultas DB |
| Incidente de Libertad de Riesgo nuevo | Pausar release, auditoría inmediata |
| NPS < 5.0 en una sede | Visita in situ del equipo de calidad |
| Tasa no recomendación > 20% | Revisión de UX y plan de remediación urgente |

### Calendario PDCA Anual

| Trimestre | Ciclo | Enfoque |
|-----------|-------|---------|
| Q2 2025 (Abr-Jun) | PDCA 1 | Estabilización: rendimiento + seguridad |
| Q3 2025 (Jul-Sep) | PDCA 2 | Satisfacción: UX + Portal Citas |
| Q4 2025 (Oct-Dic) | PDCA 3 | Excelencia: todos los indicadores en VERDE |
| Q1 2026 | PDCA 4 | Expandir a Telemedicina 2.0 y nuevos módulos |
