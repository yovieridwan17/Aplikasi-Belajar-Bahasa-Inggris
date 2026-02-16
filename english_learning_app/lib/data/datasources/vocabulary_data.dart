import '../entities/word.dart';

class VocabularyData {
  static const List<Word> numbers = [
    Word(id: 'n1', english: 'One', indonesian: 'Satu', category: 'Numbers'),
    Word(id: 'n2', english: 'Two', indonesian: 'Dua', category: 'Numbers'),
    Word(id: 'n3', english: 'Three', indonesian: 'Tiga', category: 'Numbers'),
    Word(id: 'n4', english: 'Four', indonesian: 'Empat', category: 'Numbers'),
    Word(id: 'n5', english: 'Five', indonesian: 'Lima', category: 'Numbers'),
    Word(id: 'n6', english: 'Six', indonesian: 'Enam', category: 'Numbers'),
    Word(id: 'n7', english: 'Seven', indonesian: 'Tujuh', category: 'Numbers'),
    Word(id: 'n8', english: 'Eight', indonesian: 'Delapan', category: 'Numbers'),
    Word(id: 'n9', english: 'Nine', indonesian: 'Sembilan', category: 'Numbers'),
    Word(id: 'n10', english: 'Ten', indonesian: 'Sepuluh', category: 'Numbers'),
  ];

  static const List<Word> colors = [
    Word(id: 'c1', english: 'Red', indonesian: 'Merah', category: 'Colors'),
    Word(id: 'c2', english: 'Blue', indonesian: 'Biru', category: 'Colors'),
    Word(id: 'c3', english: 'Green', indonesian: 'Hijau', category: 'Colors'),
    Word(id: 'c4', english: 'Yellow', indonesian: 'Kuning', category: 'Colors'),
    Word(id: 'c5', english: 'Orange', indonesian: 'Oranye', category: 'Colors'),
    Word(id: 'c6', english: 'Purple', indonesian: 'Ungu', category: 'Colors'),
    Word(id: 'c7', english: 'Pink', indonesian: 'Merah muda', category: 'Colors'),
    Word(id: 'c8', english: 'Black', indonesian: 'Hitam', category: 'Colors'),
    Word(id: 'c9', english: 'White', indonesian: 'Putih', category: 'Colors'),
    Word(id: 'c10', english: 'Brown', indonesian: 'Coklat', category: 'Colors'),
  ];

  static const List<Word> animals = [
    Word(id: 'a1', english: 'Dog', indonesian: 'Anjing', category: 'Animals'),
    Word(id: 'a2', english: 'Cat', indonesian: 'Kucing', category: 'Animals'),
    Word(id: 'a3', english: 'Bird', indonesian: 'Burung', category: 'Animals'),
    Word(id: 'a4', english: 'Fish', indonesian: 'Ikan', category: 'Animals'),
    Word(id: 'a5', english: 'Horse', indonesian: 'Kuda', category: 'Animals'),
    Word(id: 'a6', english: 'Cow', indonesian: 'Sapi', category: 'Animals'),
    Word(id: 'a7', english: 'Pig', indonesian: 'Babi', category: 'Animals'),
    Word(id: 'a8', english: 'Sheep', indonesian: 'Domba', category: 'Animals'),
    Word(id: 'a9', english: 'Chicken', indonesian: 'Ayam', category: 'Animals'),
    Word(id: 'a10', english: 'Duck', indonesian: 'Bebek', category: 'Animals'),
  ];

  static const List<Word> food = [
    Word(id: 'f1', english: 'Rice', indonesian: 'Nasi', category: 'Food'),
    Word(id: 'f2', english: 'Water', indonesian: 'Air', category: 'Food'),
    Word(id: 'f3', english: 'Bread', indonesian: 'Roti', category: 'Food'),
    Word(id: 'f4', english: 'Egg', indonesian: 'Telur', category: 'Food'),
    Word(id: 'f5', english: 'Milk', indonesian: 'Susu', category: 'Food'),
    Word(id: 'f6', english: 'Apple', indonesian: 'Apel', category: 'Food'),
    Word(id: 'f7', english: 'Banana', indonesian: 'Pisang', category: 'Food'),
    Word(id: 'f8', english: 'Orange', indonesian: 'Jeruk', category: 'Food'),
    Word(id: 'f9', english: 'Chicken', indonesian: 'Ayam', category: 'Food'),
    Word(id: 'f10', english: 'Fish', indonesian: 'Ikan', category: 'Food'),
  ];

  static const List<Word> family = [
    Word(id: 'fm1', english: 'Father', indonesian: 'Ayah', category: 'Family'),
    Word(id: 'fm2', english: 'Mother', indonesian: 'Ibu', category: 'Family'),
    Word(id: 'fm3', english: 'Brother', indonesian: 'Saudara laki-laki', category: 'Family'),
    Word(id: 'fm4', english: 'Sister', indonesian: 'Saudara perempuan', category: 'Family'),
    Word(id: 'fm5', english: 'Son', indonesian: 'Anak laki-laki', category: 'Family'),
    Word(id: 'fm6', english: 'Daughter', indonesian: 'Anak perempuan', category: 'Family'),
    Word(id: 'fm7', english: 'Grandfather', indonesian: 'Kakek', category: 'Family'),
    Word(id: 'fm8', english: 'Grandmother', indonesian: 'Nenek', category: 'Family'),
    Word(id: 'fm9', english: 'Uncle', indonesian: 'Paman', category: 'Family'),
    Word(id: 'fm10', english: 'Aunt', indonesian: 'Bibi', category: 'Family'),
  ];

  static const List<Word> weather = [
    Word(id: 'w1', english: 'Sun', indonesian: 'Matahari', category: 'Weather'),
    Word(id: 'w2', english: 'Moon', indonesian: 'Bulan', category: 'Weather'),
    Word(id: 'w3', english: 'Star', indonesian: 'Bintang', category: 'Weather'),
    Word(id: 'w4', english: 'Rain', indonesian: 'Hujan', category: 'Weather'),
    Word(id: 'w5', english: 'Cloud', indonesian: 'Awan', category: 'Weather'),
    Word(id: 'w6', english: 'Wind', indonesian: 'Angin', category: 'Weather'),
    Word(id: 'w7', english: 'Snow', indonesian: 'Salju', category: 'Weather'),
    Word(id: 'w8', english: 'Hot', indonesian: 'Panas', category: 'Weather'),
    Word(id: 'w9', english: 'Cold', indonesian: 'Dingin', category: 'Weather'),
    Word(id: 'w10', english: 'Storm', indonesian: 'Badai', category: 'Weather'),
  ];

  static const List<Word> greetings = [
    Word(id: 'g1', english: 'Hello', indonesian: 'Halo', category: 'Greetings'),
    Word(id: 'g2', english: 'Good Morning', indonesian: 'Selamat Pagi', category: 'Greetings'),
    Word(id: 'g3', english: 'Good Afternoon', indonesian: 'Selamat Siang', category: 'Greetings'),
    Word(id: 'g4', english: 'Good Evening', indonesian: 'Selamat Malam', category: 'Greetings'),
    Word(id: 'g5', english: 'Goodbye', indonesian: 'Selamat Tinggal', category: 'Greetings'),
    Word(id: 'g6', english: 'Thank You', indonesian: 'Terima Kasih', category: 'Greetings'),
    Word(id: 'g7', english: 'Please', indonesian: 'Tolong', category: 'Greetings'),
    Word(id: 'g8', english: 'Sorry', indonesian: 'Maaf', category: 'Greetings'),
    Word(id: 'g9', english: 'Yes', indonesian: 'Ya', category: 'Greetings'),
    Word(id: 'g10', english: 'No', indonesian: 'Tidak', category: 'Greetings'),
  ];

  static List<Word> getAllWords() {
    return [
      ...numbers,
      ...colors,
      ...animals,
      ...food,
      ...family,
      ...weather,
      ...greetings,
    ];
  }

  static List<Word> getWordsByCategory(String category) {
    switch (category) {
      case 'Numbers':
        return numbers;
      case 'Colors':
        return colors;
      case 'Animals':
        return animals;
      case 'Food':
        return food;
      case 'Family':
        return family;
      case 'Weather':
        return weather;
      case 'Greetings':
        return greetings;
      default:
        return [];
    }
  }

  static List<String> getCategories() {
    return [
      'Numbers',
      'Colors',
      'Animals',
      'Food',
      'Family',
      'Weather',
      'Greetings',
    ];
  }
}
