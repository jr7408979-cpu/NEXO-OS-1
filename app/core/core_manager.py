class CoreManager:
    def __init__(self):
        self.started = False

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

    def status(self) -> str:
        return "running" if self.started else "stopped"
