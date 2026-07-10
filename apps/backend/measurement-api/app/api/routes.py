from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, status

from ..application.service import MeasurementService
from ..domain.models import PatientSurvey, SimulationRequest, TeleconsultationRequest


router = APIRouter()


def service() -> MeasurementService:
    from ..main import measurement_service

    return measurement_service


@router.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "UP", "service": "measurement-api"}


@router.get("/api/incidentes")
def incidents(
    site: str | None = None,
    module: str | None = None,
    role: str | None = None,
    characteristic: str | None = None,
    limit: int = Query(default=50, ge=1, le=500),
    offset: int = Query(default=0, ge=0),
    use_case: MeasurementService = Depends(service),
) -> dict[str, object]:
    return use_case.incidents(site, module, role, characteristic, limit, offset)


@router.get("/api/metricas")
def metrics(use_case: MeasurementService = Depends(service)) -> list[dict[str, str]]:
    return use_case.metrics()


@router.get("/api/dashboard/resumen")
def dashboard(use_case: MeasurementService = Depends(service)) -> dict[str, object]:
    return use_case.dashboard()


@router.post("/api/simulaciones", status_code=status.HTTP_201_CREATED)
def run_simulation(request: SimulationRequest, use_case: MeasurementService = Depends(service)) -> dict[str, object]:
    return use_case.run_simulation(request.seed, request.event_count)


@router.get("/api/simulaciones/{simulation_id}")
def simulation(simulation_id: str, use_case: MeasurementService = Depends(service)) -> dict[str, object]:
    result = use_case.simulation(simulation_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Simulation not found")
    return result


@router.post("/api/paciente/teleconsultas", status_code=status.HTTP_201_CREATED)
def teleconsultation(request: TeleconsultationRequest) -> dict[str, object]:
    return {
        "session_id": f"TEL-{request.patient_id}",
        "status": "interrupted" if request.simulate_drop else "scheduled",
        "site": request.site,
        "simulated": True,
        "error_code": "SIM-VIDEO-DROP" if request.simulate_drop else None,
    }


@router.post("/api/paciente/encuestas", status_code=status.HTTP_201_CREATED)
def survey(request: PatientSurvey, use_case: MeasurementService = Depends(service)) -> dict[str, object]:
    return use_case.register_survey(request.model_dump())

