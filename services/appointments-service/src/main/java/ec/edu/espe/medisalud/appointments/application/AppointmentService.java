package ec.edu.espe.medisalud.appointments.application;

import ec.edu.espe.medisalud.appointments.domain.AppointmentRequest;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

@Service
public class AppointmentService {
    private final JdbcTemplate jdbc;
    public AppointmentService(JdbcTemplate jdbc) { this.jdbc = jdbc; }

    public Map<String, Object> create(AppointmentRequest request) {
        String scenario = request.scenario() == null ? "normal" : request.scenario();
        boolean successful = !"availability_failure".equals(scenario) && !"abandonment".equals(scenario);
        int steps = "extra_steps".equals(scenario) ? 5 : 3;
        String id = "APT-" + UUID.randomUUID().toString().substring(0, 8);
        if (successful) {
            jdbc.update("insert into appointments(appointment_id, patient_id, site, specialty, appointment_date, created_at) values (?,?,?,?,?,?)",
                id, request.patientId(), request.site(), request.specialty(), request.date(), OffsetDateTime.now(ZoneOffset.UTC));
        }
        return Map.of("appointmentId", id, "successful", successful, "steps", steps, "scenario", scenario, "simulated", true,
            "errorCode", successful ? "" : "SIM-CITA-FAIL");
    }

    public List<Map<String, Object>> list(String patientId) {
        return jdbc.query("select appointment_id, site, specialty, appointment_date from appointments where patient_id=? order by appointment_date",
            (rs, row) -> Map.of("id", rs.getString(1), "site", rs.getString(2), "specialty", rs.getString(3), "date", rs.getString(4), "status", "Confirmada"), patientId);
    }
}
