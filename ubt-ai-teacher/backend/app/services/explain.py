from __future__ import annotations
from typing import Optional

from ..core.rules import build_system_prompt
from ..providers.ai import get_provider
from ..services.memory import store


async def generate_explanation(topic: str, difficulty: str, student_id: Optional[str] = None) -> str:
    student_profile = None
    if student_id:
        student_profile = store.get_student(student_id)
        if student_profile:
            student_profile = student_profile.model_dump()
    system = build_system_prompt(student_profile)

    # Structure the user prompt to enforce 3 levels
    user = (
        f"Тақырып: {topic}. Күрделілік: {difficulty}.\n"
        "Түсіндір: 1) Қарапайым тілмен 2) Мысалдармен 3) Ғылыми терминдермен.\n"
        "Егер мүмкін болса, студент қызығушылықтарына бейімде."
    )

    provider = get_provider()
    return await provider.chat(system=system, user=user)
