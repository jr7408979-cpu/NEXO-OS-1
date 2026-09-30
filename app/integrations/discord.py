import os
from typing import Any

import discord


class DiscordService:
    """Gestiona la integración de Discord de NEXO OS."""

    def __init__(self, token: str | None = None):
        self.token = token or os.getenv("DISCORD_BOT_TOKEN", "").strip()

    def is_configured(self) -> bool:
        """Comprueba si Discord está configurado."""
        return bool(self.token)

    def status(self) -> dict[str, Any]:
        """Devuelve el estado de la integración."""
        return {
            "service": "discord",
            "configured": self.is_configured(),
        }

    def create_client(self) -> discord.Client:
        """Crea el cliente de Discord."""
        if not self.is_configured():
            raise RuntimeError(
                "DISCORD_BOT_TOKEN no está configurado."
            )

        intents = discord.Intents.default()
        intents.message_content = True

        return discord.Client(intents=intents)


discord_service = DiscordService()
