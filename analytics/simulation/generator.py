from __future__ import annotations

import argparse
import random
from datetime import datetime, timedelta
from pathlib import Path

from analytics.common.io import write_csv, write_json


SITES = ("Quito", "Guayaquil", "Cuenca", "Ambato", "Manta")
ROLES = ("Medico", "Enfermeria", "Admision", "Paciente", "Farmacia")
EVENT_TYPES = (
    "hce_save", "appointment", "billing", "prescription", "imaging", "teleconsultation",
)


class SimulationGenerator:
    def __init__(self, seed: int = 25022) -> None:
        self.seed = seed
        self.random = random.Random(seed)

    def generate(self, count: int = 6000) -> list[dict[str, object]]:
        start = datetime(2025, 1, 1, 7)
        events: list[dict[str, object]] = []
        for index in range(count):
            event_type = self.random.choices(EVENT_TYPES, weights=(32, 22, 14, 12, 8, 12), k=1)[0]
            occurred_at = start + timedelta(
                days=self.random.randrange(365),
                hours=self.random.randrange(12),
                minutes=self.random.randrange(60),
            )
            site = self.random.choices(SITES, weights=(32, 25, 17, 14, 12), k=1)[0]
            role = self._role_for(event_type)
            payload = self._event_result(event_type, occurred_at.hour, site)
            events.append(
                {
                    "event_id": f"EVT-{index + 1:06d}",
                    "occurred_at": occurred_at.isoformat(),
                    "site": site,
                    "role": role,
                    "module": payload["module"],
                    "event_type": event_type,
                    "duration_seconds": payload["duration_seconds"],
                    "successful": payload["successful"],
                    "error_code": payload["error_code"],
                    "iso_characteristic": payload["iso_characteristic"],
                    "seed": self.seed,
                    "simulated": True,
                }
            )
        return events

    def surveys(self, count: int = 2000) -> list[dict[str, object]]:
        surveys: list[dict[str, object]] = []
        for index in range(count):
            site = self.random.choices(SITES, weights=(32, 25, 17, 14, 12), k=1)[0]
            score_penalty = 1 if site == "Manta" else 0
            csat = max(1, min(5, round(self.random.gauss(3.5 - score_penalty * 0.4, 1))))
            nps = max(0, min(10, round(self.random.gauss(6.4 - score_penalty, 2.2))))
            surveys.append(
                {
                    "survey_id": f"SUR-{index + 1:05d}",
                    "date": f"2025-{self.random.randrange(1, 13):02d}-{self.random.randrange(1, 29):02d}",
                    "site": site,
                    "role": self.random.choice(ROLES),
                    "csat": csat,
                    "nps": nps,
                    "completed": self.random.random() > 0.09,
                    "seed": self.seed,
                    "simulated": True,
                }
            )
        return surveys

    def _role_for(self, event_type: str) -> str:
        return {
            "hce_save": "Medico",
            "appointment": "Paciente",
            "billing": "Admision",
            "prescription": "Medico",
            "imaging": "Medico",
            "teleconsultation": "Paciente",
        }[event_type]

    def _event_result(self, event_type: str, hour: int, site: str) -> dict[str, object]:
        peak = 10 <= hour <= 12
        slow_site = site == "Manta"
        base = {
            "hce_save": ("HCE", 5.8, 0.08, "Eficiencia", "SIM-HCE-SLOW"),
            "appointment": ("Portal Citas", 3.0, 0.12, "Efectividad", "SIM-CITA-FAIL"),
            "billing": ("Facturacion", 2.2, 0.035, "Libertad de Riesgo", "SIM-BILL-DUP"),
            "prescription": ("Farmacia", 2.8, 0.025, "Libertad de Riesgo", "SIM-RX-DOSE"),
            "imaging": ("Imagenologia", 7.0, 0.14, "Eficiencia", "SIM-IMG-SLOW"),
            "teleconsultation": ("Telemedicina", 240.0, 0.09, "Cobertura de Contexto", "SIM-VIDEO-DROP"),
        }[event_type]
        module, mean_duration, failure_rate, characteristic, error_code = base
        duration_factor = (1.9 if peak and event_type == "hce_save" else 1.0) * (1.25 if slow_site else 1.0)
        duration = max(0.2, self.random.gauss(mean_duration * duration_factor, mean_duration * 0.25))
        failed = self.random.random() < failure_rate * (1.25 if slow_site else 1.0)
        if event_type == "hce_save" and duration > 20:
            failed = True
        return {
            "module": module,
            "duration_seconds": round(duration, 2),
            "successful": not failed,
            "error_code": error_code if failed else "",
            "iso_characteristic": characteristic,
        }


def generate_files(output_dir: Path, seed: int, count: int) -> None:
    generator = SimulationGenerator(seed)
    events = generator.generate(count)
    surveys = generator.surveys()
    write_csv(output_dir / "events.csv", events, list(events[0]))
    write_csv(output_dir / "surveys.csv", surveys, list(surveys[0]))
    write_json(
        output_dir / "manifest.json",
        {"seed": seed, "period": "2025-01-01/2025-12-31", "events": len(events), "surveys": len(surveys)},
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera evidencia simulada de MediSalud")
    parser.add_argument("--seed", type=int, default=25022)
    parser.add_argument("--count", type=int, default=6000)
    parser.add_argument("--output", type=Path, default=Path("data/simulated"))
    args = parser.parse_args()
    generate_files(args.output, args.seed, args.count)


if __name__ == "__main__":
    main()

