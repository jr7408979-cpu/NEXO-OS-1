from core.config_manager import ConfigManager
from core.database import get_connection
from core.event_bus import EventBus
from core.logger import setup_logger
from core.metrics import SystemMetrics
from core.permissions import PermissionManager
from core.service_manager import ServiceManager
from core.system_state import SystemState, SystemStatus


class BootManager:
    def __init__(self):
        self.config = ConfigManager()
        self.events = EventBus()
        self.metrics = SystemMetrics()
        self.permissions = PermissionManager()
        self.services = ServiceManager()
        self.state = SystemState()
        self.logger = setup_logger()

    def start(self):
        self.state.set_status(SystemStatus.STARTING)

        get_connection()

        self.state.boot_count += 1
        self.state.set_status(SystemStatus.READY)

        self.logger.info("NEXO OS is ready.")

        return self.state
