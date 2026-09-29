from collections import deque


class NexoQueue:
    def __init__(self):
        self._queue = deque()

    def push(self, item):
        self._queue.append(item)

    def pop(self):
        if not self._queue:
            return None

        return self._queue.popleft()

    def size(self) -> int:
        return len(self._queue)

    def clear(self):
        self._queue.clear()
