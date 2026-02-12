import pytest
from models.request import ChatRequest
from models.response import ChatResponse


def test_chat_request_valid():
    """Test valid ChatRequest creation"""
    request = ChatRequest(user_id="user123", mode="daily", message="Hello")
    assert request.user_id == "user123"
    assert request.mode == "daily"
    assert request.message == "Hello"


def test_chat_request_invalid_mode():
    """Test ChatRequest with invalid mode"""
    with pytest.raises(ValueError):
        ChatRequest(user_id="user123", mode="invalid", message="Hello")


def test_chat_request_missing_fields():
    """Test ChatRequest with missing required fields"""
    with pytest.raises(ValueError):
        ChatRequest(user_id="user123", mode="daily")  # missing message


def test_chat_response_creation():
    """Test ChatResponse creation"""
    response = ChatResponse(
        corrected="I want to go to market",
        explanation_id="Koreksi: 'want go' -> 'want to go'",
        tip="Gunakan 'to' setelah 'want' untuk infinitive verb",
        reply="Sure, let's talk about going to the market!"
    )
    assert response.corrected == "I want to go to market"
    assert response.explanation_id == "Koreksi: 'want go' -> 'want to go'"
    assert response.tip == "Gunakan 'to' setelah 'want' untuk infinitive verb"
    assert response.reply == "Sure, let's talk about going to the market!"


def test_chat_response_empty():
    """Test ChatResponse with empty fields"""
    response = ChatResponse(corrected="", explanation_id="", tip="", reply="Hello!")
    assert response.corrected == ""
    assert response.explanation_id == ""
    assert response.tip == ""
    assert response.reply == "Hello!"
