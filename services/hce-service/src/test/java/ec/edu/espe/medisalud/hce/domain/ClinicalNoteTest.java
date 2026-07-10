package ec.edu.espe.medisalud.hce.domain;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class ClinicalNoteTest {
    @Test void preservesScenario() {
        var note = new ClinicalNote("P1", "M1", "Quito", "Control", "slow");
        assertEquals("slow", note.scenario());
    }
}

