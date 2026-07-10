import 'package:flutter/material.dart';

class AppBadge extends StatelessWidget {
  const AppBadge({required this.label, this.color = const Color(0xFF0C695F), super.key});
  final String label;
  final Color color;
  @override
  Widget build(BuildContext context) => DecoratedBox(
        decoration: BoxDecoration(color: color.withValues(alpha: .12), borderRadius: BorderRadius.circular(4)),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 4),
          child: Text(label, style: TextStyle(color: color, fontSize: 10, fontWeight: FontWeight.w800)),
        ),
      );
}

