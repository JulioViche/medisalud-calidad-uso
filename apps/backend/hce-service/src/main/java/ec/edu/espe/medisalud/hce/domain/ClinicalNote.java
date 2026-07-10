package ec.edu.espe.medisalud.hce.domain;

public record ClinicalNote(String patientId, String doctorId, String site, String text, String scenario) {}

