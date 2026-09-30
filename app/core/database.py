import sqlite3
from pathlib import Path
from typing import Iterator


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "nexo" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = DATA_DIR / "nexo.db"


def get_connection() -> sqlite3.Connection:
    """Abre una conexión con la base de datos de NEXO OS."""

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database() -> None:
    """Inicializa las tablas básicas de NEXO OS."""

    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS system_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                source TEXT NOT NULL,
                data TEXT,
                created_at TEXT NOT NULL
            )
            """
        )

        connection.commit()


def connection_context() -> Iterator[sqlite3.Connection]:
    """Proporciona una conexión para operaciones de base de datos."""

    connection = get_connection()

    try:
        yield connection
    finally:
        connection.close()
