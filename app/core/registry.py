from typing import Any


class ServiceRegistry:
    """Registro central de servicios de NEXO OS."""

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        """Registra un servicio."""

        if not name.strip():
            raise ValueError(
                "El nombre del servicio no puede estar vacío."
            )

        self._services[name] = service

    def get(self, name: str) -> Any | None:
        """Obtiene un servicio registrado."""

        return self._services.get(name)

    def exists(self, name: str) -> bool:
        """Comprueba si un servicio está registrado."""

        return name in self._services

    def remove(self, name: str) -> None:
        """Elimina un servicio del registro."""

        self._services.pop(name, None)

    def all(self) -> dict[str, Any]:
        """Devuelve una copia de todos los servicios."""

        return self._services.copy()

    def clear(self) -> None:
        """Elimina todos los servicios registrados."""

        self._services.clear()


service_registry = ServiceRegistry()
