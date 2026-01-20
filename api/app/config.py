from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")


@dataclass(frozen=True)
class Settings:
    db_connection: str
    db_host: str
    db_port: int
    db_database: str
    db_username: str
    db_password: str

    @property
    def database_url(self) -> str:
        connection = self.db_connection.lower()
        if connection in {"mariadb", "mysql"}:
            driver = "mysql+pymysql"
        else:
            driver = connection
        return (
            f"{driver}://{self.db_username}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_database}"
        )


settings = Settings(
    db_connection=os.getenv("DB_CONNECTION", "mariadb"),
    db_host=os.getenv("DB_HOST", "localhost"),
    db_port=int(os.getenv("DB_PORT", "3306")),
    db_database=os.getenv("DB_DATABASE", ""),
    db_username=os.getenv("DB_USERNAME", ""),
    db_password=os.getenv("DB_PASSWORD", ""),
)
