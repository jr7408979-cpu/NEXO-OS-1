from datetime import datetime, timezone
from typing import Any


class ClientRegistry:
    """Gestiona los clientes registrados en NEXO OS."""

    def __init__(self) -> None:
        self._clients: dict[str, dict[str, Any]] = {}

    def register(self, client_id: str, name: str = "") -> dict[str, Any]:
        """Registra un cliente nuevo."""
        if not client_id.strip():
            raise ValueError("El ID del cliente no puede estar vacío.")

        if client_id in self._clients:
            raise ValueError(f"El cliente ya existe: {client_id}")

        client = {
            "id": client_id,
            "name": name,
            "plan": "free",
            "status": "active",
            "created_at": datetime.now(timezone.utc).isoformat(),
        }

        self._clients[client_id] = client
        return client

    def get(self, client_id: str) -> dict[str, Any] | None:
        """Obtiene un cliente."""
        return self._clients.get(client_id)

    def update(self, client_id: str, **fields: Any) -> dict[str, Any]:
        """Actualiza información de un cliente."""
        client = self._clients.get(client_id)

        if client is None:
            raise ValueError(f"Cliente no encontrado: {client_id}")

        client.update(fields)
        client["updated_at"] = datetime.now(timezone.utc).isoformat()

        return client

    def remove(self, client_id: str) -> None:
        """Elimina un cliente."""
        self._clients.pop(client_id, None)

    def list_clients(self) -> list[dict[str, Any]]:
        """Lista todos los clientes."""
        return list(self._clients.values())


client_registry = ClientRegistry()
