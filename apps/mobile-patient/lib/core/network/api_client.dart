import 'package:dio/dio.dart';
import '../config/api_config.dart';

class ApiClient {
  ApiClient()
      : dio = Dio(BaseOptions(
          baseUrl: ApiConfig.baseUrl,
          connectTimeout: const Duration(seconds: 4),
          receiveTimeout: const Duration(seconds: 6),
          headers: const {'Content-Type': 'application/json'},
        ));
  final Dio dio;
}

