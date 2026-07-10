# Escenario 6 — Diseño de Métricas ISO/IEC 25022

## Catálogo de 10 Métricas de Calidad en Uso para MediSalud HIS

### Métrica 1: Tiempo Promedio de Registro de HCE
| Campo | Valor |
|---|---|
| **Código** | M-EFI-01 |
| **Característica** | Eficiencia |
| **Propósito** | Medir el tiempo que tarda un médico en guardar una nota de evolución clínica |
| **Fórmula** | `X = Σ tiempo_i / n` (promedio de tiempos de guardado) |
| **Unidad** | Segundos |
| **Fuente de datos** | Log del microservicio HCE |
| **Frecuencia** | Por transacción / reporte diario |
| **Meta (target)** | ≤ 8 segundos en el 90% de los casos (RNF-01) |

### Métrica 2: Tasa de Éxito de Agendamiento
| Campo | Valor |
|---|---|
| **Código** | M-EFE-01 |
| **Característica** | Efectividad |
| **Propósito** | Medir la tasa de citas agendadas exitosamente vs. intentos |
| **Fórmula** | `X = (agendados / intentados) × 100` |
| **Unidad** | Porcentaje (%) |
| **Fuente de datos** | BD del Portal de Citas |
| **Frecuencia** | Diaria |
| **Meta (target)** | ≥ 95% |

### Métrica 3: Tasa de Errores de Facturación
| Campo | Valor |
|---|---|
| **Código** | M-RIE-01 |
| **Característica** | Libertad de Riesgo |
| **Propósito** | Medir la proporción de transacciones con errores de facturación |
| **Fórmula** | `X = (errores / total transacciones) × 100` |
| **Unidad** | Porcentaje (%) |
| **Fuente de datos** | BD del módulo de Facturación |
| **Frecuencia** | Mensual |
| **Meta (target)** | < 1% (RNF-03) |

### Métrica 4: Índice de Abandono de Teleconsulta
| Campo | Valor |
|---|---|
| **Código** | M-SAT-01 |
| **Característica** | Satisfacción |
| **Propósito** | Medir la tasa de teleconsultas que se abandonan antes de finalizar |
| **Fórmula** | `X = (abandonos / teleconsultas iniciadas) × 100` |
| **Unidad** | Porcentaje (%) |
| **Fuente de datos** | Logs de la App Móvil / Plataforma de videollamadas |
| **Frecuencia** | Semanal |
| **Meta (target)** | < 5% (alineado a objetivo de 95% de finalización) |

### Métrica 5: Variabilidad de Tiempo HCE por Sede
| Campo | Valor |
|---|---|
| **Código** | M-CC-01 |
| **Característica** | Cobertura de Contexto |
| **Propósito** | Medir la desviación estándar del tiempo de registro HCE entre las distintas sedes |
| **Fórmula** | `X = σ(tiempo_por_sede)` (desviación estándar) |
| **Unidad** | Segundos |
| **Fuente de datos** | Log del microservicio HCE con campo sede |
| **Frecuencia** | Semanal |
| **Meta (target)** | σ ≤ 2 segundos (rendimiento homogéneo entre sedes) |

### Métrica 6: Tasa de Incidentes de Privacidad
| Campo | Valor |
|---|---|
| **Código** | M-RIE-02 |
| **Característica** | Libertad de Riesgo |
| **Propósito** | Contar incidentes donde datos de un paciente son visibles a otro usuario |
| **Fórmula** | `X = conteo mensual de incidentes` |
| **Unidad** | Número de incidentes |
| **Fuente de datos** | Registro de incidentes de seguridad / Logs de acceso |
| **Frecuencia** | Mensual |
| **Meta (target)** | 0 incidentes |

### Métrica 7: Tasa de Abandono en Portal de Citas
| Campo | Valor |
|---|---|
| **Código** | M-SAT-02 |
| **Característica** | Satisfacción |
| **Propósito** | Medir abandonos por formulario confuso antes de completar agendamiento |
| **Fórmula** | `X = (sesiones con abandono / total sesiones iniciadas) × 100` |
| **Unidad** | Porcentaje (%) |
| **Fuente de datos** | Analítica web del Portal de Citas |
| **Frecuencia** | Diaria |
| **Meta (target)** | < 10% |

### Métrica 8: Tasa de Éxito de Receta Electrónica
| Campo | Valor |
|---|---|
| **Código** | M-EFE-02 |
| **Característica** | Efectividad |
| **Propósito** | Medir la tasa de recetas generadas sin errores de dosificación |
| **Fórmula** | `X = (recetas_correctas / total_recetas) × 100` |
| **Unidad** | Porcentaje (%) |
| **Fuente de datos** | BD del módulo HCE / Farmacia |
| **Frecuencia** | Diaria |
| **Meta (target)** | 100% (tolerancia 0 a errores de dosis) |

### Métrica 9: Tiempo de Carga de Estudios de Imagen
| Campo | Valor |
|---|---|
| **Código** | M-EFI-02 |
| **Característica** | Eficiencia |
| **Propósito** | Medir el percentil 90 del tiempo de carga de imágenes DICOM |
| **Fórmula** | `X = P90(tiempo_carga)` |
| **Unidad** | Segundos |
| **Fuente de datos** | Log del visor DICOM / Imagenología |
| **Frecuencia** | Diaria |
| **Meta (target)** | ≤ 10 segundos |

### Métrica 10: Tasa de Caídas de Videollamada
| Campo | Valor |
|---|---|
| **Código** | M-CC-02 |
| **Característica** | Cobertura de Contexto |
| **Propósito** | Medir la tasa de teleconsultas con caídas de videollamada |
| **Fórmula** | `X = (caídas / total teleconsultas) × 100` |
| **Unidad** | Porcentaje (%) |
| **Fuente de datos** | Logs de la plataforma de videollamadas |
| **Frecuencia** | Semanal |
| **Meta (target)** | < 5% (RNF-05) |
