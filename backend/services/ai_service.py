import os
import httpx
from models.request import ChatRequest
from models.response import ChatResponse

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = os.getenv("OPENAI_API_URL", "https://api.openai.com/v1/chat/completions")

SYSTEM_PROMPT = (
    "You are a friendly English tutor for Indonesian learners. "
    "Correct the user's grammar, explain mistakes in Indonesian, provide a better sentence, "
    "and continue the conversation naturally. Keep responses short and encouraging."
)

async def get_ai_response(request: ChatRequest) -> ChatResponse:
    user_message = request.message
    mode = request.mode

    system_prompt = SYSTEM_PROMPT
    if mode == "interview":
        system_prompt += " Focus on job interview English."
    elif mode == "travel":
        system_prompt += " Focus on travel English."

    prompt = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": prompt,
        "max_tokens": 256,
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(OPENAI_API_URL, headers=headers, json=data, timeout=30)
        resp.raise_for_status()
        ai_content = resp.json()["choices"][0]["message"]["content"]

    import json
    try:
        ai_json = json.loads(ai_content)
        return ChatResponse(**ai_json)
    except Exception:
        return ChatResponse(
            corrected="",
            explanation_id="",
            tip="",
            reply=ai_content
        )
