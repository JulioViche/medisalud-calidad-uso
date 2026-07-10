import '../../domain/entities/appointment.dart';

class AppointmentModel extends Appointment {
  const AppointmentModel({required super.id, required super.site, required super.specialty, required super.date, required super.status});
  factory AppointmentModel.fromJson(Map<String, dynamic> json) => AppointmentModel(
        id: json['id']?.toString() ?? 'APT-SIM',
        site: json['site']?.toString() ?? 'Quito',
        specialty: json['specialty']?.toString() ?? 'Medicina general',
        date: json['date']?.toString() ?? '2025-12-12 09:00',
        status: json['status']?.toString() ?? 'Confirmada',
      );
}

