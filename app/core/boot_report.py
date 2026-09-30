from datetime import datetime, timezone
from typing import Any


class BootReport:
    """Genera reportes del proceso de arranque de NEXO OS."""

    def create(self, checks: dict[str, bool]) -> dict[str, Any]:
        """Crea un reporte con el resultado de las comprobaciones."""

        success = all(checks.values())

        return {
            "status": "ready" if success else "failed",
            "success": success,
            "checks": checks,
            "passed_checks": sum(
                1 for result in checks.values() if result
            ),
            "total_checks": len(checks),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
