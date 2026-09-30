from typing import Any

from app.core.agent_config import AgentConfig


class AgentConfigRegistry:
    """Gestiona las configuraciones de los agentes de IA."""

    def __init__(self) -> None:
        self._configs: dict[str, AgentConfig] = {}

    def register(self, config: AgentConfig) -> None:
        """Registra una configuración."""
        self._configs[config.name] = config

    def get(self, name: str) -> AgentConfig | None:
        """Obtiene una configuración."""
        return self._configs.get(name)

    def remove(self, name: str) -> None:
        """Elimina una configuración."""
        self._configs.pop(name, None)

    def list_configs(self) -> list[dict[str, Any]]:
        """Lista las configuraciones."""
        return [
            config.to_dict()
            for config in self._configs.values()
        ]

    def enabled_configs(self) -> list[AgentConfig]:
        """Devuelve solamente los agentes activos."""
        return [
            config
            for config in self._configs.values()
            if config.enabled
        ]


agent_config_registry = AgentConfigRegistry()
