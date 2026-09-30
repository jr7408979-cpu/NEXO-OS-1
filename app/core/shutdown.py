from enum import Enum


class ShutdownStatus(str, Enum):
    """Estados posibles durante el apagado de NEXO OS."""

    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"


class ShutdownManager:
    """Gestiona el proceso de apagado de NEXO OS."""

    def __init__(self) -> None:
        self._status = ShutdownStatus.RUNNING

    def start(self) -> None:
        """Inicia el proceso de apagado."""

        self._status = ShutdownStatus.STOPPING

    def stop(self) -> None:
        """Marca el sistema como completamente detenido."""

        self._status = ShutdownStatus.STOPPED

    def resume(self) -> None:
        """Reanuda el sistema."""

        self._status = ShutdownStatus.RUNNING

    def is_shutting_down(self) -> bool:
        """Comprueba si el sistema está apagándose."""

        return self._status == ShutdownStatus.STOPPING

    def is_stopped(self) -> bool:
        """Comprueba si el sistema está detenido."""

        return self._status == ShutdownStatus.STOPPED

    def status(self) -> str:
        """Devuelve el estado actual."""

        return self._status.value


shutdown_manager = ShutdownManager()
