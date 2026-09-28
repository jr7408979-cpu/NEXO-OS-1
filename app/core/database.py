import sqlite3
from pathlib import Path


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATA_DIR / "nexo.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection
