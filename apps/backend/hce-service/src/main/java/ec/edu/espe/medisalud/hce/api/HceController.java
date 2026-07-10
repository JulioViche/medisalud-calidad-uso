package ec.edu.espe.medisalud.hce.api;

import ec.edu.espe.medisalud.hce.application.ClinicalRecordService;
import ec.edu.espe.medisalud.hce.domain.ClinicalNote;
import java.util.List;
import java.util.Map;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
public class HceController {
    private final ClinicalRecordService service;
    public HceController(ClinicalRecordService service) { this.service = service; }

    @PostMapping("/api/hce/notas")
    @ResponseStatus(HttpStatus.CREATED)
    Map<String, Object> save(@RequestBody ClinicalNote note) { return service.save(note); }

    @GetMapping("/api/paciente/resultados")
    List<Map<String, Object>> results(@RequestParam(defaultValue = "PAC-001") String patientId) { return service.results(patientId); }
}

