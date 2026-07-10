import 'package:flutter/material.dart';
import '../../../../shared/presentation/atoms/app_badge.dart';
import '../../../../shared/presentation/templates/patient_scaffold.dart';

class ResultsPage extends StatelessWidget {
  const ResultsPage({super.key});
  @override
  Widget build(BuildContext context) => PatientScaffold(title: 'Resultados', child: ListView(padding: const EdgeInsets.all(16), children: const [
        Card(child: ListTile(leading: Icon(Icons.science, color: Color(0xFF377C9D)), title: Text('Hemograma completo'), subtitle: Text('Laboratorio · 18 nov 2025'), trailing: AppBadge(label: 'Disponible'))),
        SizedBox(height: 10),
        Card(child: ListTile(leading: Icon(Icons.image_search, color: Color(0xFFD45D4C)), title: Text('Radiografia de torax'), subtitle: Text('Imagenologia · 12 nov 2025'), trailing: AppBadge(label: 'Disponible'))),
      ]));
}

