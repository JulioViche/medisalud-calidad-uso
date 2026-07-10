# MediSalud HIS - Calidad en Uso ISO/IEC 25022

Laboratorio local para observar tareas de MediSalud HIS, reproducir fallos controlados y medir calidad en uso. La aplicación genera evidencia académica; no representa un sistema clínico productivo.

## Fuente de verdad

- El material principal está en `docs/Documento Padre`.
- `data/original/incidentes_2025.csv` contiene una copia de trabajo de los 3.000 incidentes originales.
- La copia y el archivo Padre comparten SHA-256 `814F3E5D8CF983A86BC125EC9C8461E3728C91DDCE1CFE8A5518ABD7A53CDC17`.
- Los incidentes cubren del 2 de enero al 19 de diciembre de 2025.
- Los eventos y encuestas adicionales son simulados para 2025 y declaran semilla y procedencia.
- Los reportes y scripts anteriores se conservaron bajo carpetas `legacy`; no son fuente académica.

## Componentes

| Área | Implementación |
|---|---|
| Portal hospitalario | React, TypeScript, Vite y Recharts |
| Aplicación del paciente | Flutter, Riverpod, GoRouter, Dio, Clean Architecture y Atomic Design |
| Entrada común | Spring Cloud Gateway |
| Servicios operativos | Spring Boot: HCE, citas y facturación |
| Medición | FastAPI y paquete Python `analytics` |
| Infraestructura | PostgreSQL, SQL Server y RabbitMQ |
| Informe | XeLaTeX, 12 escenarios y reto integrador |

El portal React abre en la jornada operativa del personal hospitalario: agenda, atención activa y pendientes. `Calidad y reportes` es un módulo secundario para Gerencia y Calidad. La arquitectura se documenta en `docs/arquitectura`, pero no aparece como una pantalla del HIS. Flutter corresponde exclusivamente al portal del paciente y no muestra indicadores ISO.

## Ejecución en Ubuntu WSL

Docker Engine y Compose se ejecutan dentro de la distribución `Ubuntu` de WSL 2.

```powershell
wsl -d Ubuntu
```

```bash
cd /mnt/c/Users/mesia/Desktop/Universidad/Calidad/3P/Taller/1/medisalud-calidad-uso
cp infrastructure/docker/.env.example infrastructure/docker/.env
bash scripts/setup/start-wsl.sh
```

URLs locales:

- Portal HIS: <http://localhost:5173>
- API Gateway: <http://localhost:8080>
- Documentación OpenAPI de medición: <http://localhost:8080/docs>
- RabbitMQ Management: <http://localhost:15672>

Para detener los contenedores sin eliminar datos:

```bash
bash scripts/setup/stop-wsl.sh
```

## Analítica reproducible

Desde la raíz en Windows o WSL:

```bash
python -m analytics.exporters.pipeline --seed 25022
python -m unittest discover -s analytics/tests -v
```

La ejecución crea 6.000 eventos, 2.000 encuestas, la clasificación de 3.000 incidentes y diez métricas. `data/simulated` y `data/processed` son regenerables; los resúmenes seleccionados se conservan en `evidencias/resultados`.

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

## Informe

```powershell
powershell -ExecutionPolicy Bypass -File scripts/reports/build-report.ps1
```

El PDF final se encuentra en [informe/entrega/medisalud_iso25022.pdf](informe/entrega/medisalud_iso25022.pdf). Los escenarios 1-3 siguen literalmente la copia recibida; los escenarios 4-12 y el reto están identificados como reconstruidos porque el Documento Padre parcial solo incluye sus títulos.

## Pruebas

```powershell
python -m unittest discover -s analytics/tests -v
python -m unittest discover -s tests/integration -v
cd apps/web-his
npm test
npm run build
```

El portal, las APIs, la persistencia y los escenarios intencionales se validan con el stack activo. Los fallos simulados se activan mediante campos `scenario`; no se introducen vulnerabilidades reales ni defectos accidentales.

## Datos versionados

- Se versionan el dataset original, contratos, código, migraciones, evidencia seleccionada y PDF final.
- Se ignoran secretos, builds, cachés, volúmenes y datos regenerables.
- `infrastructure/docker/.env` es local; su plantilla versionada es `.env.example`.
