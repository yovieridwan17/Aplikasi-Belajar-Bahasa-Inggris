import 'package:flutter/material.dart';
import 'screens/chat_screen.dart';

void main() {
  runApp(EnglishChatApp());
}

class EnglishChatApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AI English Chat',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: ChatScreen(),
    );
  }
}
