import '../entities/auth_session.dart';

abstract interface class AuthRepository {
  AuthSession? authenticate({required String email, required String password});
}
