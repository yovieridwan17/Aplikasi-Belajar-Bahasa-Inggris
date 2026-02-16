from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional


# Auth Requests
class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    username: str
    password: str


# Exercise Requests
class ExerciseSubmit(BaseModel):
    lesson_id: int
    answers: List[dict]  # [{"question_id": 1, "answer": "answer"}]


# Progress Requests
class ProgressReset(BaseModel):
