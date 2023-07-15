import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/dbname")
    SYNCHRONOUS_DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")  # alembic doesn't support async
    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "dbname"
    PROJECT_NAME: str = "Navid's Url Shortener Service"
    PROJECT_VERSION: str = "0.1.0"
    BASE_URL: str = "http://navidkamali.com"
    CONN_POOL_TIMEOUT: int = 30

settings = Settings()
