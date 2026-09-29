class ServiceRegistry:
    def __init__(self):
        self._services = {}

    def register(self, name: str, service):
        self._services[name] = service

    def get(self, name: str):
        return self._services.get(name)

    def exists(self, name: str) -> bool:
        return name in self._services

    def all(self) -> dict:
        return self._services.copy()
