from datetime import date
from typing import Any


class UsageManager:
    """Controla el uso diario de cada usuario."""

    def __init__(self) -> None:
        self._usage: dict[str, dict[str, Any]] = {}

    def _ensure_user(self, user_id: str) -> dict[str, Any]:
        today = date.today().isoformat()

        user_usage = self._usage.get(user_id)

        if user_usage is None or user_usage["date"] != today:
            user_usage = {
                "date": today,
                "count": 0,
            }
            self._usage[user_id] = user_usage

        return user_usage

    def get_usage(self, user_id: str) -> dict[str, Any]:
        """Obtiene el uso actual del usuario."""
        return dict(self._ensure_user(user_id))

    def increment(self, user_id: str, amount: int = 1) -> dict[str, Any]:
        """Incrementa el uso del usuario."""
        if amount < 1:
            raise ValueError("El incremento debe ser mayor que cero.")

        usage = self._ensure_user(user_id)
        usage["count"] += amount

        return dict(usage)

    def can_use(self, user_id: str, daily_limit: int) -> bool:
        """Comprueba si el usuario puede realizar otra acción."""
        if daily_limit < 0:
            raise ValueError("El límite diario no puede ser negativo.")

        usage = self._ensure_user(user_id)
        return usage["count"] < daily_limit

    def reset(self, user_id: str) -> None:
        """Reinicia el contador del usuario."""
        self._usage.pop(user_id, None)


usage_manager = UsageManager()
