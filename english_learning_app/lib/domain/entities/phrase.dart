class Phrase {
  final String id;
  final String english;
  final String indonesian;
  final String category;
  final String? pronunciation;

  const Phrase({
    required this.id,
    required this.english,
    required this.indonesian,
    required this.category,
    this.pronunciation,
  });
}
