from typing import Any


class AccessManager:
    """Gestiona permisos y acceso dentro de NEXO OS."""

    def __init__(self) -> None:
        self._roles: dict[str, set[str]] = {
            "admin": {
                "system.read",
                "system.write",
                "users.read",
                "users.write",
                "payments.read",
                "agents.run",
            },
            "user": {
                "system.read",
                "agents.run",
            },
        }

    def add_permission(self, role: str, permission: str) -> None:
        """Añade un permiso a un rol."""
        if not role.strip():
            raise ValueError("El rol no puede estar vacío.")

        if not permission.strip():
            raise ValueError("El permiso no puede estar vacío.")

        self._roles.setdefault(role, set()).add(permission)

    def remove_permission(self, role: str, permission: str) -> None:
        """Elimina un permiso de un rol."""
        permissions = self._roles.get(role)

        if permissions is not None:
            permissions.discard(permission)

    def has_permission(self, role: str, permission: str) -> bool:
        """Comprueba si un rol tiene un permiso."""
        return permission in self._roles.get(role, set())

    def get_permissions(self, role: str) -> list[str]:
        """Devuelve los permisos de un rol."""
        return sorted(self._roles.get(role, set()))

    def list_roles(self) -> dict[str, list[str]]:
        """Devuelve todos los roles y sus permisos."""
        return {
            role: sorted(permissions)
            for role, permissions in self._roles.items()
        }


access_manager = AccessManager()
