from __future__ import annotations

from pydantic import BaseModel, Field


class SimulationRequest(BaseModel):
    seed: int = Field(default=25022, ge=1, le=999999)
    event_count: int = Field(default=6000, ge=100, le=50000)


class PatientSurvey(BaseModel):
    site: str
    csat: int = Field(ge=1, le=5)
    nps: int = Field(ge=0, le=10)
    comments: str = Field(default="", max_length=500)


class TeleconsultationRequest(BaseModel):
    patient_id: str
    site: str
    symptoms: str = Field(min_length=3, max_length=1000)
    simulate_drop: bool = False

