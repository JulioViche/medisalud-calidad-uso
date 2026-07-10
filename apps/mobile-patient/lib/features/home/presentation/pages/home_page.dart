import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../../core/theme/app_theme.dart';
import '../../../../shared/presentation/molecules/service_tile.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});
  @override
  Widget build(BuildContext context) {
    final services = [
      ('Citas', Icons.calendar_month, AppTheme.teal, '/appointments'),
      ('Resultados', Icons.biotech, const Color(0xFF377C9D), '/results'),
      ('Telemedicina', Icons.video_call, AppTheme.coral, '/telemedicine'),
      ('Encuesta', Icons.rate_review, const Color(0xFFD59622), '/survey'),
    ];
    return Scaffold(body: SafeArea(child: ListView(padding: const EdgeInsets.fromLTRB(18, 16, 18, 28), children: [
      Row(children: [
        const CircleAvatar(backgroundColor: AppTheme.teal, foregroundColor: Colors.white, child: Text('AT')),
        const SizedBox(width: 10),
        const Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [Text('Buenos dias', style: TextStyle(fontSize: 11, color: Colors.black54)), Text('Ana Torres', style: TextStyle(fontWeight: FontWeight.w800, fontSize: 16))])),
        IconButton(onPressed: () => context.push('/notifications'), icon: const Icon(Icons.notifications_none), tooltip: 'Notificaciones'),
      ]),
      const SizedBox(height: 22),
      Container(padding: const EdgeInsets.all(18), decoration: BoxDecoration(color: const Color(0xFF173F3B), borderRadius: BorderRadius.circular(8)), child: const Column(crossAxisAlignment: CrossAxisAlignment.start, children: [Text('Proxima cita', style: TextStyle(color: Color(0xFF8CD2C7), fontSize: 11, fontWeight: FontWeight.w700)), SizedBox(height: 8), Text('Medicina interna', style: TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.w800)), SizedBox(height: 4), Text('12 dic · 09:30 · Sede Quito', style: TextStyle(color: Color(0xFFD5E6E3), fontSize: 12))])),
      const SizedBox(height: 22),
      const Text('Servicios', style: TextStyle(fontSize: 17, fontWeight: FontWeight.w800)),
      const SizedBox(height: 12),
      GridView.count(shrinkWrap: true, physics: const NeverScrollableScrollPhysics(), crossAxisCount: 2, childAspectRatio: 1.35, mainAxisSpacing: 10, crossAxisSpacing: 10, children: services.map((service) => ServiceTile(label: service.$1, icon: service.$2, color: service.$3, onTap: () => context.push(service.$4))).toList()),
      const SizedBox(height: 22),
      const Text('Actividad reciente', style: TextStyle(fontSize: 17, fontWeight: FontWeight.w800)),
      const SizedBox(height: 12),
      const Card(child: ListTile(leading: Icon(Icons.check_circle, color: Color(0xFF27835B)), title: Text('Resultado disponible', style: TextStyle(fontSize: 13, fontWeight: FontWeight.w700)), subtitle: Text('Hemograma completo · 18 nov', style: TextStyle(fontSize: 11)), trailing: Icon(Icons.chevron_right))),
    ])));
  }
}

