from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import settings
from .api.v1.routes import api_router

app = FastAPI(title="UBT AI Teacher", version="0.1.0")

# CORS
origins = settings.cors_origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "UBT AI Teacher backend is running", "version": app.version}
