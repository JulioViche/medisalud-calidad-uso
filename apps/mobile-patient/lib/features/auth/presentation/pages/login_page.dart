import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../../../core/theme/app_theme.dart';
import '../../../../shared/presentation/atoms/primary_action_button.dart';
import '../../data/repositories/local_auth_repository.dart';
import '../providers/auth_controller.dart';

class LoginPage extends ConsumerStatefulWidget {
  const LoginPage({super.key});

  @override
  ConsumerState<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends ConsumerState<LoginPage> {
  final emailController = TextEditingController(text: LocalAuthRepository.demoEmail);
  final passwordController = TextEditingController(text: LocalAuthRepository.demoPassword);
  bool obscurePassword = true;
  String? error;

  @override
  void dispose() {
    emailController.dispose();
    passwordController.dispose();
    super.dispose();
  }

  void submit() {
    final authenticated = ref.read(authControllerProvider.notifier).signIn(
          email: emailController.text,
          password: passwordController.text,
        );
    setState(() => error = authenticated ? null : 'El usuario o la contraseña no son correctos.');
  }

  @override
  Widget build(BuildContext context) => Scaffold(
        body: SafeArea(
          child: Center(
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(22),
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 440),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    const Align(
                      alignment: Alignment.centerLeft,
                      child: CircleAvatar(
                        radius: 28,
                        backgroundColor: AppTheme.teal,
                        foregroundColor: Colors.white,
                        child: Icon(Icons.health_and_safety_outlined, size: 29),
                      ),
                    ),
                    const SizedBox(height: 28),
                    const Text('MediSalud Paciente', style: TextStyle(fontSize: 27, fontWeight: FontWeight.w800, color: AppTheme.ink)),
                    const SizedBox(height: 6),
                    const Text('Ingrese para gestionar sus citas, resultados y teleconsultas.', style: TextStyle(color: Colors.black54, height: 1.4)),
                    const SizedBox(height: 28),
                    TextField(
                      controller: emailController,
                      keyboardType: TextInputType.emailAddress,
                      autofillHints: const [AutofillHints.username],
                      decoration: const InputDecoration(labelText: 'Correo electrónico', prefixIcon: Icon(Icons.alternate_email)),
                      onChanged: (_) => setState(() => error = null),
                    ),
                    const SizedBox(height: 14),
                    TextField(
                      controller: passwordController,
                      obscureText: obscurePassword,
                      autofillHints: const [AutofillHints.password],
                      decoration: InputDecoration(
                        labelText: 'Contraseña',
                        prefixIcon: const Icon(Icons.lock_outline),
                        suffixIcon: IconButton(
                          onPressed: () => setState(() => obscurePassword = !obscurePassword),
                          icon: Icon(obscurePassword ? Icons.visibility_outlined : Icons.visibility_off_outlined),
                          tooltip: obscurePassword ? 'Mostrar contraseña' : 'Ocultar contraseña',
                        ),
                      ),
                      onChanged: (_) => setState(() => error = null),
                      onSubmitted: (_) => submit(),
                    ),
                    if (error != null) Padding(
                      padding: const EdgeInsets.only(top: 12),
                      child: Text(error!, style: const TextStyle(color: AppTheme.coral, fontWeight: FontWeight.w700)),
                    ),
                    const SizedBox(height: 20),
                    PrimaryActionButton(label: 'Iniciar sesión', icon: Icons.login, onPressed: submit),
                    const SizedBox(height: 22),
                    Container(
                      padding: const EdgeInsets.all(14),
                      decoration: BoxDecoration(color: const Color(0xFFE7F2F0), borderRadius: BorderRadius.circular(7)),
                      child: const Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text('Cuenta de demostración', style: TextStyle(fontWeight: FontWeight.w800, color: AppTheme.teal)),
                          SizedBox(height: 5),
                          Text('paciente@medisalud.local\nMedisalud2025', style: TextStyle(fontSize: 12, height: 1.5)),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      );
}
