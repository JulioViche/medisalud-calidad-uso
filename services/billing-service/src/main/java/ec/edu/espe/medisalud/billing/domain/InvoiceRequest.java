package ec.edu.espe.medisalud.billing.domain;
import java.math.BigDecimal;
public record InvoiceRequest(String transactionId, String patientId, BigDecimal amount, String site, String scenario) {}

