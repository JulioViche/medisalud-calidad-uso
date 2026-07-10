import 'package:flutter/material.dart';
import '../core/theme/app_theme.dart';
import 'router.dart';

class MediSaludApp extends StatelessWidget {
  const MediSaludApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp.router(
        title: 'MediSalud Paciente',
        debugShowCheckedModeBanner: false,
        theme: AppTheme.light,
        routerConfig: appRouter,
      );
}

