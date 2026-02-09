import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import '../models/chat_message.dart';
import '../services/api_service.dart';

class ChatScreen extends StatefulWidget {
  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final _controller = TextEditingController();
  final List<ChatMessage> _messages = [];
  String _mode = 'daily';
  bool _loading = false;
  String? _error;

  void _sendMessage() async {
    final text = _controller.text.trim();
    if (text.isEmpty) return;
    setState(() {
      _messages.add(ChatMessage(
        text: text,
        isUser: true,
        corrected: '',
        explanationId: '',
        tip: '',
      ));
      _loading = true;
      _error = null;
    });
    _controller.clear();

    try {
      final user = FirebaseAuth.instance.currentUser;
      if (user == null) throw Exception('Not authenticated');
      final aiMsg = await ApiService.sendMessage(
        userId: user.uid,
        mode: _mode,
        message: text,
      );
      setState(() {
        _messages.add(aiMsg);
      });
    } catch (e) {
      setState(() {
        _error = 'Failed to get AI reply. Please try again.';
      });
    } finally {
      setState(() {
        _loading = false;
      });
    }
  }

  Widget _buildMessage(ChatMessage msg) {
    final align = msg.isUser ? CrossAxisAlignment.end : CrossAxisAlignment.start;
    final color = msg.isUser ? Colors.indigo[100] : Colors.grey[200];
    final radius = msg.isUser
        ? BorderRadius.only(
            topLeft: Radius.circular(16),
            topRight: Radius.circular(16),
            bottomLeft: Radius.circular(16),
          )
        : BorderRadius.only(
            topLeft: Radius.circular(16),
            topRight: Radius.circular(16),
            bottomRight: Radius.circular(16),
          );
    return Column(
      crossAxisAlignment: align,
      children: [
        Container(
          margin: EdgeInsets.symmetric(vertical: 4, horizontal: 8),
          padding: EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: color,
            borderRadius: radius,
          ),
          child: Text(msg.text, style: TextStyle(fontSize: 16)),
        ),
        if (!msg.isUser && msg.corrected.isNotEmpty)
          Padding(
            padding: EdgeInsets.only(left: 16, right: 16, bottom: 2),
            child: Text('Corrected: ${msg.corrected}', style: TextStyle(fontSize: 13, color: Colors.green[700])),
          ),
        if (!msg.isUser && msg.explanationId.isNotEmpty)
          Padding(
            padding: EdgeInsets.only(left: 16, right: 16, bottom: 2),
            child: Text('Penjelasan: ${msg.explanationId}', style: TextStyle(fontSize: 13, color: Colors.blueGrey)),
          ),
        if (!msg.isUser && msg.tip.isNotEmpty)
          Padding(
            padding: EdgeInsets.only(left: 16, right: 16, bottom: 2),
            child: Text('Tip: ${msg.tip}', style: TextStyle(fontSize: 13, color: Colors.orange[700])),
          ),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('AI English Chat'),
        actions: [
          DropdownButton<String>(
            value: _mode,
            underline: SizedBox(),
            icon: Icon(Icons.arrow_drop_down, color: Colors.white),
            dropdownColor: Colors.indigo[50],
            items: [
              DropdownMenuItem(value: 'daily', child: Text('Daily Conversation')),
              DropdownMenuItem(value: 'interview', child: Text('Interview Practice')),
              DropdownMenuItem(value: 'travel', child: Text('Travel English')),
            ],
            onChanged: (val) {
              if (val != null) setState(() => _mode = val);
            },
          ),
          IconButton(
            icon: Icon(Icons.logout),
            onPressed: () async {
              await FirebaseAuth.instance.signOut();
              Navigator.pushReplacementNamed(context, '/');
            },
          ),
        ],
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              reverse: false,
              itemCount: _messages.length,
              itemBuilder: (ctx, i) => _buildMessage(_messages[i]),
            ),
          ),
          if (_loading)
            Padding(
              padding: EdgeInsets.all(8),
              child: Row(
                children: [
                  CircularProgressIndicator(),
                  SizedBox(width: 12),
                  Text('AI is typing...'),
                ],
              ),
            ),
          if (_error != null)
            Padding(
              padding: EdgeInsets.all(8),
              child: Text(_error!, style: TextStyle(color: Colors.red)),
            ),
          Padding(
            padding: EdgeInsets.all(8),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    decoration: InputDecoration(
                      hintText: 'Type your message...',
                      border: OutlineInputBorder(),
                    ),
                    onSubmitted: (_) => _sendMessage(),
                  ),
                ),
                SizedBox(width: 8),
                IconButton(
                  icon: Icon(Icons.send, color: Colors.indigo),
                  onPressed: _loading ? null : _sendMessage,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
