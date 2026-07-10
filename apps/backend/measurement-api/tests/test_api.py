import os
import unittest
from pathlib import Path
import sys

from fastapi.testclient import TestClient


class ApiSmokeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.environ.setdefault("MEDISALUD_ROOT", str(Path.cwd()))
        sys.path.insert(0, str(Path.cwd() / "apps/backend/measurement-api"))
        from app.main import app

        cls.client = TestClient(app)

    def test_health(self) -> None:
        response = self.client.get("/api/health")
        self.assertEqual(200, response.status_code)
        self.assertEqual("UP", response.json()["status"])
