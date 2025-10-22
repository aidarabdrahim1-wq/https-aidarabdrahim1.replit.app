from fastapi import APIRouter

from .endpoints.health import router as health_router
from .endpoints.students import router as students_router
from .endpoints.explain import router as explain_router
from .endpoints.tests import router as tests_router
from .endpoints.agent import router as agent_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"]) 
api_router.include_router(students_router, prefix="/students", tags=["students"]) 
api_router.include_router(explain_router, prefix="/explain", tags=["explain"]) 
api_router.include_router(tests_router, prefix="/tests", tags=["tests"]) 
api_router.include_router(agent_router, prefix="/agent", tags=["agent"]) 
