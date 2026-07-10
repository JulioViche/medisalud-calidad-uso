import unittest

from apps.analytics.classification.classifier import IncidentClassifier, _activity_justification
from apps.analytics.metrics.calculator import percentile
from apps.analytics.simulation.generator import SimulationGenerator


class ClassificationTests(unittest.TestCase):
    def test_risk_has_precedence_over_functional_failure(self) -> None:
        result = IncidentClassifier().classify("Historial de alergias no carga")
        self.assertEqual("Libertad de Riesgo", result.characteristic)

    def test_activity_justification_is_incident_specific(self) -> None:
        description = "Nota de evolucion tarda 22s en guardarse"
        justification = _activity_justification(description, "Eficiencia")
        self.assertIn(description, justification)
        self.assertIn("mas tiempo", justification)

    def test_efficiency_is_detected(self) -> None:
        result = IncidentClassifier().classify("Nota de evolucion tarda 22s")
        self.assertEqual("Eficiencia", result.characteristic)


class SimulationTests(unittest.TestCase):
    def test_seed_is_reproducible(self) -> None:
        first = SimulationGenerator(42).generate(10)
        second = SimulationGenerator(42).generate(10)
        self.assertEqual(first, second)

    def test_percentile(self) -> None:
        self.assertEqual(9, percentile(list(range(1, 11)), 0.9))


if __name__ == "__main__":
    unittest.main()
