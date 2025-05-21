"""
Configuration settings for the User Service API
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    DEBUG: bool = False

    @staticmethod
    def get_url():
        settings = Settings()
        url = f'postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}'
        return url
