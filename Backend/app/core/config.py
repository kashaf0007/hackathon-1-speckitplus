import os
from pydantic_settings import BaseSettings

# Get the absolute path to the .env file in the Backend directory
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_env_file_path = os.path.join(_backend_dir, ".env")

class Settings(BaseSettings):
    gemini_api_key: str
    qdrant_url: str
    qdrant_api_key: str
    neon_database_url: str
    api_key: str
    qdrant_collection: str = "documents"
    gemini_model: str = "gemini-2.0-flash"

    class Config:
        env_file = _env_file_path
        extra = "ignore"

settings = Settings()