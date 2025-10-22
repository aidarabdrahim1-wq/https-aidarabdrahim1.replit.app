from fastapi import APIRouter, HTTPException

from ....schemas.student import StudentProfile, StudentProfileUpdate, StudentProfileResponse
from ....services.memory import store

router = APIRouter()


@router.get("/")
def list_students():
    return store.list_students()


@router.post("/", response_model=StudentProfileResponse)
def create_student(profile: StudentProfile):
    return store.create_student(profile)


@router.get("/{student_id}", response_model=StudentProfileResponse)
def get_student(student_id: str):
    profile = store.get_student(student_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Student not found")
    return profile


@router.patch("/{student_id}", response_model=StudentProfileResponse)
def update_student(student_id: str, update: StudentProfileUpdate):
    profile = store.update_student(student_id, update)
    if not profile:
        raise HTTPException(status_code=404, detail="Student not found")
    return profile
