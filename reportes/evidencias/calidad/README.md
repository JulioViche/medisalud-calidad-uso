# Evidencia de calidad interna y externa

- `sonarqube/metricas.json`: respuesta de la API de SonarQube para `billing-service`.
- `jmeter/resumen.json`: resumen derivado de 500 solicitudes concurrentes al portal de citas.
- `jmeter/raw/`: resultados JTL y log regenerables; no se versionan.

Ejecución desde Ubuntu WSL:

```bash
bash scripts/quality/run-sonar-wsl.sh
bash scripts/quality/run-jmeter-wsl.sh
```

SonarQube se publica localmente en `http://localhost:9000`. Los tokens se generan para cada ejecución, se revocan al finalizar y no se guardan en el repositorio.
