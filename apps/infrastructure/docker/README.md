# Ejecucion local en Ubuntu WSL

```powershell
wsl -d Ubuntu
```

```bash
cd /mnt/c/Users/mesia/Desktop/Universidad/Calidad/3P/Taller/1/medisalud-calidad-uso
cp apps/infrastructure/docker/.env.example apps/infrastructure/docker/.env
bash scripts/setup/start-wsl.sh
```

Servicios publicados:

- Portal web: <http://localhost:5173>
- Gateway: <http://localhost:8080>
- RabbitMQ: <http://localhost:15672>

## Perfil de calidad

El perfil opcional `quality` añade SonarQube, su PostgreSQL, el escáner Maven para facturación y JMeter. SonarQube se publica solamente en <http://localhost:9000>; JMeter se ejecuta como contenedor efímero mediante los scripts de `scripts/quality`.
