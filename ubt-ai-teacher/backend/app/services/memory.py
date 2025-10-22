from __future__ import annotations
from typing import Dict, Optional
from uuid import uuid4

from ..schemas.student import StudentProfile, StudentProfileUpdate, StudentProfileResponse


class InMemoryStore:
    def __init__(self) -> None:
        self._students: Dict[str, StudentProfile] = {}

    def create_student(self, profile: StudentProfile) -> StudentProfileResponse:
        student_id = uuid4().hex
        self._students[student_id] = profile
        return StudentProfileResponse(id=student_id, **profile.model_dump())

    def get_student(self, student_id: str) -> Optional[StudentProfileResponse]:
        profile = self._students.get(student_id)
        if not profile:
            return None
        return StudentProfileResponse(id=student_id, **profile.model_dump())

    def update_student(self, student_id: str, update: StudentProfileUpdate) -> Optional[StudentProfileResponse]:
        existing = self._students.get(student_id)
        if not existing:
            return None
        new_data = existing.model_dump()
        for k, v in update.model_dump(exclude_unset=True).items():
            new_data[k] = v
        new_profile = StudentProfile(**new_data)
        self._students[student_id] = new_profile
        return StudentProfileResponse(id=student_id, **new_profile.model_dump())

    def list_students(self):
        return [StudentProfileResponse(id=sid, **p.model_dump()) for sid, p in self._students.items()]


store = InMemoryStore()
