import '../../domain/entities/appointment.dart';
import '../../domain/repositories/appointment_repository.dart';
import '../datasources/appointment_remote_data_source.dart';
import '../models/appointment_model.dart';

class AppointmentRepositoryImpl implements AppointmentRepository {
  const AppointmentRepositoryImpl(this.remote);
  final AppointmentRemoteDataSource remote;
  @override
  Future<List<Appointment>> getAppointments(String patientId) async {
    try {
      final rows = await remote.getAppointments(patientId);
      if (rows.isNotEmpty) return rows.map(AppointmentModel.fromJson).toList();
    } catch (_) {
      // The offline sample is explicitly simulated and keeps the local lab usable.
    }
    return const [AppointmentModel(id: 'APT-DEMO-01', site: 'Quito', specialty: 'Medicina interna', date: '2025-12-12 09:30', status: 'Confirmada')];
  }
  @override
  Future<Map<String, dynamic>> createAppointment({required String patientId, required String site, required String specialty, required String date, required String scenario}) =>
      remote.create({'patientId': patientId, 'site': site, 'specialty': specialty, 'date': date, 'scenario': scenario});
}

