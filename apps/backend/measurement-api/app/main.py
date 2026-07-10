from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI

from .api.routes import router
from .application.service import MeasurementService


ROOT = Path(os.getenv("MEDISALUD_ROOT", Path(__file__).resolve().parents[3]))
measurement_service = MeasurementService(ROOT)
measurement_service.ensure_data()

app = FastAPI(
    title="MediSalud Measurement API",
    version="1.0.0",
    description="Academic ISO/IEC 25022 measurement and simulation API.",
)
app.include_router(router)
