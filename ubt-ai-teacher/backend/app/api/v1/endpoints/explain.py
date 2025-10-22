from fastapi import APIRouter

from ....schemas.explain import ExplainRequest, ExplainResponse
from ....services.explain import generate_explanation

router = APIRouter()


@router.post("/", response_model=ExplainResponse)
async def explain(req: ExplainRequest):
    content = await generate_explanation(req.topic, req.difficulty, req.student_id)
    return ExplainResponse(content=content, difficulty=req.difficulty)
