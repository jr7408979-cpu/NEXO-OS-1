from typing import Any


class HealthRegistry:
    """Registra el estado de salud de los servicios de NEXO OS."""

    def __init__(self) -> None:
        self._services: dict[str, str] = {}

    def update(self, service: str, status: str) -> None:
        """Actualiza el estado de un servicio."""

        if not service.strip():
            raise ValueError(
                "El nombre del servicio no puede estar vacío."
            )

        if not status.strip():
            raise ValueError(
                "El estado no puede estar vacío."
            )

        self._services[service] = status

    def get(self, service: str) -> str:
        """Obtiene el estado de un servicio."""

        return self._services.get(service, "unknown")

    def all(self) -> dict[str, str]:
        """Devuelve todos los estados registrados."""

        return self._services.copy()

    def is_healthy(self, service: str) -> bool:
        """Comprueba si un servicio está saludable."""

        return self.get(service).lower() in {
            "healthy",
            "ok",
            "ready",
            "active",
        }

    def clear(self, service: str | None = None) -> None:
        """Elimina un servicio o todos los registros."""

        if service is None:
            self._services.clear()
        else:
            self._services.pop(service, None)


health_registry = HealthRegistry()
