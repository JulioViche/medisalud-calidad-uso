import 'package:go_router/go_router.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../features/auth/presentation/pages/login_page.dart';
import '../features/auth/presentation/providers/auth_controller.dart';
import '../features/appointments/presentation/pages/appointments_page.dart';
import '../features/home/presentation/pages/home_page.dart';
import '../features/notifications/presentation/pages/notifications_page.dart';
import '../features/results/presentation/pages/results_page.dart';
import '../features/survey/presentation/pages/survey_page.dart';
import '../features/telemedicine/presentation/pages/telemedicine_page.dart';

final appRouterProvider = Provider<GoRouter>((ref) {
  final session = ref.watch(authControllerProvider);
  return GoRouter(
    initialLocation: session == null ? '/login' : '/',
    redirect: (_, state) {
      final isLogin = state.matchedLocation == '/login';
      if (session == null) return isLogin ? null : '/login';
      if (isLogin) return '/';
      return null;
    },
    routes: [
      GoRoute(path: '/login', builder: (_, _) => const LoginPage()),
      GoRoute(path: '/', builder: (_, _) => const HomePage()),
      GoRoute(path: '/appointments', builder: (_, _) => const AppointmentsPage()),
      GoRoute(path: '/results', builder: (_, _) => const ResultsPage()),
      GoRoute(path: '/telemedicine', builder: (_, _) => const TelemedicinePage()),
      GoRoute(path: '/survey', builder: (_, _) => const SurveyPage()),
      GoRoute(path: '/notifications', builder: (_, _) => const NotificationsPage()),
    ],
  );
});
