class HealthRegistry:
    def __init__(self):
        self._services = {}

    def update(self, service: str, status: str):
        self._services[service] = status

    def get(self, service: str) -> str:
        return self._services.get(service, "unknown")

    def all(self) -> dict:
        return self._services.copy()
