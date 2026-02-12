import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app
from models.request import ChatRequest


def test_chat_endpoint_success():
    """Test successful chat endpoint with mocked AI service"""
    # Mock the AI service to avoid real API calls
    from models.response import ChatResponse

    async def mock_get_ai_response(request):
        return ChatResponse(
            corrected="I want to go to the market",
            explanation_id="Koreksi: 'want go' -> 'want to go'",
            tip="Gunakan 'to' setelah 'want'",
            reply="Sure, let's talk about going to the market!"
        )

    with patch("main.get_ai_response", side_effect=mock_get_ai_response):
        client = TestClient(app)
        request_data = {
            "user_id": "user123",
            "mode": "daily",
            "message": "I want go to market"
        }

        response = client.post("/chat", json=request_data)
        assert response.status_code == 200

        data = response.json()
        assert "corrected" in data
        assert "explanation_id" in data
        assert "tip" in data
        assert "reply" in data
        assert data["corrected"] == "I want to go to the market"


def test_chat_endpoint_invalid_request():
    """Test chat endpoint with invalid request data"""
    client = TestClient(app)
    request_data = {
        "user_id": "user123",
        "mode": "invalid_mode",  # Invalid mode
        "message": "Hello"
    }

    response = client.post("/chat", json=request_data)
    assert response.status_code == 422  # Validation error


def test_chat_endpoint_missing_fields():
    """Test chat endpoint with missing required fields"""
    client = TestClient(app)
    request_data = {
        "user_id": "user123",
        "mode": "daily"
        # Missing message
    }

    response = client.post("/chat", json=request_data)
    assert response.status_code == 422  # Validation error


def test_cors_headers():
    """Test CORS headers are set correctly"""
    client = TestClient(app)
    response = client.options("/chat", headers={
        "Origin": "http://localhost:3000",
        "Access-Control-Request-Method": "POST"
    })
    assert response.status_code == 200
    assert "access-control-allow-origin" in response.headers
    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"


def test_chat_endpoint_with_different_modes():
    """Test chat endpoint with different modes"""
    import services.ai_service as ai_service
    original_get_ai_response = ai_service.get_ai_response

    async def mock_get_ai_response(request):
        from models.response import ChatResponse
        mode_suffix = " (interview)" if request.mode == "interview" else " (travel)" if request.mode == "travel" else ""
        return ChatResponse(
            corrected="",
            explanation_id="",
            tip="",
            reply=f"Hello{request.mode}!"
        )

    ai_service.get_ai_response = mock_get_ai_response

    try:
        client = TestClient(app)
        for mode in ["daily", "interview", "travel"]:
            request_data = {
                "user_id": "user123",
                "mode": mode,
                "message": "Hello"
            }

            response = client.post("/chat", json=request_data)
            assert response.status_code == 200
    finally:
        # Restore original function
        ai_service.get_ai_response = original_get_ai_response
