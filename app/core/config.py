from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    DATABASE_URL: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
