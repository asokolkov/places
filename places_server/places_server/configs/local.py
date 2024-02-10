from os import getenv


DEBUG = getenv("DEBUG", True)

DATABASE_URL = getenv("DATABASE_URL", "sqlite+aiosqlite:///")
DATABASE_ECHO = getenv("DATABASE_ECHO", False)

APP_HOST = getenv("APP_HOST", "localhost")
APP_PORT = getenv("APP_PORT", 8000)

JWT_SECRET_KEY = getenv("JWT_SECRET_KEY", "00000000000000000000000000000000")
