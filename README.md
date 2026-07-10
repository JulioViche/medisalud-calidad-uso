# MediSalud HIS - Calidad en Uso ISO/IEC 25022

Laboratorio local para observar tareas de MediSalud HIS, reproducir fallos controlados y medir calidad en uso. La aplicación genera evidencia académica; no representa un sistema clínico productivo.

## Datos del estudio

- El archivo solicitado por el taller es `data/incidentes_2025.csv`; contiene los seis casos literales y una ampliación hasta 3.000 registros.
- La clasificación solicitada en la Tabla 2.2 se entrega en `data/clasificacion/incidentes_clasificados.csv`, con 3.000 IDs únicos, justificación técnica individual y característica principal. Incluye los casos de referencia `1001–1006`.
- La copia preservada de los 3.000 incidentes suministrados se conserva en `apps/data/original/incidentes_2025.csv` para la recreación y el análisis automatizado.
- Los incidentes cubren del 2 de enero al 19 de diciembre de 2025.
- Los eventos y encuestas adicionales son simulados para 2025 y declaran semilla y procedencia.

## Componentes

| Área | Implementación |
|---|---|
| Portal hospitalario | React, TypeScript, Vite y Recharts |
| Aplicación del paciente | Flutter, Riverpod, GoRouter, Dio, Clean Architecture y Atomic Design |
| Entrada común | Spring Cloud Gateway |
| Servicios operativos | Spring Boot: HCE, citas y facturación |
| Medición | FastAPI y paquete Python `apps.analytics` |
| Infraestructura | PostgreSQL, SQL Server y RabbitMQ |
| Informe | XeLaTeX, 12 escenarios y reto integrador |
| Calidad interna y externa | SonarQube Community Build y Apache JMeter 5.6.3 |

La raíz conserva las cinco carpetas indicadas por el taller: `data`, `scripts`, `dashboards`, `docs` y `reportes`. La recreación funcional se agrupa en `apps`, separada por aplicación, backend, analítica, contratos, infraestructura y pruebas.

El portal React abre en la jornada operativa del personal hospitalario: agenda, atención activa y pendientes. `Calidad y reportes` es un módulo secundario para Gerencia y Calidad. La arquitectura técnica se conserva en el código y en la configuración de `apps/infrastructure`; no aparece como una pantalla del HIS. Flutter corresponde exclusivamente al portal del paciente y no muestra indicadores ISO.

## Ejecución en Ubuntu WSL

Docker Engine y Compose se ejecutan dentro de la distribución `Ubuntu` de WSL 2.

```powershell
wsl -d Ubuntu
```

```bash
cd /mnt/c/Users/mesia/Desktop/Universidad/Calidad/3P/Taller/1/medisalud-calidad-uso
cp apps/infrastructure/docker/.env.example apps/infrastructure/docker/.env
bash scripts/setup/start-wsl.sh
```

URLs locales:

- Portal HIS: <http://localhost:5173>
- API Gateway: <http://localhost:8080>
- Documentación OpenAPI de medición: <http://localhost:8080/docs>
- RabbitMQ Management: <http://localhost:15672>
- SonarQube local: <http://localhost:9000> (perfil `quality`)

Para detener los contenedores sin eliminar datos:

```bash
bash scripts/setup/stop-wsl.sh
```

## Analítica reproducible

Desde la raíz en Windows o WSL:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m apps.analytics.exporters.pipeline --seed 25022
python -m unittest discover -s apps/analytics/tests -v
```

La ejecución crea 6.000 eventos, 2.000 encuestas, la clasificación de 3.000 incidentes y diez métricas. `apps/data/simulated` y `apps/data/processed` son regenerables; los resúmenes seleccionados se conservan en `reportes/evidencias/resultados`.

## Flutter

Abrir `apps/mobile-patient` desde Android Studio. Para web:

```powershell
cd apps/mobile-patient
flutter pub get
flutter analyze
flutter build web --no-wasm-dry-run
flutter run -d chrome --dart-define=API_URL=http://localhost:8080
```

En el emulador Android la URL predeterminada es `http://10.0.2.2:8080`. Antes de ejecutar Android deben instalarse los `cmdline-tools` y aceptarse las licencias del SDK indicadas por `flutter doctor`.

## Dashboard académico

El [dashboard de Calidad en Uso](dashboards/index.html) se abre directamente en
el navegador y no requiere iniciar el HIS ni Docker. Incluye resumen ejecutivo,
análisis filtrable de los 3.000 incidentes y trazabilidad de fórmulas y fuentes.

Para regenerar sus datos desde los CSV versionados:

```powershell
python scripts/reports/generate-dashboard-data.py
```

## Informe

```powershell
powershell -ExecutionPolicy Bypass -File scripts/reports/build-report.ps1
```

El PDF final se encuentra en [reportes/entrega/medisalud_iso25022.pdf](reportes/entrega/medisalud_iso25022.pdf). Los escenarios 1-3 se basan en el material recibido del docente; los escenarios 4-12 y el reto integrador fueron reconstruidos por el equipo a partir de los títulos provistos.

El mapa conceptual SQuaRE puede revisarse directamente en `reportes/mapa-conceptual/` o en `docs/mapa-conceptual/`, disponible como PNG y PDF vectorial.

## Pruebas

```powershell
python -m unittest discover -s apps/analytics/tests -v
python -m unittest discover -s apps/tests/integration -v
cd apps/web-his
npm test
npm run build
```

El portal, las APIs, la persistencia y los escenarios intencionales se validan con el stack activo. Los fallos simulados se activan mediante campos `scenario`; no se introducen vulnerabilidades reales ni defectos accidentales.

## Calidad interna y externa

Desde Ubuntu WSL, con Docker activo:

```bash
bash scripts/quality/run-sonar-wsl.sh
bash scripts/quality/run-jmeter-wsl.sh
```

SonarQube analiza `billing-service`; JMeter ejecuta 500 usuarios sincronizados contra el portal de citas. Los resúmenes versionados están en `reportes/evidencias/calidad`. El token de SonarQube se genera para la ejecución, se revoca al finalizar y nunca se escribe en el repositorio.

## Datos versionados

- Se versionan el dataset original, contratos, código, migraciones, evidencia seleccionada y PDF final.
- Se ignoran secretos, builds, cachés, volúmenes y datos regenerables.
- `apps/infrastructure/docker/.env` es local; su plantilla versionada es `.env.example`.
