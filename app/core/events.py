from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class NexoEvent:
    """Representa un evento interno de NEXO OS."""

    event_type: str
    source: str
    data: dict[str, Any]
    created_at: str


def create_event(
    event_type: str,
    source: str,
    data: dict[str, Any] | None = None,
) -> NexoEvent:
    """Crea un evento nuevo."""

    if not event_type.strip():
        raise ValueError(
            "El tipo de evento no puede estar vacío."
        )

    if not source.strip():
        raise ValueError(
            "La fuente del evento no puede estar vacía."
        )

    return NexoEvent(
        event_type=event_type,
        source=source,
        data=data or {},
        created_at=datetime.now(timezone.utc).isoformat(),
    )
