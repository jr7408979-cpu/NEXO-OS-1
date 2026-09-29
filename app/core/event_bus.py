from collections import defaultdict
from typing import Callable


class EventBus:
    def __init__(self):
        self._handlers = defaultdict(list)

    def subscribe(self, event_type: str, handler: Callable):
        self._handlers[event_type].append(handler)

    def publish(self, event_type: str, data: dict | None = None):
        for handler in self._handlers[event_type]:
            handler(data or {})
