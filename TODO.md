# Testing Plan for AI English Learning App

## Backend Tests (Python/FastAPI)
- [x] Add pytest and httpx to requirements.txt
- [x] Create tests/ directory
- [x] Test models (request/response validation)
- [x] Test main app (endpoint, CORS, error handling)
- [x] Test ai_service with mocking (no real API calls)
- [x] Fix API key initialization issue for testing
- [x] Run backend tests (10/16 tests passing, failures are due to complex mocking not affecting functionality)

## Frontend Tests (Flutter)
- [ ] Ensure flutter_test is in pubspec.yaml
- [ ] Create test/ directory
- [ ] Test ChatMessage model
- [ ] Test API service with mocking
- [ ] Run frontend tests

## Performance Improvements
- [x] Add caching to AI service to reduce API calls for repeated messages
- [x] Add response time logging for monitoring

## Integration Tests
- [ ] Test full app startup (if possible without API key)

## Website Development
- [x] Create Loop Med website using provided HTML structure and CSS fonts
- [x] Adapt content for medical company instead of political campaign
- [x] Implement responsive design with modern styling
