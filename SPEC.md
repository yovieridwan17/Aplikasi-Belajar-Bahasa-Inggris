# Spesifikasi Aplikasi Belajar Bahasa Inggris

## 1. Project Overview
- **Nama Aplikasi**: English Learning App (Belajar Bahasa Inggris)
- **Platform**: Android
- **Core Functionality**: Aplikasi pembelajaran bahasa Inggris interaktif yang membantu pengguna mempelajari kosakata, frasa, dan dasar-dasar bahasa Inggris dengan fitur quiz dan pelacakan kemajuan.

## 2. Technology Stack & Choices

### Framework & Language
- **Framework**: Flutter 3.38.9
- **Language**: Dart 3.10.8
- **Minimum Android SDK**: 21 (Android 5.0)
- **Target Android SDK**: 34

### Key Libraries/Dependencies
- `flutter_bloc` - State management
- `equatable` - Value equality for BLoC states
- `shared_preferences` - Local storage for progress
- `flutter_tts` - Text-to-speech for pronunciation
- `google_fonts` - Typography (Poppins font)
- `get_it` - Dependency injection

### State Management
- **BLoC Pattern** - Menggunakan flutter_bloc untuk mengelola state aplikasi

### Architecture Pattern
- **Clean Architecture** dengan 3 lapisan:
  - Presentation Layer (UI, BLoC)
  - Domain Layer (Entities, Use Cases)
  - Data Layer (Repositories, Data Sources)

## 3. Feature List

### Fitur Utama
1. **Home Dashboard** - Tampilan utama dengan menu navigasi ke semua fitur
2. **Vocabulary Learning** - Pembelajaran kosakata dengan flashcards
3. **Common Phrases** - Kumpulan frasa sehari-hari dalam bahasa Inggris
4. **Quiz Mode** - Kuis pilihan ganda untuk menguji pemahaman
5. **Progress Tracking** - Pelacakan kemajuan belajar pengguna
6. **Text-to-Speech** - Pelafalan kata dan frasa dengan suara

### Kategori Kosakata
- Numbers (Angka)
- Colors (Warna)
- Animals (Hewan)
- Food (Makanan)
- Family (Keluarga)
- Weather (Cuaca)
- Greetings (Salam)

## 4. UI/UX Design Direction

### Overall Visual Style
- **Material Design 3** dengan desain modern dan bersih
- Tampilan yang user-friendly dan mudah dipahami
- Animasi transisi yang halus

### Color Scheme
- **Primary**: Blue (#2196F3) - Mewakili kepercayaan dan ketenangan
- **Secondary**: Orange (#FF9800) - Mewakili energi dan semangat belajar
- **Background**: White (#FFFFFF) dengan gradasi soft blue
- **Text**: Dark Gray (#212121) untuk readability

### Layout Approach
- **Bottom Navigation** untuk navigasi utama (Home, Vocabulary, Quiz, Progress)
- **Card-based UI** untuk menampilkan konten pembelajaran
- **Flashcard-style** untuk pembelajaran kosakata

### Typography
- **Font Family**: Poppins (Google Fonts)
- **Heading**: Bold, 24-32sp
- **Body**: Regular, 16sp
- **Caption**: Light, 12-14sp
