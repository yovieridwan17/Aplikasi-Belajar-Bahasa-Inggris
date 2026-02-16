class UserProgress {
  final int wordsLearned;
  final int quizzesTaken;
  final int correctAnswers;
  final int totalQuestions;
  final List<String> learnedWordIds;

  const UserProgress({
    this.wordsLearned = 0,
    this.quizzesTaken = 0,
    this.correctAnswers = 0,
    this.totalQuestions = 0,
    this.learnedWordIds = const [],
  });

  double get accuracy {
    if (totalQuestions == 0) return 0.0;
    return (correctAnswers / totalQuestions) * 100;
  }

  UserProgress copyWith({
    int? wordsLearned,
    int? quizzesTaken,
    int? correctAnswers,
    int? totalQuestions,
    List<String>? learnedWordIds,
  }) {
    return UserProgress(
      wordsLearned: wordsLearned ?? this.wordsLearned,
      quizzesTaken: quizzesTaken ?? this.quizzesTaken,
      correctAnswers: correctAnswers ?? this.correctAnswers,
      totalQuestions: totalQuestions ?? this.totalQuestions,
      learnedWordIds: learnedWordIds ?? this.learnedWordIds,
    );
  }
}
