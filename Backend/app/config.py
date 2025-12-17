import os
from pydantic_settings import BaseSettings, SettingsConfigDict

# Get the absolute path to the .env file in the Backend directory
_backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_env_file_path = os.path.join(_backend_dir, ".env")

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    QDRANT_URL: str
    QDRANT_API_KEY: str
    NEON_POSTGRES_CONNECTION_STRING: str

    model_config = SettingsConfigDict(env_file=_env_file_path)

settings = Settings()