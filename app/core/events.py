from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class NexoEvent:
    event_type: str
    source: str
    data: dict
    created_at: str


def create_event(event_type: str, source: str, data: dict) -> NexoEvent:
    return NexoEvent(
        event_type=event_type,
        source=source,
        data=data,
        created_at=datetime.now(timezone.utc).isoformat(),
    )
