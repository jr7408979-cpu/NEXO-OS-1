from datetime import datetime, timezone


class BootReport:
    def create(self, checks: dict) -> dict:
        return {
            "status": "ready" if all(checks.values()) else "failed",
            "checks": checks,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
