from dataclasses import dataclass
from enum import Enum


class SystemStatus(str, Enum):
    OFFLINE = "offline"
    STARTING = "starting"
    READY = "ready"
    DEGRADED = "degraded"
    RECOVERING = "recovering"
    SAFE_MODE = "safe_mode"
    STOPPING = "stopping"


@dataclass
class SystemState:
    status: SystemStatus = SystemStatus.OFFLINE
    version: str = "0.1.0"
    boot_count: int = 0

    def set_status(self, status: SystemStatus):
        self.status = status

    def is_ready(self) -> bool:
        return self.status == SystemStatus.READY
