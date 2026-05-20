import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Agentic Self-Healing CICD"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str
    
    # AI
    GOOGLE_API_KEY: str
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Logging
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()
