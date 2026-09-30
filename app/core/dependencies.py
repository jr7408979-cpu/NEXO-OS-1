from typing import Any


class DependencyManager:
    """Gestiona las dependencias entre componentes de NEXO OS."""

    def __init__(self) -> None:
        self.dependencies: dict[str, list[str]] = {}

    def register(
        self,
        service: str,
        dependencies: list[str],
    ) -> None:
        """Registra las dependencias de un servicio."""

        if not service.strip():
            raise ValueError(
                "El nombre del servicio no puede estar vacío."
            )

        cleaned_dependencies = [
            dependency.strip()
            for dependency in dependencies
            if dependency.strip()
        ]

        self.dependencies[service] = cleaned_dependencies

    def get(self, service: str) -> list[str]:
        """Obtiene las dependencias de un servicio."""

        return list(self.dependencies.get(service, []))

    def check(
        self,
        service: str,
        available: set[str],
    ) -> bool:
        """Comprueba si todas las dependencias están disponibles."""

        return all(
            dependency in available
            for dependency in self.get(service)
        )

    def remove(self, service: str) -> None:
        """Elimina un servicio y sus dependencias."""

        self.dependencies.pop(service, None)

    def list_services(self) -> dict[str, list[str]]:
        """Devuelve todas las dependencias registradas."""

        return {
            service: list(dependencies)
            for service, dependencies in self.dependencies.items()
        }


dependency_manager = DependencyManager()
