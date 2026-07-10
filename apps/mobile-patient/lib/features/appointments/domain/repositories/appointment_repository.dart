import '../entities/appointment.dart';

abstract interface class AppointmentRepository {
  Future<List<Appointment>> getAppointments(String patientId);
  Future<Map<String, dynamic>> createAppointment({required String patientId, required String site, required String specialty, required String date, required String scenario});
}

