# Arquitectura local

```text
Flutter / React
       |
Spring Cloud Gateway :8080
       |
       +-- HCE :8081 ---------- PostgreSQL -- RabbitMQ
       +-- Citas :8082 -------- PostgreSQL
       +-- Facturación :8083 -- SQL Server
       +-- Medición :8000 ----- CSV/JSON reproducibles
```

Los puertos internos no se publican. El Gateway es el único punto de entrada de aplicaciones. React se publica en `5173` y Flutter se ejecuta desde Windows o Android Studio.

Los servicios Spring aplican puertos y adaptadores; FastAPI separa dominio, aplicación y HTTP; Flutter separa `domain`, `data` y `presentation` y utiliza Atomic Design dentro de presentación.

