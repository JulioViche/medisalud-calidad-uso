# Plan de Implementación Arquitectónica — MediSalud HIS

## ISO/IEC 25022 — Sistema de Medición de Calidad en Uso

---

## 1. Arquitectura General

```
┌────────────────────────────────────────────────────────────────────────────┐
│                            Nginx (Reverse Proxy)                           │
│                         Puerto 80 → localhost                              │
└────────────────────────────────────────┬───────────────────────────────────┘
                                         │
                                         ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                            API Gateway                                     │
│                    Enrutamiento /api/v1/* a microservicios                  │
└──────┬──────────────────────────────────────────────┬──────────────────────┘
       │                                              │
       ▼                                              ▼
┌──────────────────────┐                  ┌──────────────────────────────┐
│  Frontend Web (React) │                  │  Aplicación Móvil (Flutter)  │
│  Dashboard SPA        │                  │  Consulta de indicadores    │
│  Puerto 3000          │                  │  Puerto 3001                │
└──────────────────────┘                  └──────────────────────────────┘
       │                                              │
       └──────────────────┬───────────────────────────┘
                          │
                          ▼
       ┌──────────────────────────────────────────────────────┐
       │                  RabbitMQ (Colas)                     │
       │  Exchange: calidad.logs, calidad.incidentes          │
       │  Queues: pipeline_hce, pipeline_encuestas            │
       └──────────┬───────────────────────────┬───────────────┘
                  │                           │
                  ▼                           ▼
┌─────────────────────────┐    ┌─────────────────────────────┐
│  Microservicio HCE      │    │  Microservicio Mediciones   │
│  Spring Boot (Java 17)  │    │  FastAPI (Python 3.12)      │
│  Simula logs de HCE     │    │  API REST /api/v1/*         │
│  Publica en RabbitMQ    │    │  Calcula métricas ISO 25022 │
│  Puerto 8081            │    │  Puerto 8000                │
└──────────┬──────────────┘    └──────────┬──────────────────┘
           │                              │
           │     ┌────────────────────────┘
           │     ▼
           │  ┌─────────────────────────────┐
           │  │  Microservicio Facturación  │
           ├──│  Spring Boot (Java 17)      │
           │  │  Simula transacciones       │
           │  │  Publica en RabbitMQ        │
           │  │  Puerto 8082                │
           │  └──────────┬──────────────────┘
           │             │
           ▼             ▼
┌────────────────────────────────────────────────────────────────┐
│                          PostgreSQL 16                          │
│  Base transaccional del sistema de medición                     │
│  Esquemas: calidad (métricas, KPIs, logs_hce, encuestas,       │
│            incidentes, ejecuciones_pipeline)                    │
│  Puerto 5432                                                    │
└──────────────┬─────────────────────────────────┬───────────────┘
               │                                 │
               ▼                                 ▼
┌─────────────────────────────┐  ┌─────────────────────────────┐
│  SQL Server (legacy)        │  │  Observabilidad             │
│  Módulo financiero heredado │  │  Logs centralizados         │
│  Datos de facturación       │  │  (archivos .log rotativos)  │
│  Puerto 1433                │  │  Sin estandarizar aún       │
└─────────────────────────────┘  └─────────────────────────────┘
```

### Contenedores Docker

| Servicio | Imagen | Puerto | Tecnología | Depende de |
|---|---|---|---|---|
| `nginx` | nginx:alpine | 80 → localhost | Reverse proxy | api, frontend, flutter |
| `api-gateway` | medisalud-gateway | 8000 | Spring Cloud Gateway | db |
| `frontend` | medisalud-frontend | 3000 | React + Vite | api-gateway |
| `flutter-app` | medisalud-flutter | 3001 | Flutter web | api-gateway |
| `ms-hce` | medisalud-ms-hce | 8081 | Spring Boot + Java 17 | db, rabbitmq |
| `ms-facturacion` | medisalud-ms-facturacion | 8082 | Spring Boot + Java 17 | db, rabbitmq |
| `ms-mediciones` | medisalud-ms-mediciones | 8001 | FastAPI + Python 3.12 | db, rabbitmq |
| `rabbitmq` | rabbitmq:3-management | 5672, 15672 | Colas asíncronas | — |
| `db` | postgres:16-alpine | 5432 | PostgreSQL | — |
| `db-legacy` | mcr.microsoft.com/mssql/server:2022-latest | 1433 | SQL Server | — |
| `pipeline-worker` | medisalud-pipeline | — | Python (servicio interno) | db, rabbitmq |

---

## 2. Tecnologías (alineadas con el documento)

| Capa | Documento dice | Implementación |
|---|---|---|
| Frontend web | React SPA | React 18 + TypeScript + Vite + Recharts |
| App móvil | Android/iOS (Flutter) | Flutter 3 + Dart (web build para taller) |
| Backend 1 | Spring Boot | Spring Boot 3 + Java 17 (ms-hce, ms-facturacion) |
| Backend 2 | FastAPI | FastAPI + SQLAlchemy asyncio (ms-mediciones) |
| API Gateway | API Gateway | Spring Cloud Gateway |
| BD transaccional | PostgreSQL | PostgreSQL 16 |
| BD heredada | SQL Server | SQL Server 2022 (módulo financiero legacy) |
| Mensajería | RabbitMQ | RabbitMQ 3 (colas calidad.logs, calidad.incidentes) |
| Infraestructura | Docker + orquestación | Docker Compose + clúster on-premise simulado |
| Servidor web | Nginx | Nginx (reverse proxy + static files) |
| CI/CD | Jenkins → GitHub Actions | GitHub Actions (build + test + docker) |
| Observabilidad | Logs centralizados (incipientes) | Archivos .log rotativos (sin estandarizar aún) |

---

## 3. Errores Intencionales Preservados (Práctica Pedagógica)

El taller está diseñado para que los estudiantes identifiquen y corrijan estos errores. Se incorporan deliberadamente en el código base.

### 3.1 Infraestructura

| # | Error | Dónde | Cómo se manifiesta |
|---|---|---|---|
| E01 | `dashboards/` no existe | Directorio raíz | `generar_dashboard.py` falla al escribir |
| E02 | `venv/` no creado | Directorio raíz | `ModuleNotFoundError` al ejecutar scripts |
| E03 | Dependencias no instaladas | Sistema | `import pandas` lanza excepción |
| E04 | Archivos generados en `.gitignore` pero ausentes | `data/` | `pipeline_medicion.py` falla al leer CSVs |
| E05 | Puerto 80 sin configuración | `nginx/default.conf` | Nginx no inicia sin config |
| E06 | Volumen de BD no persistente | `docker-compose.yml` | Datos se pierden al reiniciar contenedor |

### 3.2 Código Backend (FastAPI — ms-mediciones)

| # | Error | Archivo | Línea | Evidencia |
|---|---|---|---|---|
| E07 | Sin `if __name__ == "__main__"` | Todos los `routers/*.py` | — | Los módulos se ejecutan al importarse |
| E08 | Sin manejo de errores E/S | `routers/pipeline.py` | — | `pd.read_csv()` sin `try/except` |
| E09 | Import no usado | `routers/kpi.py` | 1-5 | `import plotly.express`, `json`, etc. declarados pero no usados |
| E10 | Import en medio del archivo | `routers/dashboard.py` | 42 | `import plotly.io` no está al inicio |
| E11 | Variable sin usar | `services/metric_calculator.py` | 10 | `horarios = ["manana", "tarde", "noche"]` declarada pero no referenciada |
| E12 | Endpoint sin validación de parámetros | `routers/incidentes.py` | — | `GET /incidentes` acepta cualquier query param sin sanitizar |
| E13 | Umbrales de semáforo hardcodeados | `services/metric_calculator.py` | 25-40 | `VERDE if valor <= 8` en lugar de leer de BD |
| E14 | Fechas en formato inconsistente | `schemas.py` | — | Incidentes con `MM/DD/YYYY` vs logs con `YYYY-MM-DD` |
| E15 | Sin autenticación | `main.py` | — | API expuesta sin API key ni JWT |
| E16 | Sin rate limiting | Ningún router | — | No hay protección contra abuso de endpoints |
| E17 | CORS configurado como `*` | `main.py` | `allow_origins=["*"]` | Permite cualquier origen en producción |
| E18 | Sin paginación en listados | `routers/incidentes.py` | — | `GET /incidentes` devuelve todos los registros |
| E19 | Modelos ORM sin constraints | `models.py` | — | `nps` permite valores fuera de 1-10 |
| E20 | Conexión a BD sin pool limits | `database.py` | — | `create_async_engine()` sin límite de conexiones |
| E21 | Logging mínimo | `services/pipeline_service.py` | — | Solo `print()` en lugar de `logging` estructurado |
| E22 | Sin health check real | `routers/health.py` | — | `GET /health` no verifica conexión a BD |

### 3.3 Código Frontend (React)

| # | Error | Archivo | Línea | Evidencia |
|---|---|---|---|---|
| E23 | Sin TypeScript strict mode | `tsconfig.json` | — | `strict: false` permite `any` implícito |
| E24 | Sin manejo de errores HTTP | `api/client.ts` | — | No hay interceptors para errores 4xx/5xx |
| E25 | Sin estado de carga | `pages/Dashboard.tsx` | — | No muestra spinner mientras fetch |
| E26 | Sin estado vacío | `components/MetricasTable.tsx` | — | Tabla no muestra mensaje si no hay datos |
| E27 | Sin tests | `src/` | — | `__tests__/` no existe |
| E28 | Sin lazy loading | `App.tsx` | — | `import` estático de todas las páginas |
| E29 | Sin responsividad | `components/*.tsx` | — | Charts no se adaptan a mobile |
| E30 | Sin accesibilidad | `components/*.tsx` | — | Faltan `aria-label`, roles semánticos |
| E31 | API URL hardcodeada | `api/client.ts` | — | `baseURL: "http://localhost:8000"` sin variable de entorno |
| E32 | Sin key en listas de React | `components/KpiCard.tsx` | — | `map()` sin `key` prop |

### 3.4 Código Flutter

| # | Error | Archivo | Línea | Evidencia |
|---|---|---|---|---|
| E33 | Sin `const` constructors | `lib/screens/dashboard.dart` | — | Widgets rebuild sin necesidad |
| E34 | Sin manejo de null safety | `lib/services/api_service.dart` | — | `String?` sin verificación |
| E35 | Sin tests widget | `test/` | — | No existen tests |

### 3.6 CI/CD

| # | Error | Archivo | Línea | Evidencia |
|---|---|---|---|---|
| E36 | Sin tests en pipeline | `.github/workflows/ci.yml` | — | Solo build, no ejecuta `pytest` |
| E37 | Sin linting | `.github/workflows/ci.yml` | — | No corre `flake8` ni `eslint` |
| E38 | Sin análisis de seguridad | `.github/workflows/ci.yml` | — | No hay `trivy` ni `snyk` |

---

## 4. Base de Datos — PostgreSQL

### 4.1 Esquema `init.sql`

```sql
-- database/init.sql
-- ERROR INTENCIONAL E06: No hay CREATE DATABASE ni verificación de existencia
-- ERROR INTENCIONAL E14: Fechas sin normalizar (TIMESTAMP vs DATE inconsistente)

CREATE SCHEMA IF NOT EXISTS calidad;

-- Tablas de referencia
CREATE TABLE calidad.sedes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE calidad.roles_usuario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE calidad.modulos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL
);

-- Logs del módulo HCE
CREATE TABLE calidad.logs_hce (
    id SERIAL PRIMARY KEY,
    id_transaccion VARCHAR(20) UNIQUE NOT NULL,
    fecha TIMESTAMP NOT NULL,
    sede_id INT REFERENCES calidad.sedes(id),
    rol_usuario_id INT REFERENCES calidad.roles_usuario(id),
    modulo_id INT REFERENCES calidad.modulos(id),
    accion VARCHAR(100) NOT NULL,
    tiempo_segundos NUMERIC(6,1) NOT NULL,
    es_hora_pico BOOLEAN NOT NULL,
    exitosa BOOLEAN NOT NULL
);
-- ERROR INTENCIONAL: Faltan índices para consultas frecuentes (por sede, fecha)

-- Encuestas de satisfacción
CREATE TABLE calidad.encuestas (
    id SERIAL PRIMARY KEY,
    id_encuesta VARCHAR(20) UNIQUE NOT NULL,
    fecha DATE NOT NULL,
    sede_id INT REFERENCES calidad.sedes(id),
    rol_usuario_id INT REFERENCES calidad.roles_usuario(id),
    nps INT,  -- ERROR INTENCIONAL E19: Falta CHECK (nps BETWEEN 1 AND 10)
    csat INT, -- ERROR INTENCIONAL E19: Falta CHECK (csat BETWEEN 1 AND 5)
    recomendaria VARCHAR(10)
);

-- Incidentes reportados
CREATE TABLE calidad.incidentes (
    id INT PRIMARY KEY,
    fecha DATE NOT NULL,
    modulo_id INT REFERENCES calidad.modulos(id),
    descripcion TEXT NOT NULL,
    rol_usuario_id INT REFERENCES calidad.roles_usuario(id),
    sede_id INT REFERENCES calidad.sedes(id)
);

-- Incidentes clasificados
CREATE TABLE calidad.incidentes_clasificados (
    incidente_id INT PRIMARY KEY REFERENCES calidad.incidentes(id),
    caracteristica VARCHAR(50) NOT NULL
);

-- Catálogo de métricas
CREATE TABLE calidad.catalogo_metricas (
    codigo VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    caracteristica VARCHAR(50) NOT NULL,
    formula TEXT NOT NULL,
    unidad VARCHAR(50) NOT NULL,
    meta VARCHAR(50) NOT NULL
);

-- Resultados de métricas
CREATE TABLE calidad.resultados_metricas (
    id SERIAL PRIMARY KEY,
    codigo_metrica VARCHAR(20) REFERENCES calidad.catalogo_metricas(codigo),
    valor NUMERIC(10,2) NOT NULL,
    estado VARCHAR(10),
    fecha_ejecucion TIMESTAMP DEFAULT NOW()
);
-- ERROR INTENCIONAL: Falta UNIQUE (codigo_metrica, fecha_ejecucion) permitiendo duplicados

-- Umbrales para semáforo
CREATE TABLE calidad.umbrales (
    codigo_metrica VARCHAR(20) REFERENCES calidad.catalogo_metricas(codigo),
    verde_hasta NUMERIC(10,2),
    amarillo_hasta NUMERIC(10,2),
    PRIMARY KEY (codigo_metrica)
);

-- ERROR INTENCIONAL E05: No hay volumen persistente en docker-compose
-- ERROR INTENCIONAL E06: No hay tabla ejecuciones_pipeline (falta de trazabilidad)
```

### 4.2 SQL Server (legacy)

```sql
-- database/legacy/init.sql
-- Módulo financiero heredado (simulado)
-- ERROR INTENCIONAL: Schema desnormalizado, fechas en VARCHAR

CREATE TABLE financiero.facturas (
    id INT IDENTITY(1,1) PRIMARY KEY,
    paciente_nombre VARCHAR(100),
    monto DECIMAL(10,2),
    fecha_emision VARCHAR(20),  -- ERROR: VARCHAR en lugar de DATE
    seguro_nombre VARCHAR(50),
    estado VARCHAR(20)
);

CREATE TABLE financiero.pagos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    factura_id INT REFERENCES financiero.facturas(id),
    monto DECIMAL(10,2),
    metodo_pago VARCHAR(30),
    fecha_pago VARCHAR(20),  -- ERROR: VARCHAR en lugar de DATE
    duplicado BIT DEFAULT 0
);
-- ERROR INTENCIONAL: No hay índices, no hay constraints CHECK
```

---

## 5. Microservicios Spring Boot (Java)

### 5.1 ms-hce (simulador de logs)

```java
// ms-hce/src/main/java/com/medisalud/hce/HceApplication.java
package com.medisalud.hce;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HceApplication {
    public static void main(String[] args) {
        SpringApplication.run(HceApplication.class, args);
    }
}
```

```java
// ms-hce/src/main/java/com/medisalud/hce/controller/LogController.java
package com.medisalud.hce.controller;

import com.medisalud.hce.model.LogHce;
import com.medisalud.hce.service.LogGeneratorService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/logs")
public class LogController {

    private final LogGeneratorService logGeneratorService;

    public LogController(LogGeneratorService logGeneratorService) {
        this.logGeneratorService = logGeneratorService;
    }

    @PostMapping("/generar")
    public String generarLogs(@RequestParam(defaultValue = "100") int cantidad) {
        // ERROR INTENCIONAL: Sin validación de cantidad máxima
        // ERROR INTENCIONAL: Sin try-catch
        logGeneratorService.generarYPublicar(cantidad);
        return "OK: " + cantidad + " logs generados";
    }

    @GetMapping
    public List<LogHce> obtenerTodos() {
        // ERROR INTENCIONAL: Sin paginación
        return logGeneratorService.obtenerTodos();
    }
}
```

```java
// ms-hce/src/main/java/com/medisalud/hce/service/LogGeneratorService.java
package com.medisalud.hce.service;

import com.medisalud.hce.model.LogHce;
import com.medisalud.hce.repository.LogHceRepository;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Random;

@Service
public class LogGeneratorService {

    private final LogHceRepository repository;
    private final RabbitTemplate rabbitTemplate;
    private final Random random = new Random(42);  // Semilla fija para reproducibilidad

    private final String[] sedes = {"Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"};
    private final String[] roles = {"Medico", "Enfermeria", "Admision"};
    // ERROR INTENCIONAL E11: Variable horarios declarada pero nunca usada
    private final String[] horarios = {"manana", "tarde", "noche"};

    public LogGeneratorService(LogHceRepository repository, RabbitTemplate rabbitTemplate) {
        this.repository = repository;
        this.rabbitTemplate = rabbitTemplate;
    }

    public void generarYPublicar(int cantidad) {
        for (int i = 0; i < cantidad; i++) {
            LogHce log = generarLog();
            repository.save(log);
            rabbitTemplate.convertAndSend("calidad.logs", "hce.logs", log);
        }
    }

    private LogHce generarLog() {
        String sede = sedes[random.nextInt(sedes.length)];
        String rol = roles[random.nextInt(roles.length)];
        int hora = 7 + random.nextInt(12);
        boolean esPico = hora >= 10 && hora <= 12;
        double tiempoBase = 6 + random.nextGaussian() * 2;
        if (esPico) tiempoBase *= 1.5 + random.nextDouble() * 1.5;
        if (sede.equals("Manta")) tiempoBase *= 1.2 + random.nextDouble() * 0.3;
        double tiempo = Math.max(0.5, Math.round(tiempoBase * 10.0) / 10.0);

        LogHce log = new LogHce();
        log.setIdTransaccion("TXN-" + System.currentTimeMillis());
        log.setFecha(LocalDateTime.now());
        log.setSede(sede);
        log.setRolUsuario(rol);
        log.setModulo("HCE");
        log.setAccion("registrar_nota_evolucion");
        log.setTiempoSegundos(tiempo);
        log.setEsHoraPico(esPico);
        log.setExitosa(tiempo < 20);
        return log;
    }

    public List<LogHce> obtenerTodos() {
        return repository.findAll();
    }
}
```

```properties
# ERROR INTENCIONAL: Puerto hardcodeado
server.port=8081
spring.datasource.url=jdbc:postgresql://db:5432/medisalud_calidad
spring.datasource.username=medisalud
spring.datasource.password=medisalud_pass
spring.rabbitmq.host=rabbitmq
spring.rabbitmq.port=5672
```

### 5.2 ms-facturacion (simulador de transacciones financieras)

```java
// Estructura idéntica a ms-hce, simulando transacciones de facturación
// ERROR INTENCIONAL: Conecta a SQL Server (legacy) como fuente de datos heredada
// ERROR INTENCIONAL: Sin manejo de errores si SQL Server no está disponible
```

---

## 6. Microservicio FastAPI (ms-mediciones)

### 6.1 Estructura

```
ms-mediciones/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI app
│   ├── config.py                  # Settings
│   ├── database.py                # SQLAlchemy async engine
│   ├── models.py                  # ORM models
│   ├── schemas.py                 # Pydantic schemas
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── metricas.py            # GET /api/v1/metricas
│   │   ├── kpi.py                 # GET /api/v1/kpi
│   │   ├── incidentes.py          # GET /api/v1/incidentes
│   │   ├── pipeline.py            # POST /api/v1/pipeline/ejecutar
│   │   └── encuestas.py           # GET /api/v1/encuestas
│   └── services/
│       ├── __init__.py
│       ├── pipeline_service.py
│       └── metric_calculator.py
├── requirements.txt
├── Dockerfile
└── .env.example
```

### 6.2 `main.py`

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import metricas, kpi, incidentes, pipeline, encuestas
from app.database import engine, Base

app = FastAPI(
    title="MediSalud HIS — Quality in Use API",
    version="1.0.0",
)

# ERROR INTENCIONAL E17: CORS abierto a cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(metricas.router, prefix="/api/v1")
app.include_router(kpi.router, prefix="/api/v1")
app.include_router(incidentes.router, prefix="/api/v1")
app.include_router(pipeline.router, prefix="/api/v1")
app.include_router(encuestas.router, prefix="/api/v1")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/api/v1/health")
async def health():
    # ERROR INTENCIONAL E22: No verifica conexión a BD
    return {"status": "ok", "version": "1.0.0"}
```

### 6.3 `services/metric_calculator.py`

```python
# ERROR INTENCIONAL E07: Sin if __name__ guard
# ERROR INTENCIONAL E13: Umbrales hardcodeados (deberían venir de BD)
# ERROR INTENCIONAL E09: Imports sin usar (dejados deliberadamente)

import json  # ERROR: No usado
import plotly.express as px  # ERROR: No usado

async def calculate_tiempo_promedio_hce(db) -> dict:
    row = await db.execute("""
        SELECT AVG(tiempo_segundos) FROM calidad.logs_hce
    """)
    valor = row.scalar() or 0
    estado = "VERDE" if valor <= 8 else "AMARILLO" if valor <= 12 else "ROJO"
    return {"codigo": "M-EFI-01", "valor": round(valor, 2), "estado": estado}


async def calculate_nps_promedio(db) -> dict:
    row = await db.execute("""
        SELECT AVG(nps) FROM calidad.encuestas
    """)
    valor = row.scalar() or 0
    estado = "VERDE" if valor >= 7 else "AMARILLO" if valor >= 4 else "ROJO"
    return {"codigo": "M-SAT-01", "valor": round(valor, 2), "estado": estado}


async def calculate_all_metrics(db) -> list[dict]:
    return [
        await calculate_tiempo_promedio_hce(db),
        await calculate_nps_promedio(db),
    ]
```

### 6.4 `routers/kpi.py`

```python
from fastapi import APIRouter, Depends
from app.database import get_db

router = APIRouter()

# ERROR INTENCIONAL E10: Import en medio del archivo
import plotly.io as pio  # ERROR: Debería estar al inicio

@router.get("/kpi")
async def get_kpi(db=Depends(get_db)):
    # ERROR INTENCIONAL E08: Sin try/except
    # ERROR INTENCIONAL E09: pio importado pero no usado
    resultados = await db.execute("SELECT * FROM calidad.resultados_metricas ORDER BY fecha_ejecucion DESC LIMIT 9")
    metricas = resultados.fetchall()
    return {"metricas": [dict(m) for m in metricas]}
```

---

## 7. Frontend React

### 7.1 Estructura

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── api/
│   │   └── client.ts
│   ├── pages/
│   │   └── Dashboard.tsx
│   ├── components/
│   │   ├── SemaforoGeneral.tsx
│   │   ├── KpiCard.tsx
│   │   ├── TiempoSedeChart.tsx
│   │   ├── IncidentesPieChart.tsx
│   │   ├── NpsSedeChart.tsx
│   │   ├── ExitoPicoChart.tsx
│   │   ├── IncidentesModuloChart.tsx
│   │   ├── CsatDistChart.tsx
│   │   └── MetricasTable.tsx
│   └── types/
│       └── index.ts
├── package.json
├── tsconfig.json
├── vite.config.ts
├── Dockerfile
└── nginx.conf
```

### 7.2 `tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "strict": false,  // ERROR INTENCIONAL E23: Strict mode desactivado
    "jsx": "react-jsx",
    "moduleResolution": "bundler"
  }
}
```

### 7.3 `api/client.ts`

```typescript
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',  // ERROR INTENCIONAL E31: URL hardcodeada
  timeout: 10000,
});

// ERROR INTENCIONAL E24: Sin interceptors para errores 4xx/5xx
// ERROR INTENCIONAL: Sin retry logic

export default api;
```

### 7.4 `pages/Dashboard.tsx`

```tsx
import { useEffect, useState } from 'react';
import api from '../api/client';
import SemaforoGeneral from '../components/SemaforoGeneral';
import KpiCard from '../components/KpiCard';

export default function Dashboard() {
  const [data, setData] = useState(null);
  // ERROR INTENCIONAL E25: Sin estado de carga (isLoading)
  // ERROR INTENCIONAL E26: Sin estado vacío
  // ERROR INTENCIONAL: Sin manejo de error en useEffect

  useEffect(() => {
    api.get('/api/v1/kpi').then(res => setData(res.data));
  }, []);

  if (!data) return null;  // ERROR: Sin spinner, pantalla en blanco

  return (
    <div>
      <SemaforoGeneral resumen={data.resumen_semaforo} />
      {data.metricas?.map(m => (
        <KpiCard key={m.codigo} metrica={m} />  // ERROR INTENCIONAL E32: key prop correcta (caso raro)
      ))}
    </div>
  );
}
```

---

## 8. Aplicación Flutter

### 8.1 Estructura

```
flutter_app/
├── lib/
│   ├── main.dart
│   ├── screens/
│   │   ├── dashboard_screen.dart
│   │   └── metric_detail_screen.dart
│   ├── widgets/
│   │   ├── kpi_card.dart
│   │   └── semaforo_indicator.dart
│   ├── services/
│   │   └── api_service.dart
│   └── models/
│       ├── metrica.dart
│       └── dashboard_kpi.dart
├── test/
│   └── widget_test.dart  // ERROR INTENCIONAL E35: Test vacío
├── pubspec.yaml
└── Dockerfile
```

### 8.2 `lib/services/api_service.dart`

```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // ERROR INTENCIONAL E31: URL hardcodeada
  static const String baseUrl = 'http://localhost:8000';

  Future<Map<String, dynamic>> fetchKpi() async {
    // ERROR INTENCIONAL E34: Sin manejo de null safety
    final response = await http.get(Uri.parse('$baseUrl/api/v1/kpi'));
    // ERROR INTENCIONAL E34: Sin verificación de statusCode
    return json.decode(response.body);
  }
}
```

### 8.3 `lib/screens/dashboard_screen.dart`

```dart
import 'package:flutter/material.dart';
import '../services/api_service.dart';

class DashboardScreen extends StatefulWidget {
  @override
  State<DashboardScreen> createState() => DashboardScreenState();
}

class DashboardScreenState extends State<DashboardScreen> {
  Map<String, dynamic>? kpiData;
  // ERROR INTENCIONAL E33: Sin const constructor

  @override
  void initState() {
    super.initState();
    ApiService().fetchKpi().then((data) {
      setState(() {
        kpiData = data;
      });
    });
    // ERROR INTENCIONAL: Sin manejo de error en then()
    // ERROR INTENCIONAL: Sin estado de carga
  }

  @override
  Widget build(BuildContext context) {
    if (kpiData == null) return Container();  // Pantalla en blanco
    return Scaffold(
      appBar: AppBar(title: Text('MediSalud HIS — Calidad en Uso')),
      body: ListView(
        children: [
          Text('Semáforo: ${kpiData!['resumen_semaforo']}'),  // Sin verificación de null
        ],
      ),
    );
  }
}
```

---

## 9. Colas RabbitMQ

```yaml
# rabbitmq/definitions.json
{
  "rabbit_version": "3.12",
  "exchanges": [
    {"name": "calidad.logs", "type": "topic", "durable": true},
    {"name": "calidad.incidentes", "type": "fanout", "durable": true}
  ],
  "queues": [
    {"name": "pipeline.hce", "durable": true},
    {"name": "pipeline.encuestas", "durable": true}
  ],
  "bindings": [
    {"source": "calidad.logs", "destination": "pipeline.hce", "routing_key": "hce.*"},
    {"source": "calidad.logs", "destination": "pipeline.encuestas", "routing_key": "*.encuestas"}
  ]
}
```

---

## 10. Docker Compose

```yaml
# docker-compose.yml
# ERROR INTENCIONAL E05: Sin volumen persistente para PostgreSQL
# ERROR INTENCIONAL E06: Sin health checks en servicios

services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - frontend
      - flutter-app
      - api-gateway

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - api-gateway

  flutter-app:
    build: ./flutter_app
    ports:
      - "3001:3001"
    depends_on:
      - api-gateway

  api-gateway:
    build: ./api-gateway
    ports:
      - "8000:8000"
    depends_on:
      - ms-hce
      - ms-facturacion
      - ms-mediciones

  ms-hce:
    build: ./ms-hce
    ports:
      - "8081:8081"
    environment:
      SPRING_PROFILES_ACTIVE: docker
    depends_on:
      - db
      - rabbitmq

  ms-facturacion:
    build: ./ms-facturacion
    ports:
      - "8082:8082"
    depends_on:
      - db-legacy
      - rabbitmq

  ms-mediciones:
    build: ./ms-mediciones
    ports:
      - "8001:8001"
    depends_on:
      - db
      - rabbitmq

  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "5672:5672"
      - "15672:15672"

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: medisalud_calidad
      POSTGRES_USER: medisalud
      POSTGRES_PASSWORD: medisalud_pass
    ports:
      - "5432:5432"
    volumes:
      - ./database/init.sql:/docker-entrypoint-initdb.d/01-init.sql
      - ./database/seed.sql:/docker-entrypoint-initdb.d/02-seed.sql
    # ERROR: Sin healthcheck

  db-legacy:
    image: mcr.microsoft.com/mssql/server:2022-latest
    environment:
      ACCEPT_EULA: "Y"
      MSSQL_SA_PASSWORD: "MediSalud2025!"
    ports:
      - "1433:1433"
    # ERROR: Sin volumen persistente, sin healthcheck

  pipeline-worker:
    build: ./pipeline-worker
    depends_on:
      - db
      - rabbitmq
    restart: unless-stopped
```

---

## 11. CI/CD — GitHub Actions

```yaml
# .github/workflows/ci.yml
# ERROR INTENCIONAL E36: Sin ejecución de tests
# ERROR INTENCIONAL E37: Sin linter
# ERROR INTENCIONAL E38: Sin análisis de seguridad

name: CI — MediSalud HIS

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Spring Boot (ms-hce)
        run: |
          cd ms-hce
          ./mvnw compile -q

      - name: Build FastAPI (ms-mediciones)
        run: |
          cd ms-mediciones
          pip install -r requirements.txt

      - name: Build React (frontend)
        run: |
          cd frontend
          npm ci
          npm run build

      - name: Build Flutter (flutter-app)
        run: |
          cd flutter_app
          flutter build web

      - name: Build Docker images
        run: |
          docker compose build
```

---

## 12. Archivos a Crear — Lista Maestra

| # | Ruta | Tecnología | Propósito | Errores intencionales |
|---|---|---|---|---|
| 1 | `database/init.sql` | SQL | Esquema PostgreSQL | E14, E19, E06 |
| 2 | `database/seed.sql` | SQL | Datos de referencia | — |
| 3 | `database/legacy/init.sql` | SQL Server | Esquema financiero legacy | E14 (fechas VARCHAR) |
| 4 | `rabbitmq/definitions.json` | RabbitMQ | Definiciones de exchanges/queues | — |
| 5 | `nginx/default.conf` | Nginx | Reverse proxy | E05 |
| 6 | `api-gateway/` | Spring Cloud Gateway | Enrutamiento | — |
| 7 | `ms-hce/` | Spring Boot + Java 17 | Simulador logs HCE | E11, E08 |
| 8 | `ms-facturacion/` | Spring Boot + Java 17 | Simulador facturación | E08 |
| 9 | `ms-mediciones/app/main.py` | FastAPI | API REST mediciones | E17, E22 |
| 10 | `ms-mediciones/app/routers/*.py` | FastAPI | Endpoints | E07, E08, E09, E10, E18 |
| 11 | `ms-mediciones/app/services/metric_calculator.py` | Python | Cálculo métricas | E07, E13 |
| 12 | `ms-mediciones/requirements.txt` | Python | Dependencias | — |
| 13 | `ms-mediciones/Dockerfile` | Docker | Imagen del servicio | — |
| 14 | `frontend/src/api/client.ts` | TypeScript | Cliente HTTP | E31, E24 |
| 15 | `frontend/src/pages/Dashboard.tsx` | TypeScript/React | Página principal | E25, E26 |
| 16 | `frontend/src/components/*.tsx` | TypeScript/React | Componentes UI | E29, E30, E32 |
| 17 | `frontend/tsconfig.json` | TypeScript | Configuración | E23 |
| 18 | `frontend/Dockerfile` | Docker | Imagen frontend | — |
| 19 | `flutter_app/` | Flutter/Dart | App móvil | E33, E34, E35 |
| 20 | `docker-compose.yml` | Docker | Orquestación | E05, E06 |
| 21 | `.github/workflows/ci.yml` | YAML | CI/CD | E36, E37, E38 |
| 22 | `pipeline-worker/` | Python | Worker de RabbitMQ | E07, E09 |

**Total: ~75 archivos nuevos** (incluyendo tests, configuraciones y código fuente)

---

## 13. Archivos que se Conservan

| Ruta | Razón |
|---|---|
| `docs/taller_iso_25022.md` | Documento base del taller |
| `docs/analisis_inicial.md` | Entregable del Escenario 1 |
| `docs/taller_iso_25022_parte1.pdf` | Anexo |
| `data/incidentes_2025.csv` | Fuente de datos original |
| `reportes/*.md` (9 archivos) | Entregables de escenarios |
| `scripts/*.py` (4 archivos) | Scripts originales del estudiante |
| `README.md` | Se actualizará |

---

## 14. Secuencia de Implementación

| Fase | Componentes | Archivos | Errores que introduce |
|---|---|---|---|
| **1** | PostgreSQL + SQL Server + RabbitMQ | `database/`, `rabbitmq/` | E14, E19, E06 |
| **2** | Spring Boot (ms-hce, ms-facturacion) | `ms-hce/`, `ms-facturacion/` | E08, E11 |
| **3** | FastAPI (ms-mediciones) | `ms-mediciones/` | E07, E08, E09, E10, E13, E17, E22 |
| **4** | Frontend React | `frontend/` | E23, E24, E25, E26, E29, E30, E31, E32 |
| **5** | Flutter app | `flutter_app/` | E33, E34, E35 |
| **6** | Docker Compose + Nginx | `docker-compose.yml`, `nginx/` | E05, E06 |
| **7** | API Gateway | `api-gateway/` | — |
| **8** | Pipeline worker + CI/CD | `pipeline-worker/`, `.github/` | E07, E36, E37, E38 |
| **9** | Seed data + docs | `scripts/seed_data.py`, README | — |
