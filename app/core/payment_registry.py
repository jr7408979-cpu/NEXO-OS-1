from datetime import datetime, timezone
from typing import Any


class PaymentRegistry:
    """Registra los pagos asociados a los usuarios."""

    def __init__(self) -> None:
        self._payments: list[dict[str, Any]] = []

    def record(
        self,
        user_id: str,
        amount: float,
        currency: str = "USD",
        provider: str = "paypal",
        transaction_id: str = "",
    ) -> dict[str, Any]:
        """Registra un pago."""
        if not user_id.strip():
            raise ValueError("El ID del usuario no puede estar vacío.")

        if amount <= 0:
            raise ValueError("El monto debe ser mayor que cero.")

        payment = {
            "user_id": user_id,
            "amount": amount,
            "currency": currency,
            "provider": provider,
            "transaction_id": transaction_id,
            "status": "recorded",
            "created_at": datetime.now(timezone.utc).isoformat(),
        }

        self._payments.append(payment)
        return payment

    def get_user_payments(self, user_id: str) -> list[dict[str, Any]]:
        """Devuelve los pagos de un usuario."""
        return [
            payment
            for payment in self._payments
            if payment["user_id"] == user_id
        ]

    def list_payments(self) -> list[dict[str, Any]]:
        """Devuelve todos los pagos registrados."""
        return list(self._payments)


payment_registry = PaymentRegistry()
