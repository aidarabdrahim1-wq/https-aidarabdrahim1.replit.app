from __future__ import annotations
from typing import List, Optional
from uuid import uuid4

from ..schemas.test import GeneratedTest, Question, TestResult
from ..services.memory import store


EXAMPLE_QUESTIONS = [
    Question(
        id="q1",
        text="1) 2 + 2 = ?",
        options=["3", "4", "5", "6"],
        correct_index=1,
        explanation="Қарапайым қосу: 2+2=4",
    ),
    Question(
        id="q2",
        text="2) Қазақстан астанасы?",
        options=["Алматы", "Шымкент", "Астана", "Қарағанды"],
        correct_index=2,
        explanation="Астана (қазіргі: Астана)",
    ),
]


def generate_test(title: str, difficulty: str = "орта", student_id: Optional[str] = None) -> GeneratedTest:
    # For MVP, return a fixed set. Later, adapt by student profile and difficulty
    test_id = uuid4().hex
    return GeneratedTest(id=test_id, title=title, questions=EXAMPLE_QUESTIONS, difficulty=difficulty)


def grade_test(test_id: str, answers: List[int]) -> TestResult:
    return grade_test_result(test_id=test_id, answers=answers)


def grade_test_result(test_id: str, answers: List[int]) -> TestResult:
    total = len(EXAMPLE_QUESTIONS)
    correct = 0
    for idx, q in enumerate(EXAMPLE_QUESTIONS):
        if idx < len(answers) and answers[idx] == q.correct_index:
            correct += 1
    score = (correct / total) * 100 if total else 0.0
    feedback = "Жарайсың!" if score >= 80 else "Тырыс! Келесі жолы жақсырақ болады."
    return TestResult(test_id=test_id, score=score, correct_count=correct, total=total, feedback=feedback)
