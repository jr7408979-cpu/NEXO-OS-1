from datetime import datetime, timezone
from typing import Any


class EventStore:
    """Almacena eventos internos de NEXO OS."""

    def __init__(self) -> None:
        self._events: list[dict[str, Any]] = []

    def add(
        self,
        event_type: str,
        data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Guarda un evento."""
        event = {
            "type": event_type,
            "data": data or {},
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        self._events.append(event)
        return event

    def get_all(self) -> list[dict[str, Any]]:
        """Devuelve todos los eventos."""
        return list(self._events)

    def get_by_type(self, event_type: str) -> list[dict[str, Any]]:
        """Devuelve eventos de un tipo específico."""
        return [
            event
            for event in self._events
            if event["type"] == event_type
        ]

    def clear(self) -> None:
        """Limpia los eventos almacenados."""
        self._events.clear()


event_store = EventStore()
