class ChatMessage {
  final String text;
  final bool isUser;
  final String corrected;
  final String explanationId;
  final String tip;

  ChatMessage({
    required this.text,
    required this.isUser,
    required this.corrected,
    required this.explanationId,
    required this.tip,
  });
}
