from .system_state import SystemState, SystemStatus


class StateManager:
    def __init__(self):
        self.state = SystemState()

    def start(self):
        self.state.set_status(SystemStatus.STARTING)

    def ready(self):
        self.state.set_status(SystemStatus.READY)

    def safe_mode(self):
        self.state.set_status(SystemStatus.SAFE_MODE)

    def recovering(self):
        self.state.set_status(SystemStatus.RECOVERING)

    def status(self):
        return self.state.status.value
