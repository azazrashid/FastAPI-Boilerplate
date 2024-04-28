from enum import Enum

from pydantic_settings import BaseSettings


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


class Config(BaseConfig):
    DEBUG: int = 0
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    DATABASE_URL: str
    RELEASE_VERSION: str = "0.1"
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24

    class Config:
        env_file = "./.env"


config: Config = Config()
