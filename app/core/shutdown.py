class ShutdownManager:
    def __init__(self):
        self.is_shutting_down = False

    def start(self):
        self.is_shutting_down = True

    def stop(self):
        self.is_shutting_down = False

    def status(self) -> str:
        return "stopping" if self.is_shutting_down else "running"
