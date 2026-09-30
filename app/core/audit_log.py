from datetime import datetime, timezone
from typing import Any


class AuditLog:
    """Registra eventos importantes de NEXO OS."""

    def __init__(self) -> None:
        self._events: list[dict[str, Any]] = []

    def record(
        self,
        event: str,
        actor: str = "system",
        details: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Registra un evento."""
        entry = {
            "event": event,
            "actor": actor,
            "details": details or {},
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        self._events.append(entry)
        return entry

    def list_events(self) -> list[dict[str, Any]]:
        """Devuelve todos los eventos registrados."""
        return list(self._events)

    def clear(self) -> None:
        """Limpia el registro en memoria."""
        self._events.clear()


audit_log = AuditLog()
