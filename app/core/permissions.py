from enum import IntEnum


class AuthorityLevel(IntEnum):
    """Niveles de autoridad disponibles en NEXO OS."""

    OBSERVE = 1
    SAFE_REPAIR = 2
    APPROVAL_REQUIRED = 3
    CRITICAL = 4


class PermissionManager:
    """Controla el nivel de autoridad del sistema."""

    def __init__(self) -> None:
        self.level = AuthorityLevel.OBSERVE

    def set_level(self, level: AuthorityLevel) -> None:
        """Establece el nivel de autoridad."""

        if not isinstance(level, AuthorityLevel):
            raise ValueError(
                "El nivel debe ser un AuthorityLevel válido."
            )

        self.level = level

    def get_level(self) -> AuthorityLevel:
        """Devuelve el nivel de autoridad actual."""

        return self.level

    def can_execute(
        self,
        required_level: AuthorityLevel,
    ) -> bool:
        """Comprueba si el sistema puede ejecutar una acción."""

        if not isinstance(required_level, AuthorityLevel):
            raise ValueError(
                "El nivel requerido debe ser un AuthorityLevel válido."
            )

        return self.level >= required_level

    def requires_approval(
        self,
        required_level: AuthorityLevel,
    ) -> bool:
        """Indica si una acción necesita un nivel superior de autoridad."""

        return not self.can_execute(required_level)
