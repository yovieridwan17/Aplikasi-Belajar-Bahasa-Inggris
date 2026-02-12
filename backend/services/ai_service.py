import os
import google.generativeai as genai
from models.request import ChatRequest
from models.response import ChatResponse

GEMINI_API_KEY = "AIzaSyDe5wxZ7yLFrBzbmy5d4u7afbRCHtR2pPs"  # Provided Gemini API key

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

SYSTEM_PROMPT = (
    "You are a friendly English tutor for Indonesian learners. "
    "Correct the user's grammar, explain mistakes in Indonesian, provide a better sentence, "
    "and continue the conversation naturally. Keep responses short and encouraging. "
    "Respond in JSON format with keys: corrected, explanation_id, tip, reply."
)

async def get_ai_response(request: ChatRequest) -> ChatResponse:
    user_message = request.message
    mode = request.mode

    system_prompt = SYSTEM_PROMPT
    if mode == "interview":
        system_prompt += " Focus on job interview English."
    elif mode == "travel":
        system_prompt += " Focus on travel English."

    prompt = f"{system_prompt}\n\nUser message: {user_message}"

    try:
        response = model.generate_content(prompt)
        ai_content = response.text.strip()

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
    except Exception as e:
        return ChatResponse(
            corrected="",
            explanation_id="Error",
            tip="",
            reply=f"Sorry, there was an error: {str(e)}"
        )
