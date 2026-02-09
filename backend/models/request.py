from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    user_id: str = Field(..., example="user123")
    mode: str = Field(..., example="daily", regex="^(daily|interview|travel)$")
    message: str = Field(..., example="I want go to market")
