import 'package:flutter/material.dart';
import '../../../../shared/presentation/templates/patient_scaffold.dart';

class NotificationsPage extends StatelessWidget {
  const NotificationsPage({super.key});
  @override
  Widget build(BuildContext context) => PatientScaffold(title: 'Notificaciones', child: ListView(padding: const EdgeInsets.all(16), children: const [
        Card(child: ListTile(leading: Icon(Icons.calendar_today, color: Color(0xFF0C695F)), title: Text('Cita confirmada'), subtitle: Text('Medicina interna · 12 dic, 09:30'))),
        SizedBox(height: 10),
        Card(child: ListTile(leading: Icon(Icons.biotech, color: Color(0xFF377C9D)), title: Text('Nuevo resultado'), subtitle: Text('Su hemograma ya esta disponible'))),
      ]));
}

