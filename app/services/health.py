from datetime import datetime, timezone
from typing import Any

from app.core.health_registry import health_registry


def get_health_status() -> dict[str, Any]:
    """Devuelve el estado de salud de NEXO OS."""

    services = health_registry.all()

    unhealthy_services = [
        service
        for service, status in services.items()
        if status.lower() not in {
            "healthy",
            "ok",
            "ready",
            "active",
        }
    ]

    overall_status = (
        "degraded"
        if unhealthy_services
        else "healthy"
    )

    return {
        "status": overall_status,
        "services": services,
        "unhealthy_services": unhealthy_services,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
