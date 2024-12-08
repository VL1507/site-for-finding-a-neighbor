import logging
from functools import lru_cache
from typing import Literal

from pydantic import (
    HttpUrl,
    PostgresDsn,
    computed_field,
)
from pydantic_settings import BaseSettings, SettingsConfigDict


class DB_sqlite(BaseSettings):
    URL: str


class DB_PostgreSQL(BaseSettings):
    USERNAME: str
    SECRET: str
    HOST: str
    PORT: str
    NAME: str

    @computed_field
    @property
    def URL(self) -> str:
        return str(
            PostgresDsn(
                f"postgresql+asyncpg://{self.USERNAME}:{self.SECRET}@{self.HOST}:{self.PORT}/{self.NAME}"
            )
        )


class LOGGING(BaseSettings):
    LEVEL: str

    @computed_field
    @property
    def VALIDATE_LEVEL(self) -> Literal[10, 20, 30, 40, 50]:
        level = self.LEVEL.lower()
        if level == "debug":
            return logging.DEBUG
        elif level == "info":
            return logging.INFO
        elif level == "warning":
            return logging.WARNING
        elif level == "error":
            return logging.ERROR
        elif level == "critical":
            return logging.CRITICAL
        else:
            raise ValueError(f"Invalid logging level: {self.LEVEL}")


class FRONTEND(BaseSettings):
    HOST: str
    PORT: str

    @computed_field
    @property
    def URL(self) -> str:
        return str(HttpUrl(f"http://{self.HOST}:{self.PORT}"))


class JWT(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    LIFE_TIME_MINUTES: int


class Settings(BaseSettings):
    DB: DB_sqlite
    # DB: DB_PostgreSQL
    LOGGING: LOGGING
    API_V1_STR: str
    JWT: JWT
    FRONTEND: FRONTEND

    model_config = SettingsConfigDict(
        env_file="./app/.env", env_nested_delimiter="__")


@lru_cache
def get_settings():
    return Settings()


settings = Settings()
