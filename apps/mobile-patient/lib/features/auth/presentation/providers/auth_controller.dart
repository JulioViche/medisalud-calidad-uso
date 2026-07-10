import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../data/repositories/local_auth_repository.dart';
import '../../domain/entities/auth_session.dart';
import '../../domain/repositories/auth_repository.dart';

final authRepositoryProvider = Provider<AuthRepository>((ref) => LocalAuthRepository());

final authControllerProvider = NotifierProvider<AuthController, AuthSession?>(AuthController.new);

class AuthController extends Notifier<AuthSession?> {
  @override
  AuthSession? build() => null;

  bool signIn({required String email, required String password}) {
    final session = ref.read(authRepositoryProvider).authenticate(email: email, password: password);
    state = session;
    return session != null;
  }

  void signOut() => state = null;
}
