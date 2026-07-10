FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MEDISALUD_ROOT=/workspace \
    PYTHONPATH=/workspace

WORKDIR /workspace
COPY services/measurement-api/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY analytics analytics
COPY services/measurement-api/app services/measurement-api/app
COPY data/original data/original
COPY data/catalogs data/catalogs
COPY data/processed data/processed
COPY data/simulated data/simulated
COPY evidencias evidencias

WORKDIR /workspace/services/measurement-api
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
