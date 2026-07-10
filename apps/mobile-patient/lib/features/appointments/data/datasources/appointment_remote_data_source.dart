import 'package:dio/dio.dart';

class AppointmentRemoteDataSource {
  const AppointmentRemoteDataSource(this.dio);
  final Dio dio;
  Future<List<Map<String, dynamic>>> getAppointments(String patientId) async {
    final response = await dio.get<List<dynamic>>('/api/paciente/citas', queryParameters: {'patientId': patientId});
    return response.data!.cast<Map<String, dynamic>>();
  }
  Future<Map<String, dynamic>> create(Map<String, dynamic> payload) async {
    final response = await dio.post<Map<String, dynamic>>('/api/paciente/citas', data: payload);
    return response.data!;
  }
}

