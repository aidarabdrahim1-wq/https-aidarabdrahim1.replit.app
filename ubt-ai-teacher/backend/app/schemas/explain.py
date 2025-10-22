from __future__ import annotations
from typing import Literal, Optional
from pydantic import BaseModel, Field

Difficulty = Literal["қарапайым", "мысалдар", "ғылыми"]


class ExplainRequest(BaseModel):
    topic: str = Field(..., description="Topic or question")
    difficulty: Difficulty = Field("қарапайым")
    student_id: Optional[str] = Field(None, description="Student profile id to adapt to")


class ExplainResponse(BaseModel):
    content: str
    difficulty: Difficulty
