from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR: Path = Path(__file__).resolve().parent


class SettingsConfig(BaseSettings):
    CORS_ORIGINS: list[str] = ["*"]

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    INNER_POSTGRES_PORT: int
    OUTER_POSTGRES_PORT: int
    DEBUG: str

    @property
    def database_connection(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.INNER_POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = BASE_DIR / ".env"
        extra = "ignore"


config: SettingsConfig = SettingsConfig()
