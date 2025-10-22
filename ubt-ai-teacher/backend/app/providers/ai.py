from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from ..core.config import settings


@dataclass
class AIMessage:
    role: str
    content: str


class AIProvider:
    async def chat(self, system: str, user: str) -> str:  # pragma: no cover - interface
        raise NotImplementedError


class FallbackProvider(AIProvider):
    async def chat(self, system: str, user: str) -> str:
        return (
            "[ЕСКЕРТУ] Нақты AI моделі бапталмаған. Төменде ережелерге сай қарапайым түсіндіру берілді.\n\n"
            f"Сұрақ: {user}\n\n"
            "Жауап: Бұл сұрақты қарапайым тілмен түсіндіріңіз, нақты мысалдармен және ғылыми терминдермен үш деңгейде."
        )


# Placeholders for real providers (not importing heavy SDKs until configured)
class OpenAIProvider(AIProvider):
    async def chat(self, system: str, user: str) -> str:
        return await FallbackProvider().chat(system, user)


class AnthropicProvider(AIProvider):
    async def chat(self, system: str, user: str) -> str:
        return await FallbackProvider().chat(system, user)


class GoogleProvider(AIProvider):
    async def chat(self, system: str, user: str) -> str:
        return await FallbackProvider().chat(system, user)


def get_provider() -> AIProvider:
    provider = settings.ai_provider.lower()
    if provider == "openai" and settings.openai_api_key:
        return OpenAIProvider()
    if provider == "anthropic" and settings.anthropic_api_key:
        return AnthropicProvider()
    if provider == "google" and settings.google_api_key:
        return GoogleProvider()
    return FallbackProvider()
