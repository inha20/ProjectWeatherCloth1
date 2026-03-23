import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "Smart Clothing Recommender"
    DEBUG: bool = True
    
    # API Keys (Public Data Portal)
    WEATHER_API_KEY: str = os.getenv("WEATHER_API_KEY", "SIMULATION_MODE")
    DUST_API_KEY: str = os.getenv("DUST_API_KEY", "SIMULATION_MODE")
    
    # Database Settings
    # Default to local SQLite for easy portability
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./weather_cloth.db")
    
    # Recommendation Constants
    DEFAULT_REGION: str = "서울"
    CLO_THRESHOLD: float = 0.1  # Score step for warmth
    
    class Config:
        env_file = ".env"

settings = Settings()
