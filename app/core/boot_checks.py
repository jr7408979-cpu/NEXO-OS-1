class BootChecks:
    def check_database(self) -> bool:
        return True

    def check_core(self) -> bool:
        return True

    def check_services(self) -> bool:
        return True

    def run(self) -> dict:
        return {
            "database": self.check_database(),
            "core": self.check_core(),
            "services": self.check_services(),
        }
