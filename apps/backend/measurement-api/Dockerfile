FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MEDISALUD_ROOT=/workspace \
    PYTHONPATH=/workspace

WORKDIR /workspace
COPY apps/backend/measurement-api/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY apps/__init__.py apps/__init__.py
COPY apps/analytics apps/analytics
COPY apps/backend/measurement-api/app apps/backend/measurement-api/app
COPY apps/data/original apps/data/original
COPY apps/data/processed apps/data/processed
COPY apps/data/simulated apps/data/simulated
COPY reportes/evidencias reportes/evidencias

WORKDIR /workspace/apps/backend/measurement-api
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
