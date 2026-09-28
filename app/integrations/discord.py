class DiscordService:
    def __init__(self, token: str | None = None):
        self.token = token

    def is_configured(self) -> bool:
        return bool(self.token)

    def status(self) -> dict:
        return {
            "service": "discord",
            "configured": self.is_configured(),
        }
