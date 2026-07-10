import 'package:flutter/material.dart';

class PrimaryActionButton extends StatelessWidget {
  const PrimaryActionButton({required this.label, required this.icon, required this.onPressed, this.loading = false, super.key});
  final String label;
  final IconData icon;
  final VoidCallback? onPressed;
  final bool loading;
  @override
  Widget build(BuildContext context) => SizedBox(
        width: double.infinity,
        height: 48,
        child: FilledButton.icon(
          onPressed: loading ? null : onPressed,
          icon: loading
              ? const SizedBox.square(dimension: 17, child: CircularProgressIndicator(strokeWidth: 2))
              : Icon(icon, size: 19),
          label: Text(label),
        ),
      );
}

