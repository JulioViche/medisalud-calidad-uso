import 'package:flutter/material.dart';

abstract final class AppTheme {
  static const teal = Color(0xFF0C695F);
  static const coral = Color(0xFFD45D4C);
  static const ink = Color(0xFF173330);
  static ThemeData get light => ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: teal, primary: teal, secondary: coral),
        scaffoldBackgroundColor: const Color(0xFFF2F5F4),
        useMaterial3: true,
        appBarTheme: const AppBarTheme(
          backgroundColor: Colors.white,
          foregroundColor: ink,
          elevation: 0,
          titleTextStyle: TextStyle(fontSize: 18, fontWeight: FontWeight.w700, color: ink),
        ),
        cardTheme: const CardThemeData(
          color: Colors.white,
          elevation: 0,
          margin: EdgeInsets.zero,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.all(Radius.circular(8)),
            side: BorderSide(color: Color(0xFFDDE5E3)),
          ),
        ),
        inputDecorationTheme: const InputDecorationTheme(
          filled: true,
          fillColor: Colors.white,
          border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(6))),
        ),
      );
}

