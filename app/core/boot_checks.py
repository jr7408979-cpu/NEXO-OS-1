from app.core.database import initialize_database


class BootChecks:
    """Comprobaciones básicas antes de iniciar NEXO OS."""

    def check_database(self) -> bool:
        try:
            initialize_database()
            return True
        except Exception:
            return False

    def check_core(self) -> bool:
        return True

    def check_services(self) -> bool:
        return True

    def run(self) -> dict[str, bool]:
        return {
            "database": self.check_database(),
            "core": self.check_core(),
            "services": self.check_services(),
        }
