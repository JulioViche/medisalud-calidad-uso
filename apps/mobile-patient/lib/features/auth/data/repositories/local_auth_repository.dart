import '../../domain/entities/auth_session.dart';
import '../../domain/repositories/auth_repository.dart';

class LocalAuthRepository implements AuthRepository {
  static const demoEmail = 'paciente@medisalud.local';
  static const demoPassword = 'Medisalud2025';

  @override
  AuthSession? authenticate({required String email, required String password}) {
    if (email.trim().toLowerCase() != demoEmail || password != demoPassword) return null;
    return const AuthSession(
      email: demoEmail,
      patientName: 'Ana Torres',
      patientId: 'PAC-001',
      site: 'Quito',
    );
  }
}
