import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from models.request import ChatRequest
from models.response import ChatResponse
from services.ai_service import get_ai_response, response_cache


@pytest.fixture(autouse=True)
def clear_cache():
    """Clear the response cache and reset client before each test"""
    response_cache.clear()
    import services.ai_service as ai_service
    ai_service.client = None
    yield
    response_cache.clear()
    ai_service.client = None


@pytest.fixture
def mock_groq_client():
    """Fixture to provide a mocked Groq client"""
    with patch("services.ai_service.os.getenv", return_value="fake_key"), patch("services.ai_service.Groq") as mock_groq:
        mock_client = MagicMock()
        mock_groq.return_value = mock_client
        yield mock_client


@pytest.mark.asyncio
async def test_get_ai_response_daily_mode():
    """Test AI response for daily mode"""
    request = ChatRequest(user_id="user123", mode="daily", message="I want go to market")

    # Mock the Groq client response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = '{"corrected": "I want to go to the market", "explanation_id": "Koreksi: want go -> want to go", "tip": "Gunakan to setelah want", "reply": "Sure, let\'s talk about the market!"}'

    with patch("services.ai_service.os.getenv", return_value="fake_key"), patch("services.ai_service.Groq") as mock_groq, patch("services.ai_service.response_cache", {}):
        mock_client = MagicMock()
        mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
        mock_groq.return_value = mock_client

        response = await get_ai_response(request)

        assert isinstance(response, ChatResponse)
        assert response.corrected == "I want to go to the market"
        assert response.explanation_id == "Koreksi: want go -> want to go"
        assert response.tip == "Gunakan to setelah want"
        assert response.reply == "Sure, let's talk about the market!"


@pytest.mark.asyncio
async def test_get_ai_response_interview_mode():
    """Test AI response for interview mode"""
    request = ChatRequest(user_id="user123", mode="interview", message="Tell me about yourself")

    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = '{"corrected": "", "explanation_id": "", "tip": "", "reply": "Sure, I can help with interview practice!"}'

    with patch("services.ai_service.os.getenv", return_value="fake_key"), patch("services.ai_service.Groq") as mock_groq:
        mock_client = MagicMock()
        mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
        mock_groq.return_value = mock_client

        response = await get_ai_response(request)

        assert isinstance(response, ChatResponse)
        assert response.reply == "Sure, I can help with interview practice!"


@pytest.mark.asyncio
async def test_get_ai_response_travel_mode():
    """Test AI response for travel mode"""
    request = ChatRequest(user_id="user123", mode="travel", message="How to ask for directions")

    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = '{"corrected": "", "explanation_id": "", "tip": "", "reply": "Great question for travel!"}'

    with patch("services.ai_service.os.getenv", return_value="fake_key"), patch("services.ai_service.Groq") as mock_groq:
        mock_client = MagicMock()
        mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
        mock_groq.return_value = mock_client

        response = await get_ai_response(request)

        assert isinstance(response, ChatResponse)
        assert response.reply == "Great question for travel!"


@pytest.mark.asyncio
async def test_get_ai_response_non_json_reply():
    """Test AI response when AI returns plain text instead of JSON"""
    request = ChatRequest(user_id="user123", mode="daily", message="Hello")

    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Hello! How can I help you learn English today?"

    with patch("services.ai_service.os.getenv", return_value="fake_key"), patch("services.ai_service.Groq") as mock_groq:
        mock_client = MagicMock()
        mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
        mock_groq.return_value = mock_client

        response = await get_ai_response(request)

        assert isinstance(response, ChatResponse)
        assert response.corrected == ""
        assert response.explanation_id == ""
        assert response.tip == ""
        assert response.reply == "Hello! How can I help you learn English today?"


@pytest.mark.asyncio
async def test_get_ai_response_api_error():
    """Test AI response when API call fails"""
    request = ChatRequest(user_id="user123", mode="daily", message="Hello")

    with patch("services.ai_service.os.getenv", return_value="fake_key"), patch("services.ai_service.Groq") as mock_groq:
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        mock_groq.return_value = mock_client

        response = await get_ai_response(request)

        assert isinstance(response, ChatResponse)
        assert response.explanation_id == "Error"
        assert "API Error" in response.reply


@pytest.mark.asyncio
async def test_get_ai_response_cache_hit():
    """Test that repeated messages use cache"""
    request = ChatRequest(user_id="user123", mode="daily", message="Hello")

    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = '{"corrected": "", "explanation_id": "", "tip": "", "reply": "Hello back!"}'

    with patch("services.ai_service.os.getenv", return_value="fake_key"), patch("services.ai_service.Groq") as mock_groq, patch("services.ai_service.response_cache", {}):
        mock_client = MagicMock()
        mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
        mock_groq.return_value = mock_client

        # First call should hit API
        response1 = await get_ai_response(request)
        # Second call should hit cache
        response2 = await get_ai_response(request)

        # Should only call API once
        assert mock_client.chat.completions.create.call_count == 1
        assert response1.reply == "Hello back!"
        assert response2.reply == "Hello back!"
