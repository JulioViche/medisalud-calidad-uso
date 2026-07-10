package ec.edu.espe.medisalud.billing.application;
import ec.edu.espe.medisalud.billing.domain.InvoiceRequest;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.Map;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;
@Service
public class BillingService {
    private final JdbcTemplate jdbc;
    public BillingService(JdbcTemplate jdbc) { this.jdbc = jdbc; }
    public Map<String,Object> invoice(InvoiceRequest request) {
        String scenario = request.scenario() == null ? "normal" : request.scenario();
        boolean duplicate = "duplicate".equals(scenario);
        String invoiceId = "INV-" + request.transactionId();
        jdbc.update("insert into invoices(invoice_id, transaction_id, patient_id, amount, site, duplicated, created_at) values (?,?,?,?,?,?,?)",
            invoiceId + (duplicate ? "-D" : ""), request.transactionId(), request.patientId(), request.amount(), request.site(), duplicate, OffsetDateTime.now(ZoneOffset.UTC));
        return Map.of("invoiceId", invoiceId, "duplicate", duplicate, "scenario", scenario, "risk", duplicate ? "financial" : "none", "simulated", true);
    }
}
