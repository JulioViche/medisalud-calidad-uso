# Ejecucion local en Ubuntu WSL

```powershell
wsl -d Ubuntu
```

```bash
cd /mnt/c/Users/mesia/Desktop/Universidad/Calidad/3P/Taller/1/medisalud-calidad-uso
cp infrastructure/docker/.env.example infrastructure/docker/.env
bash scripts/setup/start-wsl.sh
```

Servicios publicados:

- Portal web: <http://localhost:5173>
- Gateway: <http://localhost:8080>
- RabbitMQ: <http://localhost:15672>

