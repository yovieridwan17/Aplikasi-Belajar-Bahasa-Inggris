# TODO: Transform AI-based English Learning App to Static Content-based App

## Phase 1: Backend Changes

### 1.1 Remove AI Dependencies
- [ ] Remove Groq from requirements.txt
- [ ] Delete backend/services/ai_service.py
- [ ] Update backend/main.py to remove /chat endpoint

### 1.2 Create Database Layer
- [ ] Create backend/database.py (SQLite configuration)
- [ ] Create backend/models/user.py (User model)
- [ ] Create backend/models/content.py (Content/Question models)
- [ ] Create backend/models/progress.py (Progress models)

### 1.3 Create API Routers
- [ ] Create backend/routers/auth.py (Authentication)
- [ ] Create backend/routers/content.py (Content retrieval)
- [ ] Create backend/routers/exercises.py (Exercise handling)
- [ ] Create backend/routers/progress.py (Progress tracking)

### 1.4 Create Static Question Database
- [ ] Create backend/data/questions.py (Question bank with grammar, vocabulary, listening, reading)

### 1.5 Update Existing Models
- [ ] Update backend/models/request.py
- [ ] Update backend/models/response.py

### 1.6 Update Main App
- [ ] Update backend/main.py with new endpoints
- [ ] Update backend/requirements.txt

## Phase 2: Frontend Changes

### 2.1 Update Dependencies
- [ ] Update frontend/pubspec.yaml (add provider, shared_preferences)

### 2.2 Create New Models
- [ ] Create frontend/lib/models/question.dart
- [ ] Create frontend/lib/models/progress.dart
- [ ] Create frontend/lib/models/module.dart

### 2.3 Create New Screens
- [ ] Create frontend/lib/screens/home_screen.dart
- [ ] Create frontend/lib/screens/grammar_screen.dart
- [ ] Create frontend/lib/screens/vocabulary_screen.dart
- [ ] Create frontend/lib/screens/listening_screen.dart
- [ ] Create frontend/lib/screens/reading_screen.dart
- [ ] Create frontend/lib/screens/exercise_screen.dart

### 2.4 Update Existing Files
- [ ] Update frontend/lib/main.dart (new navigation)
- [ ] Update frontend/lib/services/api_service.dart (new endpoints)
- [ ] Remove/backup frontend/lib/screens/chat_screen.dart

## Phase 3: Testing & Cleanup

- [ ] Test all new endpoints
- [ ] Clean up old AI-related test files
- [ ] Verify the app works without AI features
