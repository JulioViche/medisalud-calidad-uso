package ec.edu.espe.medisalud.hce.application;

import ec.edu.espe.medisalud.hce.domain.ClinicalNote;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

@Service
public class ClinicalRecordService {
    private final JdbcTemplate jdbc;
    private final RabbitTemplate rabbit;

    public ClinicalRecordService(JdbcTemplate jdbc, RabbitTemplate rabbit) {
        this.jdbc = jdbc;
        this.rabbit = rabbit;
    }

    public Map<String, Object> save(ClinicalNote note) {
        String scenario = note.scenario() == null ? "normal" : note.scenario();
        double duration = switch (scenario) { case "slow" -> 12.4; case "peak" -> 18.8; default -> 4.6; };
        boolean successful = !"save_failure".equals(scenario);
        String noteId = "NOTE-" + UUID.randomUUID().toString().substring(0, 8);
        if (successful) {
            jdbc.update("insert into clinical_notes(note_id, patient_id, doctor_id, site, note_text, created_at) values (?,?,?,?,?,?)",
                noteId, note.patientId(), note.doctorId(), note.site(), note.text(), OffsetDateTime.now(ZoneOffset.UTC));
            rabbit.convertAndSend("medisalud.events", "{\"type\":\"hce.note.saved\",\"noteId\":\"" + noteId + "\"}");
        }
        return Map.of(
            "noteId", noteId, "successful", successful, "durationSeconds", duration,
            "scenario", scenario, "errorCode", successful ? "" : "SIM-HCE-SAVE-FAIL", "simulated", true
        );
    }

    public List<Map<String, Object>> results(String patientId) {
        return List.of(
            Map.of("id", "LAB-2025-104", "patientId", patientId, "type", "Laboratorio", "name", "Hemograma completo", "status", "Disponible", "date", "2025-11-18"),
            Map.of("id", "IMG-2025-081", "patientId", patientId, "type", "Imagenologia", "name", "Radiografia de torax", "status", "Disponible", "date", "2025-11-12")
        );
    }
}
