from fastapi import APIRouter

from ....schemas.explain import ExplainRequest, ExplainResponse
from ....services.explain import generate_explanation

router = APIRouter()


@router.post("/solve", response_model=ExplainResponse)
async def agent_solve(req: ExplainRequest):
    # For MVP, reuse explanation service; later extend with steps/visuals
    content = await generate_explanation(req.topic, req.difficulty, req.student_id)
    return ExplainResponse(content=content, difficulty=req.difficulty)
