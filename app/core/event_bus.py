from collections import defaultdict
from typing import Any, Callable


EventHandler = Callable[[dict[str, Any]], Any]


class EventBus:
    """Sistema central de eventos de NEXO OS."""

    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:
        """Suscribe un manejador a un tipo de evento."""

        if not event_type.strip():
            raise ValueError(
                "El tipo de evento no puede estar vacío."
            )

        if not callable(handler):
            raise TypeError(
                "El manejador del evento debe ser ejecutable."
            )

        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(handler)

    def unsubscribe(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:
        """Cancela la suscripción de un manejador."""

        handlers = self._handlers.get(event_type)

        if not handlers:
            return

        if handler in handlers:
            handlers.remove(handler)

        if not handlers:
            self._handlers.pop(event_type, None)

    def publish(
        self,
        event_type: str,
        data: dict[str, Any] | None = None,
    ) -> None:
        """Publica un evento a todos sus manejadores."""

        if not event_type.strip():
            raise ValueError(
                "El tipo de evento no puede estar vacío."
            )

        event_data = data or {}

        for handler in list(self._handlers.get(event_type, [])):
            handler(event_data)

    def has_subscribers(self, event_type: str) -> bool:
        """Comprueba si existen suscriptores para un evento."""

        return bool(self._handlers.get(event_type))

    def clear(self, event_type: str | None = None) -> None:
        """Elimina suscripciones de un evento o de todos."""

        if event_type is None:
            self._handlers.clear()
            return

        self._handlers.pop(event_type, None)
