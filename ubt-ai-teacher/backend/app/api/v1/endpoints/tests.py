from fastapi import APIRouter

from ....schemas.test import GeneratedTest, SubmitAnswer, TestResult
from ....services.tests import generate_test, grade_test

router = APIRouter()


@router.post("/generate", response_model=GeneratedTest)
def generate(title: str = "Бастауыш тест", difficulty: str = "орта", student_id: str | None = None):
    return generate_test(title=title, difficulty=difficulty, student_id=student_id)


@router.post("/grade", response_model=TestResult)
def grade(req: SubmitAnswer):
    return grade_test(test_id=req.test_id, answers=req.answers)
