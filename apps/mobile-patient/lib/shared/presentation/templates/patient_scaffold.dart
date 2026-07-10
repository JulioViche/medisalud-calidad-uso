import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class PatientScaffold extends StatelessWidget {
  const PatientScaffold({required this.title, required this.child, this.actions, super.key});
  final String title;
  final Widget child;
  final List<Widget>? actions;
  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(
          title: Text(title),
          actions: actions,
          leading: context.canPop() ? IconButton(onPressed: context.pop, icon: const Icon(Icons.arrow_back), tooltip: 'Volver') : null,
        ),
        body: SafeArea(child: child),
      );
}

