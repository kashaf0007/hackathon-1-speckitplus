from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    gemini_api_key: str
    qdrant_url: str
    qdrant_api_key: str
    neon_database_url: str
    api_key: str
    qdrant_collection: str
    gemini_model: str

    class Config:
        env_file = ".env"

settings = Settings()