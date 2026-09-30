from typing import Any


class PlanManager:
    """Gestiona los planes disponibles en NEXO OS."""

    def __init__(self) -> None:
        self._plans: dict[str, dict[str, Any]] = {
            "free": {
                "name": "Free",
                "active": True,
                "daily_limit": 10,
            },
            "basic": {
                "name": "Basic",
                "active": False,
                "daily_limit": 50,
            },
            "pro": {
                "name": "Pro",
                "active": False,
                "daily_limit": 200,
            },
        }

    def get(self, plan_id: str) -> dict[str, Any] | None:
        """Obtiene un plan."""
        return self._plans.get(plan_id)

    def list_plans(self) -> list[dict[str, Any]]:
        """Lista los planes disponibles."""
        return [
            {"id": plan_id, **plan}
            for plan_id, plan in self._plans.items()
        ]

    def activate(self, plan_id: str) -> dict[str, Any]:
        """Activa un plan."""
        plan = self._plans.get(plan_id)

        if plan is None:
            raise ValueError(f"Plan no encontrado: {plan_id}")

        plan["active"] = True
        return plan


plan_manager = PlanManager()
