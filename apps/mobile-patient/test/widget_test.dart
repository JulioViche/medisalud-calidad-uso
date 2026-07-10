import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:medisalud_patient/shared/presentation/atoms/app_badge.dart';

void main() {
  testWidgets('AppBadge displays its label', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: AppBadge(label: 'Disponible'))));
    expect(find.text('Disponible'), findsOneWidget);
  });
}

