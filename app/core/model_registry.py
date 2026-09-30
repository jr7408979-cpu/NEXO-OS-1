from typing import Any


class ModelRegistry:
    """Gestiona los modelos de IA disponibles en NEXO OS."""

    def __init__(self) -> None:
        self._models: dict[str, dict[str, Any]] = {}

    def register(
        self,
        name: str,
        provider: str,
        model_id: str,
        enabled: bool = True,
    ) -> dict[str, Any]:
        """Registra un modelo de IA."""
        if not name.strip():
            raise ValueError("El nombre del modelo no puede estar vacío.")

        if not provider.strip():
            raise ValueError("El proveedor no puede estar vacío.")

        if not model_id.strip():
            raise ValueError("El ID del modelo no puede estar vacío.")

        model = {
            "name": name,
            "provider": provider,
            "model_id": model_id,
            "enabled": enabled,
        }

        self._models[name] = model
        return model

    def get(self, name: str) -> dict[str, Any] | None:
        """Obtiene un modelo."""
        return self._models.get(name)

    def remove(self, name: str) -> None:
        """Elimina un modelo."""
        self._models.pop(name, None)

    def list_models(self) -> list[dict[str, Any]]:
        """Lista todos los modelos."""
        return list(self._models.values())

    def enabled_models(self) -> list[dict[str, Any]]:
        """Devuelve los modelos activos."""
        return [
            model
            for model in self._models.values()
            if model["enabled"]
        ]


model_registry = ModelRegistry()
