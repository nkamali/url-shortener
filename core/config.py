import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///:memory:")
    PROJECT_NAME: str = "Navid's Url Shortener Service"
    PROJECT_VERSION: str = "0.1.0"
    BASE_URL: str = "http://navidkamali.com"

settings = Settings()
