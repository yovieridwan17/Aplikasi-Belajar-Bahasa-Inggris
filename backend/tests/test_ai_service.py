import pytest
from unittest.mock import AsyncMock, patch
from models.request import ChatRequest
from models.response import ChatResponse
from services.ai_service import get_ai_response


@pytest.mark.asyncio
async def test_get_ai_response_daily_mode():
    """Test AI response for daily mode"""
    request = ChatRequest(user_id="user123", mode="daily", message="I want go to market")

    # Mock the httpx client
    mock_response_data = {
        "choices": [
            {
                "message": {
                    "content": '{"corrected": "I want to go to the market", "explanation_id": "Koreksi: want go -> want to go", "tip": "Gunakan to setelah want", "reply": "Sure, let\'s talk about the market!"}'
                }
            }
        ]
    }

    with patch("services.ai_service.httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.post.return_value.__aenter__.return_value.raise_for_status.return_value = None
        mock_instance.post.return_value.__aenter__.return_value.json.return_value = mock_response_data
        mock_client.return_value = mock_instance

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

    mock_response_data = {
        "choices": [
            {
                "message": {
                    "content": '{"corrected": "", "explanation_id": "", "tip": "", "reply": "Sure, I can help with interview practice!"}'
                }
            }
        ]
    }

    with patch("services.ai_service.httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.post.return_value.__aenter__.return_value.raise_for_status.return_value = None
        mock_instance.post.return_value.__aenter__.return_value.json.return_value = mock_response_data
        mock_client.return_value = mock_instance

        response = await get_ai_response(request)

        assert isinstance(response, ChatResponse)
        assert response.reply == "Sure, I can help with interview practice!"


@pytest.mark.asyncio
async def test_get_ai_response_travel_mode():
    """Test AI response for travel mode"""
    request = ChatRequest(user_id="user123", mode="travel", message="How to ask for directions")

    mock_response_data = {
        "choices": [
            {
                "message": {
                    "content": '{"corrected": "", "explanation_id": "", "tip": "", "reply": "Great question for travel!"}'
                }
            }
        ]
    }

    with patch("services.ai_service.httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.post.return_value.__aenter__.return_value.raise_for_status.return_value = None
        mock_instance.post.return_value.__aenter__.return_value.json.return_value = mock_response_data
        mock_client.return_value = mock_instance

        response = await get_ai_response(request)

        assert isinstance(response, ChatResponse)
        assert response.reply == "Great question for travel!"


@pytest.mark.asyncio
async def test_get_ai_response_non_json_reply():
    """Test AI response when AI returns plain text instead of JSON"""
    request = ChatRequest(user_id="user123", mode="daily", message="Hello")

    mock_response_data = {
        "choices": [
            {
                "message": {
                    "content": "Hello! How can I help you learn English today?"
                }
            }
        ]
    }

    with patch("services.ai_service.httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.post.return_value.__aenter__.return_value.raise_for_status.return_value = None
        mock_instance.post.return_value.__aenter__.return_value.json.return_value = mock_response_data
        mock_client.return_value = mock_instance

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

    with patch("services.ai_service.httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.post.return_value.__aenter__.return_value.raise_for_status.side_effect = Exception("API Error")
        mock_client.return_value = mock_instance

        with pytest.raises(Exception):
            await get_ai_response(request)
