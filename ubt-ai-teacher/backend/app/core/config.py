from __future__ import annotations
from typing import List, Optional
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = "development"
    ai_provider: str = "fallback"  # options: fallback, openai, anthropic, google

    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    google_api_key: Optional[str] = None

    cors_origins: List[str] = ["*"]

    data_dir: str = "app/data"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="UBT_", extra="ignore")

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors(cls, v):  # type: ignore[no-untyped-def]
        if isinstance(v, str):
            return [s.strip() for s in v.split(",") if s.strip()]
        return v


settings = Settings()  # type: ignore[call-arg]
