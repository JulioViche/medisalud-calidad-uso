package ec.edu.espe.medisalud.billing.api;
import ec.edu.espe.medisalud.billing.application.BillingService;
import ec.edu.espe.medisalud.billing.domain.InvoiceRequest;
import java.util.Map;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
@RestController @RequestMapping("/api/facturacion")
public class BillingController {
    private final BillingService service;
    public BillingController(BillingService service) { this.service = service; }
    @PostMapping @ResponseStatus(HttpStatus.CREATED) Map<String,Object> create(@RequestBody InvoiceRequest request) { return service.invoice(request); }
}

