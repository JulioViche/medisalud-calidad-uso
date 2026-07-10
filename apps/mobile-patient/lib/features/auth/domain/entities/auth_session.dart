class AuthSession {
  const AuthSession({
    required this.email,
    required this.patientName,
    required this.patientId,
    required this.site,
  });

  final String email;
  final String patientName;
  final String patientId;
  final String site;
}
