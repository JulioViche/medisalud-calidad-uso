# Plan de Corrección — Proyecto ISO/IEC 25022

**Proyecto:** MediSalud HIS — Taller de Calidad en Uso
**Documento base:** `docs/taller_iso_25022.md`
**Propósito:** Alinear el repositorio actual con lo establecido en el taller guiado, preservando los errores intencionales de código como parte de la práctica pedagógica.

---

## 1. Directorio `dashboards/` — faltante

**Problema:** El documento (Escenario 1, Paso 1) indica `mkdir -p data scripts dashboards docs reportes`. El directorio `dashboards/` no fue creado.

**Acción:**

```bash
mkdir -p dashboards
```

**Archivo a modificar:** `.gitignore`

**Cambio:** Reemplazar la línea `dashboards/dashboard_calidad_uso.html` por:

```
dashboards/*.html
```

**Justificación:** El directorio debe existir antes de ejecutar `generar_dashboard.py`. El `.gitignore` se ajusta para ignorar cualquier HTML generado en el directorio, no solo un archivo específico.

---

## 2. `requirements.txt` — archivo ausente

**Problema:** El documento lista las dependencias en Escenario 1, Paso 2 pero no existe un archivo que las capture para instalación reproducible.

**Acción:** Crear `requirements.txt` con el siguiente contenido:

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
plotly>=5.15.0
openpyxl>=3.1.0
jupyter>=1.0.0
```

**Justificación:** El documento indica `pip install pandas numpy matplotlib plotly jupyter openpyxl`. Tener un `requirements.txt` permite `pip install -r requirements.txt` y asegura reproducibilidad.

---

## 3. `README.md` — ajustes de documentación

### 3.1 Rutas de re-ejecución incorrectas para Linux

**Problema:** Las rutas usan `venv\Scripts\python` (formato Windows), que no funciona en Linux/macOS.

**Sección afectada:** "Cómo re-ejecutar"

**Cambio:**

| Actual | Nueva |
|---|---|
| `venv\Scripts\python scripts\pipeline_medicion.py` | `python scripts/pipeline_medicion.py` |
| `venv\Scripts\python scripts\generar_dashboard.py` | `python scripts/generar_dashboard.py` |

**Justificación:** Con el `venv` activado (`source venv/bin/activate`), el comando `python` resuelve al intérprete del entorno virtual.

### 3.2 Semáforo hardcodeado

**Problema:** La línea `**Semáforo general:** 🟢 2 VERDE · 🟡 6 AMARILLO · 🔴 1 ROJO` está hardcodeada. Estos valores solo son válidos después de ejecutar el pipeline con una semilla específica.

**Cambio:** Reemplazar por:

```
**Semáforo general:** *(ejecutar `python scripts/pipeline_medicion.py` para ver resultados)*
```

### 3.3 Falta sección de instalación

**Problema:** No hay instrucciones para crear el entorno virtual e instalar dependencias.

**Cambio:** Agregar bloque antes de "Cómo re-ejecutar":

```bash
python3 -m venv venv
source venv/bin/activate           # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3.4 Agregar orden de ejecución

**Problema:** No se documenta el orden secuencial de los scripts (hay dependencias entre ellos).

**Cambio:** Agregar tabla:

| Orden | Script | Genera |
|---|---|---|
| 1 | `python scripts/generar_datos_simulados.py` | `data/logs_hce.csv`, `data/encuestas_satisfaccion.csv` |
| 2 | `python scripts/clasificar_incidentes.py` | `data/incidentes_clasificados.csv` |
| 3 | `python scripts/pipeline_medicion.py` | `data/resultados_metricas.csv` |
| 4 | `python scripts/generar_dashboard.py` | `dashboards/dashboard_calidad_uso.html` |

---

## 4. Scripts Python — sin cambios (errores intencionales preservados)

Los siguientes "defectos" identificados en el código se **dejan intactos** porque forman parte de la práctica pedagógica del taller:

| Script | Defecto | Propósito pedagógico |
|---|---|---|
| `generar_datos_simulados.py` | Variable `horarios` definida pero no usada (línea 13) | El estudiante debe identificar y eliminar código muerto |
| `clasificar_incidentes.py` | Sin `if __name__ == "__main__"` | El estudiante debe agregar el guard de ejecución |
| `pipeline_medicion.py` | `import json` no usado (línea 14) | Ídem — código muerto |
| `generar_dashboard.py` | `import plotly.express as px`, `from plotly.subplots import make_subplots`, `import json` no usados | Ídem |
| `generar_dashboard.py` | `import plotly.io as pio` en línea 182 (mitad del archivo) | El estudiante debe moverlo al inicio |

---

## 5. Archivos sin modificar

- `data/incidentes_2025.csv` — dataset de 3.000+ incidentes, correcto
- `docs/taller_iso_25022.md` — documento base, no se modifica
- `docs/analisis_inicial.md` — matriz de análisis completada, correcta
- `docs/taller_iso_25022_parte1.pdf` — anexo PDF, no se modifica
- `reportes/*.md` — 9 reportes de escenarios 2–12 + reto final, correctos

---

## 6. Secuencia de implementación

| Paso | Acción | Archivos afectados |
|---|---|---|
| 1 | Crear directorio `dashboards/` | — |
| 2 | Actualizar `.gitignore` | `.gitignore` |
| 3 | Crear `requirements.txt` | `requirements.txt` |
| 4 | Corregir rutas en README | `README.md` |
| 5 | Reemplazar semáforo hardcodeado | `README.md` |
| 6 | Agregar sección de instalación | `README.md` |
| 7 | Agregar orden de ejecución | `README.md` |
