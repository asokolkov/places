from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True

    APP_NAME: str = "Places Server"
    APP_HOST: str = "localhost"
    APP_PORT: int = 8000

    JWT_ALGORITHM: str = "HS256"
    JWT_TOKEN_EXPIRE_DAYS: int = 30
    JWT_SECRET_KEY: str = "00000000000000000000000000000000"

    DATABASE_URL: str = "sqlite+aiosqlite:///"
    DATABASE_ECHO: bool = False


settings = Settings()
