# Aseguramiento de la Calidad del Software

## Taller Guiado Integral
Medición de la Calidad en Uso mediante ISO/IEC 25022
Caso de estudio: Sistema de Historia Clínica Electrónica
Red Hospitalaria MediSalud Ecuador

**Marco de referencia:** ISO/IEC 25000 (SQuaRE)
**Norma central:** ISO/IEC 25022 — Measurement of Quality in Use
**Nivel:** Séptimo Semestre — Ingeniería en Sistemas / Ingeniería de Software
**Modalidad:** Taller práctico basado en caso de estudio empresarial

*Material didáctico para docentes universitarios*
*Versión 1.0*

---

## Ficha Técnica del Material

| | |
|---|---|
| **Asignatura** | Aseguramiento de la Calidad del Software |
| **Unidad temática** | Evaluación de la Calidad del Producto de Software — Modelo SQuaRE |
| **Norma aplicada** | ISO/IEC 25022:2016 — Measurement of Quality in Use |
| **Dirigido a** | Estudiantes de séptimo semestre de Ingeniería en Sistemas, Ingeniería de Software o carreras afines |
| **Duración total sugerida** | 12 sesiones de 3 horas (36 horas académicas) |
| **Modalidad** | Presencial / híbrida, con componente de laboratorio individual y grupal |
| **Prerrequisitos** | Fundamentos de bases de datos, programación en Python, nociones de ingeniería de software |
| **Caso de estudio** | Sistema de Historia Clínica Electrónica (HCE) de una red hospitalaria nacional |

---

## Índice general

1. [Introducción al Caso Empresarial](#1-introducción-al-caso-empresarial)
2. [Comprensión de ISO/IEC 25022](#2-comprensión-de-isoiec-25022)
3. [Comprensión del Modelo SQuaRE](#3-comprensión-del-modelo-square)
4. [Identificación de Atributos de Calidad en Uso](#4-identificación-de-atributos-de-calidad-en-uso)
5. [Mapeo de Características de Calidad](#5-mapeo-de-características-de-calidad)
6. [Diseño de Métricas](#6-diseño-de-métricas)
7. [Obtención de Datos](#7-obtención-de-datos)
8. [Automatización de la Medición](#8-automatización-de-la-medición)
9. [Construcción de Indicadores](#9-construcción-de-indicadores)
10. [Interpretación de Resultados](#10-interpretación-de-resultados)
11. [Presentación Ejecutiva para Directivos](#11-presentación-ejecutiva-para-directivos)
12. [Plan de Mejora Continua](#12-plan-de-mejora-continua)
13. [Reto Final Integrador](#reto-final-integrador)
14. [Solución Propuesta del Reto Final](#solución-propuesta-del-reto-final)
15. [Rúbrica de Evaluación](#rúbrica-de-evaluación)
16. [Glosario](#glosario)
17. [Lista de Acrónimos](#lista-de-acrónimos)
18. [Anexos](#anexos)

---

## Presentación General del Taller

### Objetivo General

Desarrollar en los estudiantes la capacidad de aplicar la norma ISO/IEC 25022 para medir la Calidad en Uso de un sistema software empresarial real, combinando fundamento teórico riguroso con práctica intensiva sobre herramientas modernas de medición, automatización y visualización de indicadores de calidad.

### Filosofía del Taller

Este material no es un compendio teórico. Cada uno de los doce escenarios que lo componen combina una base conceptual sólida con actividades de laboratorio completamente guiadas, ejecutadas sobre un caso de estudio empresarial único y coherente: la red hospitalaria MediSalud Ecuador y su sistema de Hospital Information System (HIS). El estudiante recorrerá el ciclo completo de un proyecto real de evaluación de calidad en uso: desde la comprensión de la norma hasta la entrega de un informe ejecutivo y un plan de mejora continua.

> **Nota**
> Todas las herramientas utilizadas en este taller cuentan con edición Community, Free o Trial suficiente para fines académicos. No se requiere presupuesto institucional para su ejecución completa.

### Estructura de cada Escenario

Cada escenario sigue la misma arquitectura pedagógica:

1. **Parte 1 — Fundamento Teórico:** definiciones, marco normativo, fórmulas y ejemplos aplicados al caso MediSalud.
2. **Parte 2 — Actividad Práctica:** laboratorio guiado con ficha técnica, instalación, configuración, ejecución, capturas sugeridas y solución de errores.
3. Resultados obtenidos e interpretación.
4. Análisis crítico.
5. Preguntas de discusión.
6. Conclusiones parciales.

### Mapa de Escenarios

| # | Escenario | Duración |
|---|---|---|
| 1 | Introducción al caso empresarial MediSalud | 2h |
| 2 | Comprensión de ISO/IEC 25022 | 3h |
| 3 | Comprensión del modelo SQuaRE (ISO/IEC 25000) | 2h |
| 4 | Identificación de atributos de Calidad en Uso | 3h |
| 5 | Mapeo de características de calidad | 2h |
| 6 | Diseño de métricas | 3h |
| 7 | Obtención de datos (logs, BD, encuestas) | 3h |
| 8 | Automatización de la medición con Python | 4h |
| 9 | Construcción de indicadores (KPI) | 3h |
| 10 | Interpretación de resultados | 3h |
| 11 | Presentación ejecutiva para directivos | 3h |
| 12 | Plan de mejora continua | 2h |
| | **Reto Final Integrador** | **4h** |

---

## Caso de Estudio: Red Hospitalaria MediSalud Ecuador

### Descripción de la Empresa

MediSalud Ecuador es una red privada de salud constituida en 2009, con cobertura en cinco ciudades del país (Quito, Guayaquil, Cuenca, Ambato y Manta). La red opera actualmente:

- 4 hospitales generales de tercer nivel.
- 12 centros de atención ambulatoria.
- 1 laboratorio clínico centralizado con sucursales.
- 1 central de imagenología y diagnóstico por imágenes.
- Un servicio de telemedicina en expansión desde 2022.

La organización atiende aproximadamente 38.000 pacientes activos por mes y emplea a más de 2.100 colaboradores, entre personal médico, administrativo y de TI.

### Estructura Organizacional

- **Dirección General** — define objetivos estratégicos de la red.
- **Dirección Médica** — supervisa protocolos clínicos y calidad asistencial.
- **Gerencia de Tecnología (TI)** — responsable del sistema HIS, infraestructura y ciberseguridad.
- **Gerencia de Calidad y Aseguramiento** — responsable de certificaciones (ISO 9001, acreditación hospitalaria) y ahora del programa de Calidad en Uso del Software.
- **Departamento de Admisión y Facturación.**
- **Departamento de Enfermería y Hospitalización.**
- **Departamento de Farmacia.**
- **Call Center y Agendamiento de Citas.**

### El Sistema: MediSalud HIS

El núcleo tecnológico de la operación es MediSalud HIS, un sistema de información hospitalaria que integra:

- Módulo de Historia Clínica Electrónica (HCE) (historia clínica electrónica).
- Módulo de admisión, agendamiento y facturación.
- Módulo de farmacia e inventario de insumos médicos.
- Portal del paciente (web y app móvil) para citas y resultados.
- Módulo de telemedicina (videoconsulta e indicaciones remotas).
- Módulo de reportes gerenciales y business intelligence.

### Usuarios del Sistema

| Perfil | Uso principal | Usuarios activos |
|---|---|---|
| Médico tratante | Registro de HCE, órdenes, recetas | 640 |
| Enfermería | Signos vitales, administración de medicamentos | 910 |
| Personal de admisión | Agendamiento, facturación | 210 |
| Farmacia | Dispensación, inventario | 85 |
| Paciente (portal/app) | Citas, resultados, telemedicina | 38.000+ |
| Gerencia / Calidad | Reportes, indicadores | 45 |

### Arquitectura del Sistema

MediSalud HIS sigue una arquitectura de microservicios desplegada en contenedores, con las siguientes capas:

- **Frontend web:** React, desplegado como SPA.
- **Aplicación móvil:** Android/iOS (Flutter).
- **Backend:** microservicios en Spring Boot y FastAPI, expuestos vía API REST.
- **Base de datos transaccional:** PostgreSQL (HCE, facturación) y SQL Server (módulo financiero heredado).
- **Mensajería:** colas asíncronas para integración entre laboratorio, imagenología y HCE.
- **Infraestructura:** contenedores Docker orquestados en un clúster on-premise, con planes de migración a la nube pública.
- **Observabilidad:** logs centralizados y métricas de infraestructura (aún incipientes, sin estandarizar).

```
                    ┌─────────────────────────────────────────────┐
                    │         Portal Web (React)                   │
                    │         App Móvil (Flutter)                  │
                    └────────────────────┬────────────────────────┘
                                         │
                                         ▼
                              ┌─────────────────────┐
                              │     API Gateway      │
                              └──────────┬──────────┘
                                         │
                    ┌────────────────────┼────────────────────┐
                    ▼                    ▼                    ▼
        ┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐
        │  Microservicio     │ │  Microservicio     │ │  Microservicio     │
        │  HCE               │ │  Facturación       │ │  Farmacia          │
        └────────┬──────────┘ └────────┬──────────┘ └────────┬──────────┘
                 │                     │                     │
                 └─────────────────────┼─────────────────────┘
                                       ▼
                    ┌─────────────────────────────────────────────┐
                    │       PostgreSQL / SQL Server                │
                    └─────────────────────────────────────────────┘
```

*Figura 1: Arquitectura simplificada de MediSalud HIS*

### Tecnologías Utilizadas

React, Flutter, Spring Boot, FastAPI, PostgreSQL, SQL Server, Docker, Nginx, RabbitMQ, Git/GitHub, Jenkins (en migración a GitHub Actions).

### Procesos Críticos del Negocio

1. Agendamiento y admisión de pacientes.
2. Atención médica y registro de historia clínica.
3. Prescripción y dispensación de medicamentos.
4. Facturación y gestión de seguros/reaseguros.
5. Telemedicina y seguimiento remoto.
6. Generación de reportes gerenciales para toma de decisiones.

### Problemática Actual

Durante el último año, la Gerencia de Calidad ha recibido señales de alerta consistentes:

- Quejas recurrentes de médicos por lentitud del módulo de HCE en horas pico (10:00–12:00).
- Incremento del tiempo de espera para agendar citas vía portal del paciente.
- Errores de doble facturación reportados por el área financiera.
- Abandono de sesiones en la app móvil antes de completar el registro de síntomas en telemedicina.
- Ausencia de métricas objetivas: las decisiones se toman actualmente por percepción, no por datos.
- El área de TI afirma que «el sistema funciona correctamente» basándose únicamente en la disponibilidad de los servidores (uptime), sin considerar la experiencia real del usuario final.

### Riesgos Identificados

- **Riesgo clínico:** demoras en el registro de HCE pueden retrasar decisiones médicas críticas.
- **Riesgo financiero:** errores de facturación afectan el flujo de caja y la relación con aseguradoras.
- **Riesgo reputacional:** fricciones en el portal del paciente afectan la retención de usuarios frente a competidores.
- **Riesgo regulatorio:** la normativa ecuatoriana de protección de datos en salud exige trazabilidad y disponibilidad de la información clínica.

### Objetivos del Negocio

1. Reducir en un 30 % el tiempo de registro de HCE en consulta externa en un plazo de 6 meses.
2. Disminuir los errores de facturación duplicada a menos del 1 % de las transacciones.
3. Aumentar la tasa de finalización de teleconsultas al 95 %.
4. Establecer un programa permanente de medición de Calidad en Uso basado en ISO/IEC 25022, con reportes trimestrales a Dirección General.

### Requerimientos No Funcionales Relevantes para el Taller

| Código | Requerimiento |
|---|---|
| RNF-01 | El registro de una nota de evolución clínica no debe tardar más de 8 segundos en el 90 % de los casos. |
| RNF-02 | El portal de citas debe permitir agendar una cita en máximo 3 pasos, sin errores de disponibilidad. |
| RNF-03 | La tasa de errores de facturación no debe superar el 1 % de las transacciones mensuales. |
| RNF-04 | El sistema debe permitir auditar el uso por rol, sede y horario. |
| RNF-05 | Las teleconsultas deben completarse sin caídas de conexión en más del 95 % de los casos. |

> **Nota**
> Este caso de estudio será utilizado de forma transversal en los doce escenarios del taller. Todos los archivos de datos (CSV, logs, JSON) referenciados en las prácticas simulan –de forma anonimizada y ficticia– el comportamiento real de MediSalud HIS.

> **Recomendación para el Docente**
> Se recomienda al docente adaptar los nombres del caso de estudio a una empresa local reconocida por los estudiantes (banco, universidad, retail) si se desea aumentar la cercanía con su contexto, manteniendo la estructura de datos y métricas aquí propuesta.

---

## 1. Introducción al Caso Empresarial

**Objetivo del Escenario**

Familiarizar al estudiante con la organización MediSalud Ecuador, su sistema HIS, su problemática de calidad y el rol que jugará el equipo de Aseguramiento de la Calidad del Software a lo largo del taller, estableciendo el contrato pedagógico y el entorno de trabajo compartido.

### 1.1 Parte 1 — Fundamento Teórico

#### 1.1.1 El rol del Ingeniero de Calidad en un contexto empresarial real

En la industria, el aseguramiento de la calidad no se limita a probar que el software «no falla»; consiste en demostrar, con evidencia medible, que el sistema permite a los usuarios reales alcanzar sus objetivos de forma efectiva, eficiente y satisfactoria, dentro de un contexto de uso determinado. Esta idea es precisamente el núcleo de la **Calidad en Uso (Quality in Use)**, el concepto central que se desarrollará durante todo el taller.

#### 1.1.2 De la percepción a la evidencia

Como se describió en el caso de estudio, MediSalud Ecuador toma decisiones de TI basándose en percepciones («el sistema funciona bien porque los servidores están arriba»). El objetivo de este taller es transformar esa cultura hacia una cultura de decisiones basada en métricas, siguiendo el ciclo:

**Observar el uso real → Medir con métricas normalizadas → Construir indicadores → Interpretar → Actuar**

#### 1.1.3 Presentación del equipo de trabajo

Durante el taller, cada estudiante (o grupo de 3–4 estudiantes) asumirá el rol de un consultor externo de Calidad de Software contratado por la Gerencia de Calidad de MediSalud para implementar, de principio a fin, un programa de medición basado en ISO/IEC 25022.

### 1.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Configurar el entorno de trabajo compartido del taller y realizar el primer reconocimiento del caso |
| **Tiempo estimado:** | 2 horas |
| **Nivel de dificultad:** | Básico |
| **Herramientas requeridas:** | Cuenta de GitHub, Visual Studio Code, Python 3.11+, Git |
| **Archivos / datos necesarios:** | Repositorio medisalud-calidad-uso (se crea en este laboratorio), documento de caso de estudio |

#### Paso 1: Creación del repositorio de trabajo

1. Ingresar a https://github.com y crear una cuenta institucional (si no se dispone de una).
2. Crear un nuevo repositorio llamado `medisalud-calidad-uso`, público o privado según la política del curso.
3. Clonar el repositorio en el equipo local:

```bash
git clone https://github.com/<usuario>/medisalud-calidad-uso.git
cd medisalud-calidad-uso
mkdir -p data scripts dashboards docs reportes
```

*Listing 1.1: Clonado del repositorio de trabajo*

#### Paso 2: Instalación del entorno Python

```bash
python3 --version                               # Verificar Python 3.11 o superior
python3 -m venv venv
source venv/bin/activate                         # En Windows: venv\Scripts\activate
pip install --upgrade pip
pip install pandas numpy matplotlib plotly jupyter openpyxl
```

*Listing 1.2: Creación de entorno virtual para todo el taller*

> **Advertencia / Error Frecuente**
> Error frecuente: `python3: command not found` en Windows.
> Solución: en Windows utilizar `python` en lugar de `python3`, y verificar que la casilla «Add Python to PATH» haya sido marcada durante la instalación del intérprete descargado desde https://python.org.

#### Paso 3: Análisis dirigido del caso

En grupos de 3–4 estudiantes, completar la siguiente matriz en el archivo `docs/analisis_inicial.md`:

| Pregunta guía | Respuesta del grupo |
|---|---|
| ¿Cuáles son los 3 procesos más críticos del negocio? | |
| ¿Qué usuarios se ven más afectados por la problemática actual? | |
| ¿Qué evidencia tiene hoy MediSalud sobre la calidad de su software? | |
| ¿Qué evidencia le falta? | |

*Tabla 1.1: Matriz de análisis inicial del caso MediSalud*

> **Resultado Esperado**
> Al finalizar este escenario, cada grupo dispone de: (1) un repositorio Git funcional con la estructura de carpetas del taller, (2) un entorno Python operativo, y (3) un documento inicial de análisis del caso que evidencia comprensión crítica de la problemática empresarial.

### Resolución de Problemas

- **Error de permisos en Git (Permission denied (publickey)):** configurar una llave SSH con `ssh-keygen -t ed25519` y agregarla en GitHub → Settings → SSH Keys.
- **Conflictos de versión de Python:** usar `pyenv` para gestionar múltiples versiones si el sistema operativo trae una versión antigua preinstalada.

### Preguntas de Discusión

1. ¿Por qué la disponibilidad de servidores (uptime) no es suficiente para afirmar que un sistema tiene buena calidad en uso?
2. ¿Qué diferencia existe entre la calidad interna, la calidad externa y la calidad en uso de un producto software?
3. En el caso de MediSalud, ¿qué stakeholder se beneficiaría más de un programa de medición de calidad en uso: el paciente, el médico o la gerencia? Justifique.

### Conclusiones Parciales

Este primer escenario estableció el marco de trabajo y evidenció que las decisiones de TI en MediSalud carecen de sustento medible. Los escenarios siguientes dotarán al estudiante del marco normativo (ISO/IEC 25000 y 25022) necesario para cerrar esa brecha.

> **Recomendación para el Docente**
> Aproveche este escenario para indagar experiencias previas de los estudiantes con sistemas lentos o poco usables (bancos, universidades, salud) y conectar esas vivencias con el concepto de Calidad en Uso antes de formalizarlo en el Escenario 2.

---

## 2. Comprensión de ISO/IEC 25022

**Objetivo del Escenario**

Comprender en profundidad la norma ISO/IEC 25022 (Measurement of Quality in Use), sus cinco características, sus fórmulas de medición y su rol dentro de la familia SQuaRE, aplicándolas conceptualmente al caso MediSalud HIS.

### 2.1 Parte 1 — Fundamento Teórico

#### 2.1.1 ¿Qué es ISO/IEC 25022?

ISO/IEC 25022 es la norma internacional, perteneciente a la familia Software product Quality Requirements and Evaluation (SQuaRE) (ISO/IEC 25000), que define un modelo de medición de la Calidad en Uso de un producto software. A diferencia de ISO/IEC 25010 (que define el modelo de calidad, es decir, qué características debe tener un producto), la norma 25022 define **cómo medir** dichas características desde la perspectiva de quien efectivamente utiliza el sistema en un contexto real de uso.

> **Nota**
> La Calidad en Uso no se mide sobre el código fuente ni sobre el producto en abstracto: se mide observando a usuarios reales realizando tareas reales en un contexto de uso específico.

#### 2.1.2 Las cinco características de Calidad en Uso

ISO/IEC 25022 organiza la Calidad en Uso en cinco características:

| Característica | Definición |
|---|---|
| **Efectividad (Effectiveness)** | Precisión y grado de completitud con que los usuarios alcanzan sus objetivos específicos. |
| **Eficiencia (Efficiency)** | Recursos utilizados (tiempo, esfuerzo, personas) en relación con la efectividad alcanzada. |
| **Satisfacción (Satisfaction)** | Grado en que las necesidades del usuario son cubiertas, generando percepciones y respuestas positivas de utilidad, confianza, placer y comodidad. |
| **Libertad de Riesgo (Freedom from Risk)** | Grado en que el sistema mitiga riesgos económicos, de salud, de seguridad o ambientales potenciales. |
| **Cobertura de Contexto (Context Coverage)** | Grado en que el producto puede ser utilizado con efectividad, eficiencia, libertad de riesgo y satisfacción tanto en los contextos previstos como en otros no previstos inicialmente. |

*Tabla 2.1: Características de Calidad en Uso según ISO/IEC 25022*

#### 2.1.3 Aplicación conceptual al caso MediSalud

> **Ejemplo Empresarial**
> Un médico (usuario) intenta registrar una nota de evolución clínica (tarea) durante la consulta externa de la mañana (contexto de uso). Si logra registrarla completa y sin errores, hay **efectividad**; si lo hace en menos de 8 segundos, hay **eficiencia**; si termina la consulta sintiéndose cómodo con el sistema, hay **satisfacción**; si el sistema no expone datos sensibles del paciente durante el proceso, hay **libertad de riesgo**; y si el mismo flujo funciona igual de bien en el hospital de Quito que en el centro ambulatorio de Manta, hay **cobertura de contexto**.

#### 2.1.4 Estructura general de una métrica en ISO/IEC 25022

Toda métrica de Calidad en Uso se expresa mediante la fórmula general:

```
X = A / B
```

donde **A** representa el resultado observado (tareas completadas, tiempo invertido, incidentes detectados) y **B** representa la base de referencia (tareas intentadas, tiempo total disponible, número de usuarios). El resultado X se interpreta siempre en función de un rango deseado, definido previamente por la organización.

### 2.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Analizar la norma ISO/IEC 25022 y clasificar problemas reales de MediSalud según sus cinco características |
| **Tiempo estimado:** | 3 horas |
| **Nivel de dificultad:** | Básico – Intermedio |
| **Herramientas requeridas:** | Navegador web, editor de texto / Markdown, Miro o similar (opcional) |
| **Archivos / datos necesarios:** | Lista de incidentes de MediSalud HIS (data/incidentes_2025.csv, provisto en este escenario) |

#### Paso 1: Dataset de incidentes reportados

Crear el archivo `data/incidentes_2025.csv` con el siguiente contenido (fragmento representativo; el estudiante puede ampliarlo):

```csv
id,fecha,modulo,descripcion,rol_usuario,sede
1001,2025-11-03,HCE,Nota de evolucion tarda 22s en guardarse,Medico,Quito
1002,2025-11-03,Portal Citas,Usuario no logra agendar tras 3 intentos,Paciente,Guayaquil
1003,2025-11-04,Facturacion,Factura duplicada al reintentar pago,Admision,Cuenca
1004,2025-11-05,Telemedicina,Videollamada se corta a los 4 minutos,Paciente,Ambato
1005,2025-11-05,HCE,Datos de otro paciente visibles brevemente,Medico,Quito
1006,2025-11-06,Portal Citas,Formulario confuso, abandono de registro,Paciente,Manta
```

*Listing 2.1: Fragmento de incidentes reportados en MediSalud HIS*

#### Paso 2: Clasificación según las cinco características

En equipos, clasificar cada incidente del dataset anterior en la característica de ISO/IEC 25022 que mejor lo representa, completando la tabla:

| ID | Característica | Justificación |
|---|---|---|
| 1001 | | |
| 1002 | | |
| 1003 | | |
| 1004 | | |
| 1005 | | |
| 1006 | | |

*Tabla 2.2: Plantilla de clasificación de incidentes según ISO/IEC 25022*

> **Actividad para el Estudiante**
> Como grupo, discutan el incidente 1005. ¿Por qué corresponde principalmente a Libertad de Riesgo y no a Efectividad, a pesar de tratarse también de un error del sistema?

> **Resultado Esperado**
> Cada equipo entrega una tabla de clasificación completa con justificación técnica, demostrando la capacidad de diferenciar las cinco características de la norma sobre casos reales, no solo sobre definiciones memorizadas.

### Resolución de Problemas

- **Confusión frecuente:** los estudiantes tienden a clasificar todo como «Efectividad». Solución docente: preguntar explícitamente «¿el usuario logró o no su objetivo?» (Efectividad) versus «¿a qué costo/riesgo lo logró?» (Eficiencia / Riesgo).

### Preguntas de Discusión

1. ¿Puede un sistema ser efectivo pero no eficiente? Dé un ejemplo del caso MediSalud.
2. ¿Por qué la Cobertura de Contexto es especialmente relevante para una red hospitalaria con sedes en cinco ciudades distintas?

### Conclusiones Parciales

El estudiante ha comprendido que ISO/IEC 25022 provee un vocabulario común y estructurado para describir problemas de calidad que, en la práctica diaria de MediSalud, se reportaban de forma ambigua e inconsistente.

---

## 3. Comprensión del Modelo SQuaRE

**Objetivo del Escenario**

Ubicar a ISO/IEC 25022 dentro de la familia completa ISO/IEC 25000 (SQuaRE), diferenciando claramente entre modelo de calidad, medición de calidad, requerimientos y evaluación, para que el estudiante comprenda el marco normativo completo en el que se inserta el taller.

### 3.1 Parte 1 — Fundamento Teórico

#### 3.1.1 ¿Qué es SQuaRE?

SQuaRE es la familia de normas internacionales ISO/IEC 25000, que reemplazó y unificó a las antiguas normas ISO/IEC 9126 e ISO/IEC 14598. SQuaRE organiza el ciclo completo de gestión de la calidad del software en cinco divisiones:

| División | Rango | Propósito |
|---|---|---|
| Gestión de calidad | 2500n | Guía de uso de toda la familia SQuaRE. |
| Modelo de calidad | 2501n | Define qué características debe tener un producto (ISO/IEC 25010) y su calidad en uso. |
| Medición de calidad | 2502n | Define cómo medir cada característica: aquí reside ISO/IEC 25022 (Calidad en Uso), junto con 25023 (calidad de producto) y 25024 (calidad de datos). |
| Requerimientos de calidad | 2503n | Guía para especificar requerimientos de calidad. |
| Evaluación de calidad | 2504n | Guía para el proceso de evaluación formal de calidad. |

*Tabla 3.1: Divisiones de la familia ISO/IEC 25000 (SQuaRE)*

#### 3.1.2 Relación entre ISO/IEC 25010 y 25022

ISO/IEC 25010 define el modelo de calidad en uso con sus cinco características (las mismas vistas en el Escenario 2). ISO/IEC 25022 toma exactamente esas características y les asocia métricas concretas, fórmulas y escalas de medición. Es decir: **25010 dice qué medir; 25022 dice cómo medirlo.**

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

*Figura 3.1: Ubicación de ISO/IEC 25022 dentro de la familia SQuaRE*

### 3.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Construir un mapa conceptual de la familia SQuaRE aplicado a MediSalud y diferenciar los tres niveles de calidad (interna, externa, en uso) |
| **Tiempo estimado:** | 2 horas |
| **Nivel de dificultad:** | Básico |
| **Herramientas requeridas:** | Draw.io / Miro / papel y lápiz |
| **Archivos / datos necesarios:** | Documento resumen de las normas (proporcionado por el docente o buscado por los estudiantes en fuentes oficiales de ISO) |

#### Paso 1: Investigación dirigida

Cada grupo investiga y resume en máximo media página, en sus propias palabras, la diferencia entre:

- **Calidad interna** (código, arquitectura) — ISO/IEC 25010, vista estática.
- **Calidad externa** (comportamiento observable en pruebas) — ISO/IEC 25010, vista dinámica en entorno controlado.
- **Calidad en uso** (experiencia real del usuario) — ISO/IEC 25022, vista en producción.

#### Paso 2: Aplicación al caso MediSalud

Completar la tabla identificando, para cada nivel, un ejemplo concreto del sistema HIS:

| Nivel | Ejemplo en MediSalud HIS |
|---|---|
| Calidad interna | Complejidad ciclomática del módulo de facturación medida con SonarQube. |
| Calidad externa | Pruebas de carga con JMeter simulando 500 usuarios concurrentes en el portal de citas. |
| Calidad en uso | Tiempo real que tarda un médico en registrar una nota clínica durante consulta externa (dato de producción). |

*Tabla 3.2: Los tres niveles de calidad aplicados a MediSalud HIS*

> **Resultado Esperado**
> Cada grupo entrega un mapa conceptual (imagen o diagrama) que ubica correctamente las normas ISO/IEC 25000, 25010, 25022 y 25040, y diferencia sin ambigüedad los tres niveles de calidad usando ejemplos propios del caso MediSalud.

### Preguntas de Discusión

1. ¿Puede un sistema tener excelente calidad interna (código limpio) y mala calidad en uso? Explique con un ejemplo.
2. ¿Por qué SonarQube (calidad interna) no es suficiente para que MediSalud resuelva su problemática de lentitud percibida por los médicos?

### Conclusiones Parciales

El estudiante reconoce que la calidad en uso es el nivel más cercano al negocio y al paciente, y que por ello será el foco exclusivo del resto del taller, sin descuidar que se apoya en buenas prácticas de calidad interna y externa.

---

## 4. Identificación de Atributos de Calidad en Uso

**Objetivo del Escenario**

Identificar y definir atributos observables de calidad en uso dentro del sistema MediSalud HIS, aplicando el modelo Usuario–Tarea–Contexto como herramienta de descomposición analítica.

### 4.1 Parte 1 — Fundamento Teórico

#### 4.1.1 El modelo Usuario–Tarea–Contexto

Para medir calidad en uso es necesario descomponer la experiencia en tres dimensiones:

- **Usuario:** quién usa el sistema (perfil, rol, nivel de competencia digital).
- **Tarea:** qué intenta lograr el usuario (acción atómica medible).
- **Contexto:** bajo qué condiciones lo hace (ubicación, horario, dispositivo, estado del sistema).

#### 4.1.2 Atributos de calidad en uso

Un atributo es una propiedad medible de una tarea ejecutada por un usuario en un contexto específico. Por ejemplo:

- Tiempo promedio de registro de HCE → atributo de eficiencia.
- Tasa de errores de facturación por turno → atributo de efectividad.
- Índice de abandono de teleconsulta → atributo de satisfacción.

### 4.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Identificar al menos 10 atributos de calidad en uso para MediSalud HIS usando el modelo UTC |
| **Tiempo estimado:** | 3 horas |
| **Nivel de dificultad:** | Intermedio |
| **Herramientas requeridas:** | Hoja de cálculo o editor colaborativo (Google Sheets, Excel) |
| **Archivos / datos necesarios:** | Caso de estudio (escenarios 1–3), plantilla UTC provista |

#### Plantilla Usuario–Tarea–Contexto

| Usuario | Tarea | Contexto | Atributo | Característica |
|---|---|---|---|---|
| Médico | Registrar nota evolución | Consulta externa, horario pico, sede Quito | Tiempo promedio registro | Eficiencia |
| Paciente | Agendar cita | Portal web, noche, dispositivo móvil | Tasa de abandono | Satisfacción |
| Admisión | Facturar consulta | Fin de mes, sistema lento | Tasa de errores | Efectividad |
| Enfermería | Administrar medicamento | Turno nocturno, urgencias | Incidentes de seguridad | Libertad de Riesgo |
| Médico | Realizar teleconsulta | Domicilio, conexión limitada | Caídas de videollamada | Cobertura de Contexto |

*Tabla 4.1: Plantilla Usuario–Tarea–Contexto*

> **Resultado Esperado**
> Cada grupo identifica y documenta al menos 10 atributos con su correspondiente característica ISO/IEC 25022, evidenciando capacidad de descomposición analítica.

### Preguntas de Discusión

1. ¿Por qué es importante separar usuario, tarea y contexto antes de definir una métrica?
2. ¿Un mismo atributo puede pertenecer a más de una característica? Ponga un ejemplo.

### Conclusiones Parciales

El modelo UTC permite descomponer la calidad en uso en elementos concretos y medibles, preparando el terreno para el diseño de métricas en el Escenario 6.

---

## 5. Mapeo de Características de Calidad

**Objetivo del Escenario**

Priorizar las características de calidad en uso más relevantes para MediSalud según su impacto en el negocio, y construir una matriz de mapeo tarea–característica–prioridad.

### 5.1 Parte 1 — Fundamento Teórico

#### 5.1.1 ¿Por qué priorizar?

No todas las características de ISO/IEC 25022 tienen el mismo peso para una organización. Para MediSalud, la **Efectividad** (que los médicos puedan registrar HCE sin errores) puede ser más crítica que la **Cobertura de Contexto** en una primera iteración. Priorizar permite enfocar recursos limitados.

#### 5.1.2 Matriz de priorización

La priorización se realiza evaluando cada característica contra dos criterios:

- **Impacto en el negocio** (alto, medio, bajo).
- **Urgencia percibida** por stakeholders (alta, media, baja).

### 5.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Construir una matriz de mapeo tarea–característica–prioridad para MediSalud HIS |
| **Tiempo estimado:** | 2 horas |
| **Nivel de dificultad:** | Intermedio |
| **Herramientas requeridas:** | Hoja de cálculo, Miro o similar |
| **Archivos / datos necesarios:** | Lista de atributos del Escenario 4 |

#### Matriz de mapeo tarea–característica–prioridad (fragmento)

| Tarea | Efectividad | Eficiencia | Satisfacción | Libertad de Riesgo | Cobertura Contexto | Prioridad |
|---|---|---|---|---|---|---|
| Registrar HCE | Alto | Alto | Medio | Alto | Medio | **Crítica** |
| Agendar cita | Alto | Medio | Alto | Bajo | Medio | **Alta** |
| Facturar consulta | Alto | Medio | Bajo | Alto | Bajo | **Crítica** |
| Teleconsulta | Medio | Medio | Alto | Medio | Alto | **Alta** |

*Tabla 5.1: Matriz de mapeo tarea–característica–prioridad (fragmento)*

> **Resultado Esperado**
> Matriz de priorización completa con justificación de al menos 3 tareas clasificadas como críticas.

### Preguntas de Discusión

1. ¿Qué criterios adicionales usaría para priorizar características en un hospital público vs. uno privado?
2. ¿Cómo cambiaría la priorización si MediSalud estuviera en proceso de certificación ISO 9001?

### Conclusiones Parciales

La matriz de priorización conecta las características de la norma con las decisiones de negocio, permitiendo enfocar esfuerzos de medición donde generan mayor valor.

---

## 6. Diseño de Métricas

**Objetivo del Escenario**

Diseñar métricas de calidad en uso alineadas con ISO/IEC 25022, especificando fórmula, unidad, escala, fuente de datos y frecuencia de medición para cada atributo priorizado.

### 6.1 Parte 1 — Fundamento Teórico

#### 6.1.1 Anatomía de una métrica ISO/IEC 25022

Toda métrica en esta norma incluye:

- **Nombre:** identificador único.
- **Propósito:** qué se quiere medir y por qué.
- **Fórmula:** expresión matemática (generalmente un cociente).
- **Unidad:** segundos, porcentaje, tasa, etc.
- **Escala:** ordinal, intervalar, de razón.
- **Fuente de datos:** log, base de datos, encuesta, observación.
- **Frecuencia:** por transacción, por hora, diaria, semanal, mensual.
- **Meta (target):** valor deseado (ej. ≤ 8 segundos).

#### 6.1.2 Catálogo de métricas ISO/IEC 25022 aplicadas a MediSalud

| Código | Métrica | Fórmula | Unidad | Fuente | Característica |
|---|---|---|---|---|---|
| M-EFI-01 | Tiempo promedio registro HCE | Σ tiempo_i / n | segundos | Log HCE | Eficiencia |
| M-EFE-01 | Tasa de éxito agendamiento | (agendados / intentados) × 100 | % | BD Portal | Efectividad |
| M-SAT-01 | Índice abandono teleconsulta | (abandonos / iniciados) × 100 | % | App Móvil | Satisfacción |
| M-RIE-01 | Tasa de errores facturación | (errores / total) × 100 | % | BD Facturación | Libertad de Riesgo |
| M-CC-01 | Variabilidad tiempo HCE por sede | σ (tiempo por sede) | segundos | Log HCE | Cobertura Contexto |

*Tabla 6.1: Catálogo de métricas de Calidad en Uso — MediSalud HIS*

### 6.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Diseñar 10 métricas completas siguiendo la anatomía ISO/IEC 25022 |
| **Tiempo estimado:** | 3 horas |
| **Nivel de dificultad:** | Intermedio – Avanzado |
| **Herramientas requeridas:** | Hoja de cálculo o plantilla Markdown |
| **Archivos / datos necesarios:** | Atributos priorizados del Escenario 4, matriz del Escenario 5 |

> **Resultado Esperado**
> Catálogo de 10 métricas documentadas con nombre, fórmula, unidad, fuente, frecuencia y meta, listas para ser implementadas en los escenarios siguientes.

### Preguntas de Discusión

1. ¿Qué ocurre si una métrica tiene una meta demasiado ambiciosa o demasiado laxa?
2. ¿Es posible medir satisfacción sin encuestas? Proponga una métrica proxy.

### Conclusiones Parciales

El diseño riguroso de métricas es la base de un programa de medición confiable. Sin métricas bien definidas, los indicadores posteriores carecerán de validez.

---

## 7. Obtención de Datos

**Objetivo del Escenario**

Identificar las fuentes de datos disponibles en MediSalud HIS para alimentar las métricas diseñadas, evaluar su calidad y aplicar técnicas de extracción básicas.

### 7.1 Parte 1 — Fundamento Teórico

#### 7.1.1 Fuentes típicas de datos para Calidad en Uso

| Característica | Fuentes de datos típicas |
|---|---|
| Efectividad | Logs de transacciones, BD, bitácoras de auditoría |
| Eficiencia | Logs de rendimiento (APM), trazas de请求, temporizadores |
| Satisfacción | Encuestas NPS, CSAT, abandonment rate, reseñas |
| Libertad de Riesgo | Registros de incidentes de seguridad, auditoría de acceso |
| Cobertura de Contexto | Datos de uso por ubicación, horario, dispositivo |

*Tabla 7.1: Fuentes de datos según característica ISO/IEC 25022*

#### 7.1.2 Calidad del dato antes que calidad del indicador

Un indicador construido sobre datos incorrectos, incompletos o sesgados lleva a decisiones erróneas. Es necesario evaluar:

- **Completitud:** ¿faltan registros?
- **Exactitud:** ¿los datos reflejan la realidad?
- **Oportunidad:** ¿están disponibles cuando se necesitan?
- **Consistencia:** ¿coinciden entre fuentes?

### 7.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Extraer, limpiar y validar datos reales simulados de logs y BD de MediSalud HIS |
| **Tiempo estimado:** | 3 horas |
| **Nivel de dificultad:** | Intermedio |
| **Herramientas requeridas:** | Python, pandas, Jupyter Notebook |
| **Archivos / datos necesarios:** | Archivos simulados: logs_hce.csv (ver repositorio), encuestas_satisfaccion.csv |

> **Resultado Esperado**
> Dataset limpio y validado listo para ser utilizado en el cálculo de métricas del Escenario 8.

### Preguntas de Discusión

1. ¿Qué fuentes de datos adicionales recomendaría implementar a MediSalud para mejorar la medición de Satisfacción?
2. ¿Cómo detectaría datos inconsistentes entre logs de HCE y registros de facturación?

### Conclusiones Parciales

Sin datos de calidad no hay métricas confiables. La limpieza y validación de datos es una habilidad crítica del ingeniero de calidad.

---

## 8. Automatización de la Medición

**Objetivo del Escenario**

Automatizar el cálculo de métricas de calidad en uso mediante scripts en Python, estableciendo un pipeline reproducible que sirva como base para el programa permanente de medición.

### 8.1 Parte 1 — Fundamento Teórico

#### 8.1.1 ¿Por qué automatizar?

El cálculo manual de métricas no escala, introduce errores humanos y no permite generar reportes en tiempo real. La automatización garantiza consistencia, repetibilidad y trazabilidad.

#### 8.1.2 Arquitectura del pipeline de medición

```
                    ┌──────────────┐
                    │   Fuentes    │
                    │  de Datos    │
                    └──────┬───────┘
                           ▼
                    ┌──────────────┐
                    │  Extracción  │
                    │  (pandas)    │
                    └──────┬───────┘
                           ▼
                    ┌──────────────┐
                    │   Cálculo    │
                    │  de Métricas │
                    └──────┬───────┘
                           ▼
                    ┌──────────────┐
                    │   Reporte    │
                    │ (CSV / JSON) │
                    └──────────────┘
```

*Figura 8.1: Pipeline de automatización de la medición de Calidad en Uso*

### 8.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Escribir scripts en Python que calculen automáticamente las métricas del catálogo |
| **Tiempo estimado:** | 4 horas |
| **Nivel de dificultad:** | Avanzado |
| **Herramientas requeridas:** | Python, pandas, Jupyter Notebook / VS Code |
| **Archivos / datos necesarios:** | Datos limpios del Escenario 7, catálogo de métricas del Escenario 6 |

> **Resultado Esperado**
> Script(s) funcional(es) que lean datos, calculen métricas y exporten resultados a CSV/JSON, listos para ser integrados en un dashboard.

### Preguntas de Discusión

1. ¿Qué ventajas tiene almacenar los resultados de las métricas en una base de datos vs. archivos CSV?
2. ¿Cómo manejaría el pipeline la llegada de nuevos datos sin recalcular todo el histórico?

### Conclusiones Parciales

La automatización transforma un ejercicio académico en una herramienta de valor industrial. El pipeline construido en este escenario será la base del sistema de indicadores del Escenario 9.

---

## 9. Construcción de Indicadores

**Objetivo del Escenario**

Transformar las métricas calculadas en indicadores visuales (KPI) que faciliten la toma de decisiones, aplicando principios de visualización de datos y diseñando un dashboard ejecutivo.

### 9.1 Parte 1 — Fundamento Teórico

#### 9.1.1 De la métrica al indicador

- **Métrica:** valor numérico calculado (ej. 12.5 segundos).
- **Indicador:** métrica interpretada en contexto (ej. 12.5 segundos → supera la meta de 8 segundos → semáforo rojo).
- **KPI:** indicador vinculado a un objetivo estratégico del negocio (ej. "Tiempo promedio de registro HCE" es un KPI del objetivo "Mejorar eficiencia clínica").

#### 9.1.2 Principios de buena visualización de indicadores de calidad

- Simpleza: evitar gráficos recargados.
- Contexto: mostrar siempre la meta o línea base.
- Consistencia: usar los mismos colores, escalas y formatos.
- Accionabilidad: cada indicador debe sugerir una decisión.

### 9.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Diseñar y construir un dashboard de calidad en uso con 5–7 KPI |
| **Tiempo estimado:** | 3 horas |
| **Nivel de dificultad:** | Intermedio – Avanzado |
| **Herramientas requeridas:** | Plotly / Matplotlib / Power BI / Tableau (cualquier herramienta de visualización) |
| **Archivos / datos necesarios:** | Resultados del pipeline del Escenario 8 |

> **Resultado Esperado**
> Dashboard funcional con al menos 5 KPI visuales que permitan monitorear el estado de la calidad en uso de MediSalud HIS.

### Preguntas de Discusión

1. ¿Por qué un semáforo (verde/amarillo/rojo) es más efectivo que mostrar el valor numérico crudo en un dashboard ejecutivo?
2. ¿Qué indicador considera más relevante para la Gerencia de Calidad? ¿Y para la Dirección Médica?

### Conclusiones Parciales

Un buen indicador no solo informa, sino que impulsa la acción. El dashboard construido será la herramienta de comunicación con la alta dirección en el Escenario 11.

---

## 10. Interpretación de Resultados

**Objetivo del Escenario**

Desarrollar la capacidad de interpretar críticamente los indicadores de calidad en uso, identificando causas raíz, sesgos de medición y patrones engañosos.

### 10.1 Parte 1 — Fundamento Teórico

#### 10.1.1 Errores comunes de interpretación

- **Correlación ↔ causalidad:** una alta tasa de abandono de teleconsulta puede deberse a problemas de conexión del paciente, no necesariamente a mala usabilidad del sistema.
- **Sobre-generalización:** una métrica buena en promedio puede ocultar problemas graves en un subgrupo (ej. tiempo de HCE aceptable en promedio, pero pésimo en el hospital de Manta).
- **Fijarse solo en la tendencia:** un indicador que mejora lentamente puede hacer perder de vista que aún está lejos de la meta.

#### 10.1.2 Técnica de análisis de causa raíz (5 Por Qué)

Ejemplo aplicado a MediSalud:

> **Problema:** Tasa de error de facturación > 3%.
> 1. ¿Por qué? Porque el sistema permite reintentar el pago sin validar estado.
> 2. ¿Por qué? Porque la validación de idempotencia no se implementó.
> 3. ¿Por qué? Porque el equipo de desarrollo priorizó velocidad de entrega.
> 4. ¿Por qué? Porque no había una métrica de calidad en uso visibilizando el problema.
> 5. ¿Por qué? Porque no existía el programa de medición ISO/IEC 25022 (que este taller busca instaurar).

### 10.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Interpretar los resultados del dashboard y realizar análisis de causa raíz para al menos 2 indicadores fuera de meta |
| **Tiempo estimado:** | 3 horas |
| **Nivel de dificultad:** | Intermedio |
| **Herramientas requeridas:** | Dashboard del Escenario 9, plantilla de 5 Por Qué |
| **Archivos / datos necesarios:** | Resultados del dashboard, registro de incidentes |

> **Resultado Esperado**
> Informe de interpretación con análisis de causa raíz de al menos 2 indicadores críticos, incluyendo recomendaciones accionables.

### Preguntas de Discusión

1. ¿Qué indicador del dashboard podría estar mostrando una mejora ilusoria? ¿Cómo verificarlo?
2. ¿Cómo diferenciar entre un problema de usabilidad del software y un problema de capacitación del usuario?

### Conclusiones Parciales

La interpretación de indicadores es una habilidad analítica que distingue al ingeniero de calidad del técnico de datos. Sin interpretación, los números son solo números.

---

## 11. Presentación Ejecutiva para Directivos

**Objetivo del Escenario**

Preparar y presentar un informe ejecutivo de calidad en uso dirigido a la Dirección General de MediSalud, comunicando hallazgos técnicos en lenguaje de negocio y proponiendo acciones concretas.

### 11.1 Parte 1 — Fundamento Teórico

#### 11.1.1 Comunicar calidad de software a audiencias no técnicas

Los directivos no necesitan conocer la fórmula de ISO/IEC 25022; necesitan saber:

- ¿El software está ayudando o perjudicando al negocio?
- ¿Dónde debemos invertir para mejorar?
- ¿Qué retorno de inversión esperar?

#### 11.1.2 Estructura recomendada de un informe ejecutivo

1. Resumen ejecutivo (1 página).
2. Contexto: ¿qué medimos y por qué?
3. Hallazgos principales (3–5 indicadores clave).
4. Análisis de causa raíz (solo lo relevante para decisión).
5. Recomendaciones priorizadas.
6. Plan de acción y próximos pasos.
7. Anexos técnicos (opcional, para el equipo de TI).

### 11.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Preparar y presentar (simuladamente) un informe ejecutivo de 5 minutos ante la "Dirección General" |
| **Tiempo estimado:** | 3 horas |
| **Nivel de dificultad:** | Intermedio |
| **Herramientas requeridas:** | PowerPoint, Google Slides, Canva o similar |
| **Archivos / datos necesarios:** | Dashboard (Escenario 9), análisis de causa raíz (Escenario 10) |

> **Resultado Esperado**
> Presentación ejecutiva de máximo 5 diapositivas que comunique claramente el estado de la calidad en uso de MediSalud HIS y proponga 3 acciones concretas.

### Preguntas de Discusión

1. ¿Qué indicador mostraría primero a un director general? ¿Por qué?
2. ¿Cómo manejaría una reacción defensiva del área de TI durante la presentación?

### Conclusiones Parciales

La comunicación efectiva de resultados técnicos a audiencias no técnicas es una competencia diferenciadora del ingeniero de calidad. Un buen análisis que no se comunica bien es un análisis que no genera impacto.

---

## 12. Plan de Mejora Continua

**Objetivo del Escenario**

Diseñar un plan de mejora continua basado en el ciclo PDCA (Plan–Do–Check–Act) que institutionalice la medición de calidad en uso en MediSalud más allá del taller.

### 12.1 Parte 1 — Fundamento Teórico

#### 12.1.1 El ciclo PDCA aplicado a la Calidad en Uso

- **Plan:** definir objetivos, métricas y metas (lo hecho en escenarios 4–6).
- **Do:** ejecutar la medición automatizada (escenarios 7–8).
- **Check:** analizar indicadores y comparar con metas (escenarios 9–10).
- **Act:** tomar decisiones correctivas y actualizar el plan (escenario 11).

#### 12.1.2 Gobernanza del programa

Un programa de medición requiere:

- Dueño del programa (rol: Quality Manager).
- Comité de revisión periódica (cada 3 meses).
- Repositorio compartido de métricas, datos y reportes.
- Procedimiento de actualización del catálogo de métricas.

### 12.2 Parte 2 — Actividad Práctica

**Ficha de Laboratorio**

| | |
|---|---|
| **Objetivo:** | Diseñar el plan de mejora continua con cronograma, responsables y recursos |
| **Tiempo estimado:** | 2 horas |
| **Nivel de dificultad:** | Intermedio |
| **Herramientas requeridas:** | Hoja de cálculo o gestor de proyectos (Trello, Notion, Jira) |
| **Archivos / datos necesarios:** | Todos los entregables de escenarios anteriores |

#### Cronograma propuesto del programa de medición continua

| Actividad | Frecuencia | Responsable |
|---|---|---|
| Ejecución del pipeline de métricas | Semanal | Ingeniero de Calidad |
| Revisión de dashboard | Quincenal | Equipo de Calidad |
| Informe ejecutivo | Trimestral | Quality Manager |
| Auditoría del catálogo de métricas | Semestral | Comité de Calidad |
| Actualización de metas y prioridades | Anual | Dirección + Calidad |

*Tabla 12.1: Cronograma propuesto del programa de medición continua*

#### Matriz de responsables del programa de medición

| Rol | Responsabilidad |
|---|---|
| Quality Manager | Dueño del programa, reporta a Dirección |
| Ingeniero de Calidad | Ejecuta pipeline, mantiene dashboards |
| TI (DevOps) | Provee acceso a logs y BD |
| Dirección Médica | Valida relevancia clínica de métricas |
| Gerencia General | Aproba inversiones y metas |

*Tabla 12.2: Matriz de responsables del programa de medición*

> **Resultado Esperado**
> Plan de mejora continua documentado con cronograma, matriz de responsables y procedimiento de revisión, listo para ser presentado a la Dirección General.

### Preguntas de Discusión

1. ¿Qué riesgos enfrenta un programa de medición que no tiene un dueño claramente asignado?
2. ¿Cómo evitar que el programa se convierta en un "ejercicio de métricas por las métricas" sin impacto real?

### Conclusiones Parciales

La sostenibilidad del programa de medición depende más de la gobernanza que de la tecnología. Sin un plan de mejora continua, los esfuerzos de medición se diluyen después del entusiasmo inicial.

---

## Reto Final Integrador

**Objetivo**

Integrar todos los conocimientos y habilidades desarrollados a lo largo de los 12 escenarios en un proyecto completo de evaluación de calidad en uso para un nuevo módulo de MediSalud HIS.

**Enunciado**

La Gerencia de Calidad de MediSalud ha aprobado el desarrollo de un nuevo módulo: **"Portal de Telemedicina 2.0"**, que reemplazará al actual sistema de videoconsultas. Su equipo ha sido contratado para diseñar e implementar el programa de medición de calidad en uso desde el inicio del proyecto (Shift-Left Quality).

**Entregables**

1. Definición del modelo Usuario–Tarea–Contexto para Telemedicina 2.0.
2. Catálogo de métricas ISO/IEC 25022 (mínimo 8 métricas).
3. Scripts automatizados de medición en Python.
4. Dashboard de indicadores (mínimo 5 KPI).
5. Informe ejecutivo con recomendaciones.

**Duración:** 4 horas (en clase) + trabajo autónomo.

---

## Solución Propuesta del Reto Final

### Ficha UTC de Telemedicina 2.0

| Usuario | Tarea | Contexto |
|---|---|---|
| Paciente | Iniciar videoconsulta | Conexión 4G, horario nocturno |
| Médico | Revisar resultados en videollamada | Compartiendo pantalla, sede Quito |
| Paciente | Subir receta médica | App móvil, Android versión anterior |
| Médico | Recetar en línea | Post-consulta, desde casa |

*Tabla 12.3: Solución: ficha Usuario–Tarea–Contexto de Telemedicina 2.0*

### Catálogo de métricas de Telemedicina 2.0

| Código | Métrica | Fórmula | Característica |
|---|---|---|---|
| TM-EFI-01 | Latencia de inicio videollamada | Percentil 90 (tiempo inicio) | Eficiencia |
| TM-EFE-01 | Tasa de conexión exitosa | (conexiones exitosas / intentos) × 100 | Efectividad |
| TM-SAT-01 | NPS post-consulta | Encuesta 0–10 | Satisfacción |
| TM-RIE-01 | Incidentes de privacidad | Conteo mensual | Libertad de Riesgo |
| TM-CC-01 | Tasa de éxito por dispositivo | % por tipo dispositivo | Cobertura Contexto |

*Tabla 12.4: Solución: catálogo de métricas de Telemedicina 2.0*

---

## Rúbrica de Evaluación

| Criterio | Excelente (4) | Bueno (3) | Suficiente (2) | Insuficiente (1) |
|---|---|---|---|---|
| Comprensión de ISO/IEC 25022 | Clasifica correctamente las 5 características con ejemplos propios | Clasifica 4–5 características | Clasifica 2–3 características | No diferencia características |
| Diseño de métricas | 10 métricas completas con fórmula, fuente y meta | 7–9 métricas completas | 4–6 métricas completas | < 4 métricas |
| Automatización (Python) | Pipeline completo, documentado, reusable | Pipeline funcional, sin documentación | Script parcial, errores menores | No funciona o no entregado |
| Dashboard | 7+ KPI, interactivo, diseño profesional | 5–6 KPI, funcional | 3–4 KPI, básico | < 3 KPI |
| Informe ejecutivo | Claro, convincente, 3 acciones concretas | Claro, 2 acciones | Presentación confusa | No entregado |
| Plan de mejora continua | Completo con gobernanza, cronograma y responsables | Completo pero sin responsables | Plan básico sin cronograma | No entregado |

*Tabla 12.5: Rúbrica de evaluación del Reto Final Integrador*

---

## Glosario

- **Calidad en Uso (Quality in Use):** grado en que un producto software permite a usuarios específicos alcanzar objetivos específicos con efectividad, eficiencia, satisfacción, libertad de riesgo y cobertura de contexto en un contexto de uso específico.
- **Efectividad:** precisión y completitud con que los usuarios logran sus objetivos.
- **Eficiencia:** recursos gastados en relación con la efectividad alcanzada.
- **Satisfacción:** respuesta positiva del usuario ante la interacción con el sistema.
- **Libertad de Riesgo:** capacidad del sistema para mitigar riesgos económicos, de salud, seguridad o ambientales.
- **Cobertura de Contexto:** capacidad del sistema para funcionar correctamente en diversos contextos de uso.
- **SQuaRE:** Software product Quality Requirements and Evaluation — familia ISO/IEC 25000.
- **Métrica:** función de medición definida para cuantificar un atributo de calidad.
- **Indicador (KPI):** métrica interpretada en contexto, vinculada a un objetivo de negocio.
- **PDCA:** Plan–Do–Check–Act, ciclo de mejora continua.

---

## Lista de Acrónimos

| Acrónimo | Significado |
|---|---|
| HCE | Historia Clínica Electrónica |
| HIS | Hospital Information System |
| ISO | International Organization for Standardization |
| KPI | Key Performance Indicator |
| NPS | Net Promoter Score |
| PDCA | Plan–Do–Check–Act |
| RNF | Requerimiento No Funcional |
| SQuaRE | Software product Quality Requirements and Evaluation |
| UTC | Usuario–Tarea–Contexto |

---

## Anexos

### Comandos frecuentes utilizados a lo largo del taller

| Comando | Propósito |
|---|---|
| `python -m venv venv` | Crear entorno virtual |
| `source venv/bin/activate` | Activar entorno virtual (Linux/macOS) |
| `venv\Scripts\activate` | Activar entorno virtual (Windows) |
| `pip install pandas numpy matplotlib plotly jupyter openpyxl` | Instalar dependencias del taller |
| `git clone <url>` | Clonar repositorio |
| `git add . && git commit -m "mensaje"` | Guardar cambios |
| `jupyter notebook` | Iniciar Jupyter Notebook |
| `python script.py` | Ejecutar script Python |

*Tabla 12.6: Comandos frecuentes utilizados a lo largo del taller*
