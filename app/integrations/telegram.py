import os
from typing import Any

from aiogram import Bot


class TelegramService:
    """Gestiona la integración de Telegram de NEXO OS."""

    def __init__(self, token: str | None = None):
        self.token = token or os.getenv("TELEGRAM_BOT_TOKEN", "").strip()

    def is_configured(self) -> bool:
        """Comprueba si Telegram está configurado."""
        return bool(self.token)

    def status(self) -> dict[str, Any]:
        """Devuelve el estado de la integración."""
        return {
            "service": "telegram",
            "configured": self.is_configured(),
        }

    def create_bot(self) -> Bot:
        """Crea la instancia del bot de Telegram."""
        if not self.is_configured():
            raise RuntimeError(
                "TELEGRAM_BOT_TOKEN no está configurado."
            )

        return Bot(token=self.token)


telegram_service = TelegramService()
