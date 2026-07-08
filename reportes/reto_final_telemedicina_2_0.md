# Reto Final: Telemedicina 2.0 — ISO/IEC 25022

## Integración de Teleconsulta en el Sistema de Calidad en Uso

---

## 1. Nuevas Características de Calidad para Telemedicina

La Telemedicina 2.0 introduce requerimientos específicos que extienden el modelo ISO/IEC 25022:

| Característica ISO 25022 | Subcaracterística | Relevancia en Telemedicina |
|-------------------------|-------------------|---------------------------|
| **Efectividad** | Precisión diagnóstica remota | La calidad del audio/video no debe afectar el diagnóstico |
| **Eficiencia** | Tiempo de establecimiento de llamada | La conexión debe establecerse en < 15 s |
| **Satisfacción** | Confort del paciente en consulta virtual | Experiencia comparable a consulta presencial |
| **Libertad de Riesgo** | Privacidad de datos en transmisión | Video-cifrado end-to-end, cumplimiento GDPR/LOPD |
| **Cobertura de Contexto** | Funcionamiento en redes de baja velocidad | Adaptive bitrate streaming |

---

## 2. Nuevas Métricas (Catálogo Extendido)

| Código | Métrica | Fórmula | Unidad | Meta |
|--------|---------|---------|--------|------|
| M-TEL-01 | Tasa de conexión exitosa | (conexiones exitosas / total intentos) × 100 | % | ≥ 95% |
| M-TEL-02 | Tiempo de establecimiento de llamada | T_establecimiento — T_inicio | s | ≤ 15 s |
| M-TEL-03 | Índice de calidad de video | (frames recibidos / frames esperados) × 100 | % | ≥ 90% |
| M-TEL-04 | NPS Teleconsulta | ∑ NPS / total encuestas teleconsulta | 1-10 | ≥ 7.0 |
| M-TEL-05 | Tasa de reconexión | (reconexiones / total sesiones) × 100 | % | ≤ 5% |
| M-TEL-06 | Resolución promedio de llamada | Resolución más frecuente durante la sesión | p | ≥ 720p |
| M-TEL-07 | Latencia promedio | T_envío + T_procesamiento + T_recepción | ms | ≤ 200 ms |
| M-TEL-08 | Tasa de caídas de llamada | (caídas / total llamadas) × 100 | % | ≤ 2% |
| M-TEL-09 | Satisfacción del médico con plataforma | ∑ CSAT_med / total médicos | 1-5 | ≥ 4.0 |
| M-TEL-10 | Cumplimiento de programación | (citas realizadas / citas agendadas) × 100 | % | ≥ 90% |

---

## 3. Integración al Pipeline Existente

```python
def calcular_metricas_telemedicina(calidad_video, latencia, reconexiones):
    # Se añade al pipeline_medicion.py como nueva sección
    metricas_tel = []
    metricas_tel.append({"codigo": "M-TEL-01", "valor": tasa_conexion, ...})
    metricas_tel.append({"codigo": "M-TEL-07", "valor": latencia, ...})
    return metricas_tel
```

El dashboard existente debe ampliarse con una sección "Telemedicina" con 3 KPI adicionales.

---

## 4. Arquitectura Sugerida de Monitoreo

```
[App Móvil/Paciente] → [WebRTC/SFU] → [MediSalud HIS]
                          ↓
                [Monitor de Calidad]
                    ↓             ↓
        [Pipeline Métricas]  [Alertas Tiempo Real]
                    ↓
            [Dashboard Calidad en Uso]
```

### Componentes técnicos recomendados

| Componente | Tecnología Propuesta | Propósito |
|-----------|---------------------|-----------|
| SFU (Selective Forwarding Unit) | LiveKit / Jitsi | Manejo de video multiparte |
| Adaptive Bitrate | HLS/DASH | Ajuste dinámico según ancho de banda |
| Cifrado | WebRTC SRTP/SCTP + DTLS | Privacidad end-to-end |
| Monitoreo en tiempo real | Prometheus + Grafana | Latencia, jitter, packet loss |
| Logs de calidad | Exportador WebRTC Stats → CSV | Alimentar pipeline ISO 25022 |

---

## 5. Estrategia de Despliegue

| Fase | Contenido | Duración |
|------|-----------|----------|
| **Fase 1 — Piloto** | 3 sedes urbanas (Quito, Guayaquil, Cuenca), 50 médicos | 30 días |
| **Fase 2 — Expansión** | Todas las sedes, 200+ médicos | 60 días |
| **Fase 3 — Optimización** | Adaptive bitrate + modo offline para Manta y zonas rurales | 45 días |
| **Fase 4 — Madurez** | IA para detección de caídas de calidad + autocuración | 90 días |

### Criterios de éxito para pasar de Fase 1 a Fase 2

- M-TEL-01 ≥ 90% (tasa de conexión exitosa)
- M-TEL-07 ≤ 250 ms (latencia promedio)
- M-TEL-04 ≥ 6.0 (NPS Teleconsulta)

---

## 6. Cierre: Lecciones Aprendidas del Taller

1. **ISO/IEC 25022 proporciona un marco integral** que va más allá de pruebas funcionales: evalúa la experiencia real del usuario en su contexto de uso.
2. **La medición sin automatización no escala** — el pipeline desarrollado permite ciclos PDCA semanales.
3. **La satisfacción del usuario es el indicador síntesis** — si el NPS es bajo, las métricas técnicas pueden ser buenas pero el sistema no genera valor.
4. **Telemedicina 2.0 requiere extender el modelo** con métricas específicas de calidad de video, latencia y adaptabilidad a condiciones de red variables.
5. **La mejora continua no termina** — cada ciclo PDCA revela nuevas oportunidades de optimización.

---

*Documento generado como parte del Taller de Calidad en Uso ISO/IEC 25022*
*Caso de estudio: MediSalud HIS — Ecuador, 2025*
