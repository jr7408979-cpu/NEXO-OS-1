from .boot_checks import BootChecks
from .boot_report import BootReport
from .config_manager import ConfigManager
from .event_bus import EventBus
from .logger import setup_logger
from .metrics import SystemMetrics
from .permissions import PermissionManager
from .service_manager import ServiceManager
from .system_state import SystemState, SystemStatus


class BootManager:
    """Gestiona el arranque principal de NEXO OS."""

    def __init__(self):
        self.config = ConfigManager()
        self.events = EventBus()
        self.metrics = SystemMetrics()
        self.permissions = PermissionManager()
        self.services = ServiceManager()
        self.state = SystemState()
        self.checks = BootChecks()
        self.reporter = BootReport()
        self.logger = setup_logger()

    def start(self) -> dict:
        """Ejecuta el proceso de arranque de NEXO OS."""

        self.state.set_status(SystemStatus.STARTING)

        self.logger.info("Starting NEXO OS...")

        checks = self.checks.run()
        report = self.reporter.create(checks)

        self.metrics.increment("boot_attempts")

        if not all(checks.values()):
            self.state.set_status(SystemStatus.SAFE_MODE)
            self.metrics.increment("boot_failures")

            self.logger.error("NEXO boot checks failed.")

            return {
                **report,
                "system_status": self.state.status.value,
                "boot_count": self.state.boot_count,
            }

        self.state.boot_count += 1
        self.state.set_status(SystemStatus.READY)

        self.metrics.increment("successful_boots")

        self.logger.info("NEXO OS is ready.")

        return {
            **report,
            "system_status": self.state.status.value,
            "boot_count": self.state.boot_count,
        }

    def status(self) -> str:
        """Devuelve el estado actual del sistema."""
        return self.state.status.value
