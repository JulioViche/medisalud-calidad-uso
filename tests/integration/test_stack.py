from __future__ import annotations

import json
import time
import unittest
import urllib.error
import urllib.request


BASE_URL = "http://localhost:8080"


def request(path: str, method: str = "GET", payload: dict[str, object] | None = None) -> object:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        BASE_URL + path,
        data=data,
        method=method,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read())


class StackIntegrationTests(unittest.TestCase):
    def test_health_dashboard_and_incidents(self) -> None:
        self.assertEqual("UP", request("/api/health")["status"])
        dashboard = request("/api/dashboard/resumen")
        self.assertEqual(3000, dashboard["incident_count"])
        self.assertEqual(10, len(dashboard["metrics"]))
        self.assertEqual(2, len(request("/api/incidentes?limit=2")["items"]))

    def test_reproducible_simulation(self) -> None:
        payload = {"seed": 25022, "event_count": 250}
        first = request("/api/simulaciones", "POST", payload)
        second = request("/api/simulaciones", "POST", payload)
        self.assertEqual(first["simulation_id"], second["simulation_id"])

    def test_controlled_failures(self) -> None:
        failed_appointment = request(
            "/api/paciente/citas",
            "POST",
            {"patientId": "PAC-TEST", "site": "Manta", "specialty": "Medicina general", "date": "2025-12-20 11:00", "scenario": "availability_failure"},
        )
        self.assertFalse(failed_appointment["successful"])

        slow_note = request(
            "/api/hce/notas",
            "POST",
            {"patientId": "PAC-TEST", "doctorId": "MED-TEST", "site": "Quito", "text": "Control", "scenario": "slow"},
        )
        self.assertGreater(slow_note["durationSeconds"], 8)

        transaction_id = f"TEST-{time.time_ns()}"
        duplicate = request(
            "/api/facturacion",
            "POST",
            {"transactionId": transaction_id, "patientId": "PAC-TEST", "amount": 10.5, "site": "Quito", "scenario": "duplicate"},
        )
        self.assertTrue(duplicate["duplicate"])


if __name__ == "__main__":
    unittest.main()

