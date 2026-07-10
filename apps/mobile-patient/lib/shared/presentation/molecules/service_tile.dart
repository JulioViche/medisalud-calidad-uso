import 'package:flutter/material.dart';

class ServiceTile extends StatelessWidget {
  const ServiceTile({required this.label, required this.icon, required this.color, required this.onTap, super.key});
  final String label;
  final IconData icon;
  final Color color;
  final VoidCallback onTap;
  @override
  Widget build(BuildContext context) => Material(
        color: Colors.white,
        borderRadius: BorderRadius.circular(7),
        child: InkWell(
          onTap: onTap,
          borderRadius: BorderRadius.circular(7),
          child: Container(
            constraints: const BoxConstraints(minHeight: 102),
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(border: Border.all(color: const Color(0xFFDDE5E3)), borderRadius: BorderRadius.circular(7)),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
              DecoratedBox(decoration: BoxDecoration(color: color.withValues(alpha: .12), borderRadius: BorderRadius.circular(6)), child: Padding(padding: const EdgeInsets.all(8), child: Icon(icon, color: color, size: 20))),
              Text(label, maxLines: 2, style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w700)),
            ]),
          ),
        ),
      );
}

