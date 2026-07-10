import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../../../shared/presentation/atoms/primary_action_button.dart';
import '../../../../shared/presentation/templates/patient_scaffold.dart';
import '../providers/appointment_providers.dart';
import '../widgets/appointment_card.dart';

class AppointmentsPage extends ConsumerStatefulWidget {
  const AppointmentsPage({super.key});
  @override ConsumerState<AppointmentsPage> createState() => _AppointmentsPageState();
}

class _AppointmentsPageState extends ConsumerState<AppointmentsPage> {
  bool simulateFailure = false;
  bool loading = false;
  String? message;
  Future<void> create() async {
    setState(() { loading = true; message = null; });
    try {
      final result = await ref.read(appointmentRepositoryProvider).createAppointment(patientId: 'PAC-001', site: 'Quito', specialty: 'Medicina interna', date: '2025-12-19 10:00', scenario: simulateFailure ? 'availability_failure' : 'normal');
      setState(() => message = result['successful'] == true ? 'Cita registrada correctamente' : 'No fue posible completar el agendamiento');
      ref.invalidate(appointmentsProvider);
    } catch (_) { setState(() => message = 'Gateway no disponible: fallo registrado para la simulacion'); }
    finally { if (mounted) setState(() => loading = false); }
  }
  @override
  Widget build(BuildContext context) {
    final appointments = ref.watch(appointmentsProvider);
    return PatientScaffold(title: 'Mis citas', child: ListView(padding: const EdgeInsets.all(16), children: [
      Text('Proximas atenciones', style: Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.w800)),
      const SizedBox(height: 12),
      appointments.when(
        data: (items) => Column(children: items.map((item) => Padding(padding: const EdgeInsets.only(bottom: 10), child: AppointmentCard(appointment: item))).toList()),
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (_, _) => const Text('No se pudieron cargar las citas.'),
      ),
      const SizedBox(height: 12),
      SwitchListTile(contentPadding: EdgeInsets.zero, title: const Text('Simular error de disponibilidad'), subtitle: const Text('Genera evidencia sin corregir el fallo'), value: simulateFailure, onChanged: (value) => setState(() => simulateFailure = value)),
      if (message != null) Padding(padding: const EdgeInsets.only(bottom: 10), child: Text(message!, style: const TextStyle(fontWeight: FontWeight.w700))),
      PrimaryActionButton(label: 'Agendar cita', icon: Icons.add, onPressed: create, loading: loading),
    ]));
  }
}

