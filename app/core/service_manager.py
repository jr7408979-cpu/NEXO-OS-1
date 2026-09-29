from dataclasses import dataclass


@dataclass
class ServiceStatus:
    name: str
    status: str = "stopped"


class ServiceManager:
    def __init__(self):
        self.services = {}

    def register(self, name: str):
        self.services[name] = ServiceStatus(name)

    def start(self, name: str):
        if name in self.services:
            self.services[name].status = "running"

    def stop(self, name: str):
        if name in self.services:
            self.services[name].status = "stopped"

    def status(self, name: str) -> str:
        if name not in self.services:
            return "unknown"
        return self.services[name].status
