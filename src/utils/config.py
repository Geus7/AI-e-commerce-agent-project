from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ollama_url: str = "http://localhost:11434"
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
