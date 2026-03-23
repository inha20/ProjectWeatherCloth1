from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    user_id: str
    name: str
    region: str = "서울"
    cold_sensitivity: int = 3
    heat_sensitivity: int = 3

class UserCreate(UserBase):
    pass

class User(UserBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class WeatherInfo(BaseModel):
    temperature: float
    feels_like: float
    humidity: int
    rain_prob: int
    wind_speed: float
    description: str

class DustInfo(BaseModel):
    pm10: int
    pm25: int
    status: str

class RecommendationResult(BaseModel):
    outer: Optional[str]
    top: str
    bottom: str
    shoes: str
    accessories: List[str]
    warmth_score: float
    tips: List[str]

class FullReport(BaseModel):
    user_name: str
    weather: WeatherInfo
    dust: DustInfo
    adjusted_temp: float
    recommendation: RecommendationResult
    timestamp: datetime = datetime.now()
