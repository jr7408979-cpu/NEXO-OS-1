from .system_state import SystemState, SystemStatus


class StateManager:
    """Gestiona el estado general de NEXO OS."""

    def __init__(self) -> None:
        self.state = SystemState()

    def start(self) -> None:
        """Pone el sistema en estado de inicio."""
        self.state.set_status(SystemStatus.STARTING)

    def ready(self) -> None:
        """Marca el sistema como listo."""
        self.state.set_status(SystemStatus.READY)

    def safe_mode(self) -> None:
        """Pone el sistema en modo seguro."""
        self.state.set_status(SystemStatus.SAFE_MODE)

    def recovering(self) -> None:
        """Marca el sistema como recuperándose."""
        self.state.set_status(SystemStatus.RECOVERING)

    def status(self) -> str:
        """Devuelve el estado actual."""
        return self.state.status.value

    def is_ready(self) -> bool:
        """Comprueba si el sistema está listo."""
        return self.state.status == SystemStatus.READY

    def is_safe_mode(self) -> bool:
        """Comprueba si el sistema está en modo seguro."""
        return self.state.status == SystemStatus.SAFE_MODE

    def is_recovering(self) -> bool:
        """Comprueba si el sistema está recuperándose."""
        return self.state.status == SystemStatus.RECOVERING


state_manager = StateManager()
