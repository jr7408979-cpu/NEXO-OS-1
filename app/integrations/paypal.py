class PayPalService:
    def __init__(self, client_id: str | None = None):
        self.client_id = client_id

    def is_configured(self) -> bool:
        return bool(self.client_id)

    def status(self) -> dict:
        return {
            "service": "paypal",
            "configured": self.is_configured(),
        }
