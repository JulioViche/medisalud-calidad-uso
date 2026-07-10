package ec.edu.espe.medisalud.appointments.domain;
public record AppointmentRequest(String patientId, String site, String specialty, String date, String scenario) {}

