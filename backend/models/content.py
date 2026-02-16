from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from database import Base


class ModuleType(str, enum.Enum):
    GRAMMAR = "grammar"
    VOCABULARY = "vocabulary"
    LISTENING = "listening"
    READING = "reading"


class QuestionType(str, enum.Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    FILL_BLANK = "fill_blank"
    MATCHING = "matching"


class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    icon = Column(String, default="book")
    module_type = Column(String, nullable=False)  # grammar, vocabulary, listening, reading
    order = Column(Integer, default=0)

    lessons = relationship("Lesson", back_populates="module")


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    order = Column(Integer, default=0)

    module = relationship("Module", back_populates="lessons")
    questions = relationship("Question", back_populates="lesson")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    question_type = Column(String, nullable=False)  # multiple_choice, fill_blank, matching
    question_text = Column(Text, nullable=False)
    options = Column(Text, nullable=True)  # JSON string for multiple choice options
    correct_answer = Column(String, nullable=False)
    explanation = Column(Text, nullable=True)

    lesson = relationship("Lesson", back_populates="questions")
