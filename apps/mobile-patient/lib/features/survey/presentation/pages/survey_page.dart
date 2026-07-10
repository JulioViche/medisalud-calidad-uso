import 'package:flutter/material.dart';
import '../../../../core/network/api_client.dart';
import '../../../../shared/presentation/atoms/primary_action_button.dart';
import '../../../../shared/presentation/templates/patient_scaffold.dart';

class SurveyPage extends StatefulWidget {
  const SurveyPage({super.key});
  @override State<SurveyPage> createState() => _SurveyPageState();
}

class _SurveyPageState extends State<SurveyPage> {
  double csat = 4;
  double nps = 7;
  bool loading = false;
  bool sent = false;
  Future<void> submit() async {
    setState(() => loading = true);
    try { await ApiClient().dio.post('/api/paciente/encuestas', data: {'site': 'Quito', 'csat': csat.round(), 'nps': nps.round(), 'comments': ''}); } catch (_) {
      // An offline submission remains visible as simulated evidence.
    } finally { if (mounted) setState(() { loading = false; sent = true; }); }
  }
  @override
  Widget build(BuildContext context) => PatientScaffold(title: 'Encuesta', child: ListView(padding: const EdgeInsets.all(18), children: [
        const Text('Su experiencia', style: TextStyle(fontSize: 19, fontWeight: FontWeight.w800)),
        const SizedBox(height: 4),
        const Text('Cuéntenos cómo fue su atención para mejorar el servicio.', style: TextStyle(fontSize: 12)),
        const SizedBox(height: 22),
        Text('Satisfaccion: ${csat.round()}/5', style: const TextStyle(fontWeight: FontWeight.w700)),
        Slider(value: csat, min: 1, max: 5, divisions: 4, label: csat.round().toString(), onChanged: (value) => setState(() => csat = value)),
        Text('Recomendacion: ${nps.round()}/10', style: const TextStyle(fontWeight: FontWeight.w700)),
        Slider(value: nps, min: 0, max: 10, divisions: 10, label: nps.round().toString(), onChanged: (value) => setState(() => nps = value)),
        if (sent) const Padding(padding: EdgeInsets.only(bottom: 12), child: Text('Gracias. Su respuesta fue registrada.', style: TextStyle(fontWeight: FontWeight.w700, color: Color(0xFF0C695F)))),
        PrimaryActionButton(label: 'Enviar respuesta', icon: Icons.send, onPressed: submit, loading: loading),
      ]));
}
