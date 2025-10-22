from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class Question(BaseModel):
    id: str
    text: str
    options: List[str]
    correct_index: int
    explanation: Optional[str] = None


class GeneratedTest(BaseModel):
    id: str
    title: str
    questions: List[Question]
    difficulty: str = Field("орта")


class SubmitAnswer(BaseModel):
    test_id: str
    answers: List[int]


class TestResult(BaseModel):
    test_id: str
    score: float
    correct_count: int
    total: int
    feedback: str
