from collections import deque
from typing import Any


class NexoQueue:
    """Cola interna de tareas de NEXO OS."""

    def __init__(self) -> None:
        self._queue: deque[Any] = deque()

    def push(self, item: Any) -> None:
        """Añade un elemento al final de la cola."""

        self._queue.append(item)

    def pop(self) -> Any | None:
        """Obtiene y elimina el primer elemento."""

        if not self._queue:
            return None

        return self._queue.popleft()

    def peek(self) -> Any | None:
        """Obtiene el primer elemento sin eliminarlo."""

        if not self._queue:
            return None

        return self._queue[0]

    def size(self) -> int:
        """Devuelve el número de elementos."""

        return len(self._queue)

    def is_empty(self) -> bool:
        """Comprueba si la cola está vacía."""

        return not self._queue

    def clear(self) -> None:
        """Vacía la cola."""

        self._queue.clear()


nexo_queue = NexoQueue()
