# Evidencia de ejecución real de pruebas

## Identificación

- Proyecto: MediSalud HIS — taller ISO/IEC 25022, parte 2.
- Fecha local: 13 de julio de 2026, 21:15–22:07 (UTC-05:00, America/Guayaquil).
- Revisión probada: `3baf75d`, rama `main`, más los cambios de documentación en curso.
- Entorno: Windows 11, WSL Ubuntu, Python 3.14.3, Node.js 24.14.0, npm 11.9.0, Docker Server 29.4.3 y Docker Compose 5.1.3.
- Flutter usado para la verificación: 3.44.6, Dart 3.12.2. Se instaló en paralelo porque el SDK 3.41.7/Dart 3.11.5 disponible inicialmente no satisfacía `sdk: ^3.12.2`; no se modificó el SDK anterior.

## Matriz de resultados

| Componente | Comando ejecutado | Resultado comprobado |
|---|---|---|
| Pipeline de medición | `python -m apps.analytics.exporters.pipeline --seed 25022` | Aprobado; generó 10 métricas con semilla 25022. |
| Analítica Python | `python -m unittest discover -s apps/analytics/tests -v` | 5/5 aprobadas; 0 fallos y 0 errores. |
| API de medición | `python -m unittest discover -s apps/backend/measurement-api/tests -v` | 1/1 aprobada; 0 fallos y 0 errores; 0,409 s. |
| Dominio HCE Java | `docker run --rm ... maven:3.9.9-eclipse-temurin-21 mvn -B test` | 1/1 aprobada; `ClinicalNoteTest`; 0 fallos, 0 errores y 0 omitidas; `BUILD SUCCESS`. |
| Portal React | `npm test -- --reporter=verbose` | 8/8 aprobadas en 2 archivos; autenticación, autorización por rol, sesión y `StatusBadge`. |
| Compilación React | `npm run build` | Aprobada; 2.345 módulos transformados y artefactos Vite generados. Se conserva una advertencia no bloqueante por un fragmento JS mayor de 500 kB. |
| Integración completa | `MEDISALUD_BASE_URL=http://localhost:18080 python -m unittest discover -s apps/tests/integration -v` | 3/3 aprobadas en 1,302 s contra servicios y bases reales en Docker. |
| Flutter estático | `flutter analyze` | Aprobado; `No issues found`, 46,1 s. |
| Flutter widget | `flutter test` | 1/1 aprobada; `AppBadge displays its label`. |
| Compilación Flutter | `flutter build web --no-wasm-dry-run` | Aprobada; artefacto `build/web` generado en 55,6 s de compilación. |
| Carga JMeter | `docker compose ... --profile quality run --rm jmeter` | 500/500 solicitudes correctas, 0 errores, media 1.875,7 ms, P90 2.487 ms y P95 2.510 ms. |

En total se ejecutaron **19 casos automatizados y los 19 aprobaron**: 5 de analítica, 1 de API, 1 de dominio Java, 8 de React, 3 de integración y 1 de Flutter. Los análisis y compilaciones se informan por separado porque no son casos de prueba unitarios.

## Verificación de integración

La pila se levantó con PostgreSQL, SQL Server, RabbitMQ, API de medición, servicios de citas, HCE y facturación, y API Gateway. Todos alcanzaron estado `healthy`. Como los puertos 8080 y 15672 estaban ocupados por contenedores ajenos al proyecto, se aplicó `apps/infrastructure/docker/compose.test.override.yaml`: el Gateway se publicó en 18080 y RabbitMQ no expuso su consola al host. No se detuvieron ni alteraron los otros proyectos.

Los tres casos comprobaron:

1. salud del Gateway, tablero con 3.000 incidentes y 10 métricas, y consulta paginada de incidentes;
2. reproducibilidad de una simulación de 250 eventos con semilla 25022;
3. fallas controladas de disponibilidad de citas, lentitud de HCE y duplicación de facturación.

## Evidencia de rendimiento

La corrida JMeter inició el 14 de julio de 2026 a las 02:57:16 UTC, equivalente al 13 de julio a las 21:57:16 en Ecuador. Los 500 usuarios sincronizados consultaron citas a través del Gateway. El archivo fuente de resultados es `reportes/evidencias/calidad/jmeter/raw/citas-500-usuarios.jtl` y el resumen regenerado es `reportes/evidencias/calidad/jmeter/resumen.json`.

## Incidencias del entorno y resolución

- El primer `flutter pub get` no podía ejecutarse con Dart 3.11.5. Se preservó el SDK existente y se instaló Flutter 3.44.6/Dart 3.12.2 en paralelo; después se repitieron y aprobaron dependencia, análisis, prueba y compilación.
- Docker requirió descargar la imagen de SQL Server y construir `billing-service` y JMeter. Las imágenes terminaron correctamente.
- Las colisiones de puertos con otro proyecto se aislaron mediante el archivo de sobreescritura de pruebas; no se emplearon resultados de ese otro sistema.

## Conclusión de la ejecución

La automatización evaluada es ejecutable y reproducible en el entorno documentado. No se registraron fallos en los 19 casos. La advertencia de tamaño del paquete React y las versiones más recientes de algunos paquetes Flutter son observaciones de mantenimiento, no fallos de esta corrida.
