# AI English Chat App

AI-powered English learning chat app for Indonesian learners.

## Features

- Login/Register (Firebase Auth)
- WhatsApp-style chat UI
- Daily, Interview, and Travel English modes
- AI grammar correction, explanations, and tips
- FastAPI backend with OpenAI-compatible LLM

## Backend

- Python FastAPI
- POST /chat endpoint
- Requires OpenAI API key

### Run Backend

1. Copy `.env.example` to `.env` and fill in your OpenAI API key.
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run:
   ```powershell
   uvicorn main:app --reload
   ```

## Frontend

- Flutter mobile app
- Firebase Auth & Firestore

### Firebase Setup

1. Create Firebase project at https://console.firebase.google.com/
2. Add Android app, download `google-services.json`, place in `android/app/`
3. Enable Email/Password Auth
4. Add Firestore (test mode for dev)

### Run Frontend

1. Add Firebase dependencies to `pubspec.yaml`
2. Run `flutter pub get`
3. Run:
   ```powershell
   flutter run
   ```
4. Update backend URL in `api_service.dart` if needed.

---

## License

MIT
