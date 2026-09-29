class DependencyManager:
    def __init__(self):
        self.dependencies = {}

    def register(self, service: str, dependencies: list[str]):
        self.dependencies[service] = dependencies

    def get(self, service: str) -> list[str]:
        return self.dependencies.get(service, [])

    def check(self, service: str, available: set[str]) -> bool:
        return all(
            dependency in available
            for dependency in self.get(service)
        )
