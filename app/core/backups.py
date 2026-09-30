from datetime import datetime, timezone
from pathlib import Path
import shutil


class BackupManager:
    """Gestiona copias de seguridad locales de NEXO OS."""

    def __init__(self, backup_dir: str = "nexo/data/backups") -> None:
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def create_backup(self, source_dir: str = "app") -> str:
        """Crea una copia de seguridad del directorio indicado."""

        source = Path(source_dir)

        if not source.exists():
            raise FileNotFoundError(
                f"No existe el directorio de origen: {source}"
            )

        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        destination = self.backup_dir / f"backup_{timestamp}"

        shutil.copytree(source, destination)

        return str(destination)

    def list_backups(self) -> list[str]:
        """Devuelve las copias de seguridad existentes."""

        if not self.backup_dir.exists():
            return []

        return sorted(
            str(path)
            for path in self.backup_dir.iterdir()
            if path.is_dir()
        )


backup_manager = BackupManager()
