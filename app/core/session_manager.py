from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


class SessionManager:
    """Gestiona las sesiones activas de NEXO OS."""

    def __init__(self) -> None:
        self._sessions: dict[str, dict[str, Any]] = {}

    def create(self, user_id: str) -> dict[str, Any]:
        """Crea una sesión para un usuario."""
        if not user_id.strip():
            raise ValueError("El ID del usuario no puede estar vacío.")

        session_id = str(uuid4())

        session = {
            "id": session_id,
            "user_id": user_id,
            "status": "active",
            "created_at": datetime.now(timezone.utc).isoformat(),
        }

        self._sessions[session_id] = session
        return session

    def get(self, session_id: str) -> dict[str, Any] | None:
        """Obtiene una sesión."""
        return self._sessions.get(session_id)

    def close(self, session_id: str) -> None:
        """Cierra una sesión."""
        session = self._sessions.get(session_id)

        if session is not None:
            session["status"] = "closed"
            session["closed_at"] = datetime.now(timezone.utc).isoformat()

    def list_active(self) -> list[dict[str, Any]]:
        """Lista las sesiones activas."""
        return [
            session
            for session in self._sessions.values()
            if session["status"] == "active"
        ]


session_manager = SessionManager()
