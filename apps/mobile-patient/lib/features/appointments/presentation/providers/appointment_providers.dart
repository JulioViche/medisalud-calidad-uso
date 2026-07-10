import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../../../core/network/api_client.dart';
import '../../data/datasources/appointment_remote_data_source.dart';
import '../../data/repositories/appointment_repository_impl.dart';
import '../../domain/entities/appointment.dart';
import '../../domain/repositories/appointment_repository.dart';
import '../../domain/usecases/get_appointments.dart';

final apiClientProvider = Provider((_) => ApiClient());
final appointmentRepositoryProvider = Provider<AppointmentRepository>((ref) => AppointmentRepositoryImpl(AppointmentRemoteDataSource(ref.watch(apiClientProvider).dio)));
final getAppointmentsProvider = Provider((ref) => GetAppointments(ref.watch(appointmentRepositoryProvider)));
final appointmentsProvider = FutureProvider<List<Appointment>>((ref) => ref.watch(getAppointmentsProvider)('PAC-001'));

