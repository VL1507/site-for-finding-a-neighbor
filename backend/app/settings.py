import logging
from functools import lru_cache
from typing import Literal
from pydantic import BaseModel, ValidationInfo, computed_field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class DB(BaseSettings):
    URL: str


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
        return f"http://{self.HOST}:{self.PORT}"


class JWT(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    LIFE_TIME_MINUTES: int


class Settings(BaseSettings):
    DB: DB
    LOGGING: LOGGING
    API_V1_STR: str
    JWT: JWT
    FRONTEND: FRONTEND

    model_config = SettingsConfigDict(env_file="./app/.env", env_nested_delimiter="__")


@lru_cache
def get_settings():
    return Settings()


settings = Settings()
