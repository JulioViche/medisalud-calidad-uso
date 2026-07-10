import 'package:flutter/material.dart';
import '../../../../shared/presentation/atoms/app_badge.dart';
import '../../domain/entities/appointment.dart';

class AppointmentCard extends StatelessWidget {
  const AppointmentCard({required this.appointment, super.key});
  final Appointment appointment;
  @override
  Widget build(BuildContext context) => Card(
        child: Padding(
          padding: const EdgeInsets.all(15),
          child: Row(children: [
            const DecoratedBox(decoration: BoxDecoration(color: Color(0xFFE2F2EF), borderRadius: BorderRadius.all(Radius.circular(6))), child: Padding(padding: EdgeInsets.all(10), child: Icon(Icons.calendar_today, color: Color(0xFF0C695F)))),
            const SizedBox(width: 12),
            Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [Text(appointment.specialty, style: const TextStyle(fontWeight: FontWeight.w800)), const SizedBox(height: 4), Text('${appointment.date} · ${appointment.site}', style: TextStyle(fontSize: 12, color: Colors.grey.shade700))])),
            AppBadge(label: appointment.status),
          ]),
        ),
      );
}

