# Escenario 3 — Comprensión del Modelo SQuaRE

## Mapa Conceptual de la Familia SQuaRE

```
                    ┌─────────────────────────────────────┐
                    │       ISO/IEC 25000                  │
                    │    Guía general SQuaRE               │
                    └──────────────────┬──────────────────┘
                                       │
            ┌──────────────────────────┼──────────────────────────┐
            ▼                          ▼                          ▼
┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐
│    ISO/IEC 25010     │ │    ISO/IEC 25022     │ │    ISO/IEC 25040     │
│  Modelo de Calidad   │ │ Medición de Calidad  │ │ Proceso de Evaluación│
│  (qué medir)         │ │ en Uso (cómo medir)  │ │                      │
└──────────────────────┘ └──────────────────────┘ └──────────────────────┘
```

## Divisiones de la Familia ISO/IEC 25000

| División | Rango | Propósito |
|---|---|---|
| Gestión de calidad | 2500n | Guía de uso de toda la familia SQuaRE |
| Modelo de calidad | 2501n | Define qué características debe tener un producto (ISO/IEC 25010) |
| Medición de calidad | 2502n | Define cómo medir cada característica (25022, 25023, 25024) |
| Requerimientos de calidad | 2503n | Guía para especificar requerimientos de calidad |
| Evaluación de calidad | 2504n | Guía para el proceso de evaluación formal de calidad |

## Los Tres Niveles de Calidad Aplicados a MediSalud HIS

| Nivel | Definición | Ejemplo en MediSalud HIS |
|---|---|---|
| **Calidad Interna** | Código, arquitectura, estática (ISO/IEC 25010) | Complejidad ciclomática del módulo de facturación medida con SonarQube |
| **Calidad Externa** | Comportamiento observable en pruebas, dinámica en entorno controlado (ISO/IEC 25010) | Pruebas de carga con JMeter simulando 500 usuarios concurrentes en el portal de citas |
| **Calidad en Uso** | Experiencia real del usuario en producción (ISO/IEC 25022) | Tiempo real que tarda un médico en registrar una nota clínica durante consulta externa (dato de producción) |

### Ejemplos Adicionales del Propio Dataset

| Nivel | Ejemplo con datos reales de MediSalud |
|---|---|
| **Calidad Interna** | Deuda técnica en el microservicio de HCE por falta de pruebas unitarias |
| **Calidad Externa** | Pruebas de integración entre el módulo de farmacia y HCE para verificar sincronización de órdenes médicas |
| **Calidad en Uso** | Incidente #3846: "Datos de otro paciente visibles brevemente al abrir un expediente" — medido en producción como fallo de Libertad de Riesgo |

## Preguntas de Discusión

1. **¿Puede un sistema tener excelente calidad interna y mala calidad en uso?** Sí. Un código limpio y bien estructurado puede tener una interfaz confusa o tardar demasiado en responder. Por ejemplo, el microservicio de HCE puede tener código impecable (calidad interna) pero el médico experimenta 24s de carga en horas pico (mala calidad en uso).

2. **¿Por qué SonarQube no es suficiente para resolver la lentitud percibida por los médicos?** Porque SonarQube mide atributos estáticos del código (complejidad, duplicación, cobertura), no la experiencia del usuario en producción. La lentitud puede deberse a infraestructura (red, BD), configuración o concurrencia, no al código mismo.
