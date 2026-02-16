from pydantic import BaseModel

class ChatResponse(BaseModel):
    corrected: str
    explanation_id: str
    tip: str
    reply: str
