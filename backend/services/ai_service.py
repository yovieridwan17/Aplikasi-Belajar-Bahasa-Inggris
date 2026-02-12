import os
import time
import logging
from functools import lru_cache
from groq import Groq
from models.request import ChatRequest
from models.response import ChatResponse

client = None

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a friendly English tutor for Indonesian learners. "
    "Correct the user's grammar, explain mistakes in Indonesian, provide a better sentence, "
    "and continue the conversation naturally. Keep responses short and encouraging. "
    "Respond in JSON format with keys: corrected, explanation_id, tip, reply."
)

# Simple in-memory cache for responses
response_cache = {}

async def get_ai_response(request: ChatRequest) -> ChatResponse:
    global client
    start_time = time.time()
    user_message = request.message
    mode = request.mode

    # Create cache key
    cache_key = f"{mode}:{user_message}"

    # Check cache first
    if cache_key in response_cache:
        logger.info(f"Cache hit for message: '{user_message}' in mode: {mode}")
        response_time = time.time() - start_time
        logger.info(f"Response time (cached): {response_time:.2f}s")
        return response_cache[cache_key]

    # Initialize client if not already done
    if client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if api_key:
            client = Groq(api_key=api_key)
        else:
            # For testing purposes, allow client to be None
            pass

    system_prompt = SYSTEM_PROMPT
    if mode == "interview":
        system_prompt += " Focus on job interview English."
    elif mode == "travel":
        system_prompt += " Focus on travel English."

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    try:
        if client is None:
            raise Exception("GROQ_API_KEY not set")
        response = await client.chat.completions.create(
            model="llama3-8b-8192",  # Free tier model
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )

        ai_content = response.choices[0].message.content.strip()

        import json
        try:
            ai_json = json.loads(ai_content)
            chat_response = ChatResponse(**ai_json)
        except Exception:
            chat_response = ChatResponse(
                corrected="",
                explanation_id="",
                tip="",
                reply=ai_content
            )

        # Cache the response
        response_cache[cache_key] = chat_response
        logger.info(f"Cached response for message: '{user_message}' in mode: {mode}")

        response_time = time.time() - start_time
        logger.info(f"Response time (API): {response_time:.2f}s")

        return chat_response
    except Exception as e:
        response_time = time.time() - start_time
        logger.error(f"Error response time: {response_time:.2f}s - Error: {str(e)}")
        return ChatResponse(
            corrected="",
            explanation_id="Error",
            tip="",
            reply=f"Sorry, there was an error: {str(e)}"
        )
