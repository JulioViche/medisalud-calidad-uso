package ec.edu.espe.medisalud.appointments.api;
import ec.edu.espe.medisalud.appointments.application.AppointmentService;
import ec.edu.espe.medisalud.appointments.domain.AppointmentRequest;
import java.util.List;
import java.util.Map;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
@RestController
@RequestMapping("/api/paciente/citas")
public class AppointmentController {
    private final AppointmentService service;
    public AppointmentController(AppointmentService service) { this.service = service; }
    @GetMapping List<Map<String, Object>> list(@RequestParam(defaultValue="PAC-001") String patientId) { return service.list(patientId); }
    @PostMapping @ResponseStatus(HttpStatus.CREATED) Map<String, Object> create(@RequestBody AppointmentRequest request) { return service.create(request); }
}

