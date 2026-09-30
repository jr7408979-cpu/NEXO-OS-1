from typing import Any

from app.core.model_registry import model_registry
from app.core.provider_registry import provider_registry


class AIRouter:
    """Selecciona el proveedor y modelo de IA que utilizará NEXO OS."""

    def select_model(self, model_name: str) -> dict[str, Any]:
        """Selecciona un modelo específico."""

        model = model_registry.get(model_name)

        if model is None:
            raise ValueError(f"Modelo no encontrado: {model_name}")

        if not model["enabled"]:
            raise ValueError(f"El modelo está desactivado: {model_name}")

        provider = provider_registry.get(model["provider"])

        if provider is None:
            raise ValueError(
                f"Proveedor no encontrado: {model['provider']}"
            )

        if not provider["enabled"]:
            raise ValueError(
                f"El proveedor está desactivado: {model['provider']}"
            )

        return {
            "model": model,
            "provider": provider,
        }

    def available_models(self) -> list[dict[str, Any]]:
        """Devuelve los modelos disponibles."""

        available = []

        for model in model_registry.enabled_models():
            provider = provider_registry.get(model["provider"])

            if provider and provider["enabled"]:
                available.append(model)

        return available


ai_router = AIRouter()
