from typing import Any


class AgentConfig:
    """Configuración de un agente de IA."""

    def __init__(
        self,
        name: str,
        enabled: bool = True,
        priority: int = 0,
        settings: dict[str, Any] | None = None,
    ) -> None:
        if not name.strip():
            raise ValueError("El nombre del agente no puede estar vacío.")

        self.name = name
        self.enabled = enabled
        self.priority = priority
        self.settings = settings or {}

    def enable(self) -> None:
        """Activa el agente."""
        self.enabled = True

    def disable(self) -> None:
        """Desactiva el agente."""
        self.enabled = False

    def update(self, **settings: Any) -> None:
        """Actualiza la configuración del agente."""
        self.settings.update(settings)

    def to_dict(self) -> dict[str, Any]:
        """Convierte la configuración a un diccionario."""
        return {
            "name": self.name,
            "enabled": self.enabled,
            "priority": self.priority,
            "settings": dict(self.settings),
        }
