import 'package:equatable/equatable.dart';

class Word extends Equatable {
  final String id;
  final String english;
  final String indonesian;
  final String category;
  final String? pronunciation;

  const Word({
    required this.id,
    required this.english,
    required this.indonesian,
    required this.category,
    this.pronunciation,
  });

  @override
  List<Object?> get props => [id, english, indonesian, category, pronunciation];
}
