import os
from typing import Any


class PayPalService:
    """Gestiona la integración de PayPal de NEXO OS."""

    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
    ):
        self.client_id = (
            client_id
            or os.getenv("PAYPAL_CLIENT_ID", "").strip()
        )
        self.client_secret = (
            client_secret
            or os.getenv("PAYPAL_CLIENT_SECRET", "").strip()
        )

    def is_configured(self) -> bool:
        """Comprueba si PayPal está configurado."""
        return bool(self.client_id and self.client_secret)

    def status(self) -> dict[str, Any]:
        """Devuelve el estado de la integración."""
        return {
            "service": "paypal",
            "configured": self.is_configured(),
        }


paypal_service = PayPalService()
