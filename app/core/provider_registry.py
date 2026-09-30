from typing import Any


class ProviderRegistry:
    """Gestiona los proveedores de IA disponibles en NEXO OS."""

    def __init__(self) -> None:
        self._providers: dict[str, dict[str, Any]] = {}

    def register(
        self,
        name: str,
        base_url: str,
        enabled: bool = True,
    ) -> dict[str, Any]:
        """Registra un proveedor de IA."""
        if not name.strip():
            raise ValueError("El nombre del proveedor no puede estar vacío.")

        if not base_url.strip():
            raise ValueError("La URL del proveedor no puede estar vacía.")

        provider = {
            "name": name,
            "base_url": base_url,
            "enabled": enabled,
        }

        self._providers[name] = provider
        return provider

    def get(self, name: str) -> dict[str, Any] | None:
        """Obtiene un proveedor."""
        return self._providers.get(name)

    def remove(self, name: str) -> None:
        """Elimina un proveedor."""
        self._providers.pop(name, None)

    def list_providers(self) -> list[dict[str, Any]]:
        """Lista los proveedores registrados."""
        return list(self._providers.values())

    def enabled_providers(self) -> list[dict[str, Any]]:
        """Devuelve los proveedores activos."""
        return [
            provider
            for provider in self._providers.values()
            if provider["enabled"]
        ]


provider_registry = ProviderRegistry()
