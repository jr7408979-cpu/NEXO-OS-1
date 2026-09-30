from datetime import datetime, timezone
from typing import Any


class UserRegistry:
    """Gestiona los usuarios registrados en NEXO OS."""

    def __init__(self) -> None:
        self._users: dict[str, dict[str, Any]] = {}

    def register(
        self,
        user_id: str,
        name: str = "",
    ) -> dict[str, Any]:
        """Registra un usuario nuevo."""
        if not user_id.strip():
            raise ValueError("El ID del usuario no puede estar vacío.")

        if user_id in self._users:
            raise ValueError(f"El usuario ya existe: {user_id}")

        user = {
            "id": user_id,
            "name": name,
            "status": "active",
            "created_at": datetime.now(timezone.utc).isoformat(),
        }

        self._users[user_id] = user
        return user

    def get(self, user_id: str) -> dict[str, Any] | None:
        """Obtiene un usuario."""
        return self._users.get(user_id)

    def update(self, user_id: str, **fields: Any) -> dict[str, Any]:
        """Actualiza información de un usuario."""
        user = self._users.get(user_id)

        if user is None:
            raise ValueError(f"Usuario no encontrado: {user_id}")

        user.update(fields)
        user["updated_at"] = datetime.now(timezone.utc).isoformat()

        return user

    def remove(self, user_id: str) -> None:
        """Elimina un usuario."""
        self._users.pop(user_id, None)

    def list_users(self) -> list[dict[str, Any]]:
        """Lista todos los usuarios."""
        return list(self._users.values())


user_registry = UserRegistry()
