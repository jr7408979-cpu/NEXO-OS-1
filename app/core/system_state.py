from dataclasses import dataclass
from enum import Enum


class SystemStatus(str, Enum):
    """Estados posibles de NEXO OS."""

    OFFLINE = "offline"
    STARTING = "starting"
    READY = "ready"
    DEGRADED = "degraded"
    RECOVERING = "recovering"
    SAFE_MODE = "safe_mode"
    STOPPING = "stopping"


@dataclass
class SystemState:
    """Estado central del sistema NEXO OS."""

    status: SystemStatus = SystemStatus.OFFLINE
    version: str = "0.1.0"
    boot_count: int = 0

    def set_status(self, status: SystemStatus) -> None:
        """Actualiza el estado del sistema."""

        if not isinstance(status, SystemStatus):
            raise ValueError(
                "El estado debe ser un SystemStatus válido."
            )

        self.status = status

    def is_ready(self) -> bool:
        """Comprueba si NEXO OS está listo."""

        return self.status == SystemStatus.READY

    def is_offline(self) -> bool:
        """Comprueba si NEXO OS está desconectado."""

        return self.status == SystemStatus.OFFLINE

    def is_degraded(self) -> bool:
        """Comprueba si el sistema está degradado."""

        return self.status == SystemStatus.DEGRADED

    def is_safe_mode(self) -> bool:
        """Comprueba si el sistema está en modo seguro."""

        return self.status == SystemStatus.SAFE_MODE

    def snapshot(self) -> dict[str, object]:
        """Devuelve una copia del estado actual."""

        return {
            "status": self.status.value,
            "version": self.version,
            "boot_count": self.boot_count,
        }
