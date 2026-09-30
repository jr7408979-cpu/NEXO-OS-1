from dataclasses import dataclass
from typing import Any


@dataclass
class ServiceStatus:
    """Estado de un servicio de NEXO OS."""

    name: str
    status: str = "stopped"


class ServiceManager:
    """Gestiona el ciclo de vida de los servicios de NEXO OS."""

    VALID_STATUSES = {
        "stopped",
        "running",
        "error",
        "disabled",
    }

    def __init__(self) -> None:
        self.services: dict[str, ServiceStatus] = {}

    def register(self, name: str) -> None:
        """Registra un servicio."""

        if not name.strip():
            raise ValueError(
                "El nombre del servicio no puede estar vacío."
            )

        if name not in self.services:
            self.services[name] = ServiceStatus(name=name)

    def start(self, name: str) -> None:
        """Inicia un servicio."""

        if name not in self.services:
            raise ValueError(
                f"Servicio no registrado: {name}"
            )

        self.services[name].status = "running"

    def stop(self, name: str) -> None:
        """Detiene un servicio."""

        if name not in self.services:
            raise ValueError(
                f"Servicio no registrado: {name}"
            )

        self.services[name].status = "stopped"

    def set_error(self, name: str) -> None:
        """Marca un servicio como fallido."""

        if name not in self.services:
            raise ValueError(
                f"Servicio no registrado: {name}"
            )

        self.services[name].status = "error"

    def disable(self, name: str) -> None:
        """Desactiva un servicio."""

        if name not in self.services:
            raise ValueError(
                f"Servicio no registrado: {name}"
            )

        self.services[name].status = "disabled"

    def status(self, name: str) -> str:
        """Obtiene el estado de un servicio."""

        if name not in self.services:
            return "unknown"

        return self.services[name].status

    def exists(self, name: str) -> bool:
        """Comprueba si un servicio está registrado."""

        return name in self.services

    def list_services(self) -> list[dict[str, str]]:
        """Lista todos los servicios y sus estados."""

        return [
            {
                "name": service.name,
                "status": service.status,
            }
            for service in self.services.values()
        ]

    def remove(self, name: str) -> None:
        """Elimina un servicio."""

        self.services.pop(name, None)
