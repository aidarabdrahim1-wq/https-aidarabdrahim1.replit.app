from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class StudentProfile(BaseModel):
    student_name: str = Field(..., description="Student's name")
    level: str = Field("орташа", description="Level: бастауыш/орташа/жоғары")
    interests: List[str] = Field(default_factory=list)
    learning_style: str = Field("аралас", description="визуалды/аудио/практика/аралас")
    weak_topics: List[str] = Field(default_factory=list)
    strong_topics: List[str] = Field(default_factory=list)
    preferred_language: str = Field("қазақша")


class StudentProfileUpdate(BaseModel):
    student_name: Optional[str] = None
    level: Optional[str] = None
    interests: Optional[List[str]] = None
    learning_style: Optional[str] = None
    weak_topics: Optional[List[str]] = None
    strong_topics: Optional[List[str]] = None
    preferred_language: Optional[str] = None


class StudentProfileResponse(StudentProfile):
    id: str
