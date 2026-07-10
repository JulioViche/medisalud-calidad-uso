import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import '../../../../core/network/api_client.dart';
import '../../../../shared/presentation/atoms/primary_action_button.dart';
import '../../../../shared/presentation/templates/patient_scaffold.dart';

class TelemedicinePage extends StatefulWidget {
  const TelemedicinePage({super.key});
  @override State<TelemedicinePage> createState() => _TelemedicinePageState();
}

class _TelemedicinePageState extends State<TelemedicinePage> {
  final symptoms = TextEditingController();
  bool drop = false;
  bool loading = false;
  String? result;
  @override void dispose() { symptoms.dispose(); super.dispose(); }
  Future<void> start() async {
    setState(() { loading = true; result = null; });
    try {
      final response = await ApiClient().dio.post<Map<String, dynamic>>('/api/paciente/teleconsultas', data: {'patient_id': 'PAC-001', 'site': 'Quito', 'symptoms': symptoms.text.isEmpty ? 'Control general' : symptoms.text, 'simulate_drop': drop});
      setState(() => result = response.data?['status'].toString());
    } on DioException { setState(() => result = 'Sin conexion con el servicio'); }
    finally { if (mounted) setState(() => loading = false); }
  }
  @override
  Widget build(BuildContext context) => PatientScaffold(title: 'Telemedicina', child: ListView(padding: const EdgeInsets.all(16), children: [
        const Card(child: Padding(padding: EdgeInsets.all(16), child: Row(children: [Icon(Icons.video_camera_front, size: 35, color: Color(0xFFD45D4C)), SizedBox(width: 12), Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [Text('Consulta remota', style: TextStyle(fontWeight: FontWeight.w800)), Text('Registre sus sintomas antes de iniciar.', style: TextStyle(fontSize: 12))]))]))),
        const SizedBox(height: 14),
        TextField(controller: symptoms, maxLines: 4, decoration: const InputDecoration(labelText: 'Sintomas')),
        const SizedBox(height: 8),
        SwitchListTile(contentPadding: EdgeInsets.zero, title: const Text('Simular caida de videollamada'), value: drop, onChanged: (value) => setState(() => drop = value)),
        if (result != null) Padding(padding: const EdgeInsets.only(bottom: 10), child: Text('Estado: $result', style: const TextStyle(fontWeight: FontWeight.w700))),
        PrimaryActionButton(label: 'Preparar consulta', icon: Icons.video_call, onPressed: start, loading: loading),
      ]));
}

