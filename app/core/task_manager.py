from datetime import datetime, timezone
from typing import Any


class TaskManager:
    """Gestiona tareas internas de NEXO OS."""

    def __init__(self) -> None:
        self._tasks: dict[str, dict[str, Any]] = {}

    def create(self, task_id: str, name: str) -> dict[str, Any]:
        """Crea una tarea."""
        if not task_id.strip():
            raise ValueError("El ID de la tarea no puede estar vacío.")

        if task_id in self._tasks:
            raise ValueError(f"La tarea ya existe: {task_id}")

        task = {
            "id": task_id,
            "name": name,
            "status": "pending",
            "created_at": datetime.now(timezone.utc).isoformat(),
        }

        self._tasks[task_id] = task
        return task

    def update_status(self, task_id: str, status: str) -> dict[str, Any]:
        """Actualiza el estado de una tarea."""
        task = self._tasks.get(task_id)

        if task is None:
            raise ValueError(f"Tarea no encontrada: {task_id}")

        task["status"] = status
        task["updated_at"] = datetime.now(timezone.utc).isoformat()

        return task

    def get(self, task_id: str) -> dict[str, Any] | None:
        """Obtiene una tarea."""
        return self._tasks.get(task_id)

    def list_tasks(self) -> list[dict[str, Any]]:
        """Lista todas las tareas."""
        return list(self._tasks.values())


task_manager = TaskManager()
