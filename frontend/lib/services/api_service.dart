import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/chat_message.dart';

class ApiService {
  static const String _baseUrl = 'http://localhost:8000'; // Change to your backend URL

  static Future<ChatMessage> sendMessage({
    required String userId,
    required String mode,
    required String message,
  }) async {
    final url = Uri.parse('$_baseUrl/chat');
    final resp = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'user_id': userId,
        'mode': mode,
        'message': message,
      }),
    );
    if (resp.statusCode == 200) {
      final data = jsonDecode(resp.body);
      return ChatMessage(
        text: data['reply'] ?? '',
        isUser: false,
        corrected: data['corrected'] ?? '',
        explanationId: data['explanation_id'] ?? '',
        tip: data['tip'] ?? '',
      );
    } else {
      throw Exception('API error');
    }
  }
}
