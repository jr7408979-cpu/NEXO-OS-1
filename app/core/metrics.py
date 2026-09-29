from dataclasses import dataclass


@dataclass
class SystemMetrics:
    requests: int = 0
    errors: int = 0
    active_services: int = 0

    def record_request(self):
        self.requests += 1

    def record_error(self):
        self.errors += 1

    def set_active_services(self, count: int):
        self.active_services = count
