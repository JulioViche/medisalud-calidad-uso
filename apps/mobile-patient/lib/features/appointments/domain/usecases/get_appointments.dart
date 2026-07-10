import '../entities/appointment.dart';
import '../repositories/appointment_repository.dart';

class GetAppointments {
  const GetAppointments(this.repository);
  final AppointmentRepository repository;
  Future<List<Appointment>> call(String patientId) => repository.getAppointments(patientId);
}

