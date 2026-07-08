# Escenario 11: Presentación Ejecutiva

## MediSalud HIS — Informe de Calidad en Uso ISO/IEC 25022
**Período:** Enero - Febrero 2025 | **Audiencia:** Dirección de TI, Gerencia General

---

## 1. Resumen Ejecutivo

Se evaluó la **calidad en uso** del sistema MediSalud HIS aplicando el estándar ISO/IEC 25022 sobre **3,000 incidentes reales**, **5,000 logs de rendimiento** y **2,000 encuestas de satisfacción**.

**Semáforo general:**
- 🟢 **VERDE:** 2 métricas (22%)
- 🟡 **AMARILLO:** 6 métricas (67%)
- 🔴 **ROJO:** 1 métrica (11%)

## 2. Hallazgos Principales

| Dimensión | Hallazgo | Prioridad |
|-----------|----------|-----------|
| **Efectividad** | ✅ Tasa de éxito 96.92% — el sistema cumple su función | 🟢 Baja |
| **Eficiencia** | ⚠️ Tiempo promedio HCE 8.13 s (meta: 8 s). P90 de 14.8 s | 🟡 Media |
| **Satisfacción** | ❌ NPS 5.43/10 y CSAT 2.93/5. 29.65% no recomienda el sistema | 🔴 Alta |
| **Libertad de Riesgo** | ⚠️ 5.10% de incidentes afectan seguridad de datos | 🟡 Alta |
| **Cobertura de Contexto** | ✅ Variabilidad por sede controlada (σ = 1.18 s) | 🟢 Baja |

## 3. Impacto en el Negocio

1. **Pérdida de confianza:** 3 de cada 10 pacientes no recomendarían MediSalud
2. **Riesgo regulatorio:** Incidentes de exposición de datos sensibles
3. **Productividad reducida:** Personal médico pierde ~8s por registro HCE en hora pico
4. **Brecha digital:** Sede Manta significativamente rezagada

## 4. Recomendaciones Estratégicas

| Acción | Inversión Estimada | ROI Esperado |
|--------|-------------------|--------------|
| **Optimización de infraestructura** (Manta + horas pico) | $15,000 | Reducción tiempo HCE a 5s |
| **Rediseño UX Portal Citas** | $25,000 | Aumento NPS a 7.0+ |
| **RBAC + auditoría de seguridad** | $10,000 | Mitigar riesgo regulatorio |
| **Capacitación a usuarios** | $5,000 | Reducción incidentes en 20% |

## 5. Próximos Pasos

1. **Sprint 1 (Abril):** Capacitación + fixes rápidos de Portal Citas
2. **Sprint 2 (Mayo):** Implementación RBAC + monitoreo en Manta
3. **Sprint 3 (Junio):** Optimización backend HCE
4. **Julio:** Nueva medición ISO/IEC 25022 con metas ajustadas
