class TelegramService:
    def __init__(self, token: str | None = None):
        self.token = token

    def is_configured(self) -> bool:
        return bool(self.token)

    def status(self) -> dict:
        return {
            "service": "telegram",
            "configured": self.is_configured(),
        }
