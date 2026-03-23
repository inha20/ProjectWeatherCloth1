import random
from datetime import datetime
from typing import Dict, Any
from ..config import settings

class WeatherService:
    @staticmethod
    def get_weather(region: str) -> Dict[str, Any]:
        # Simulation Mode (Real API implementation would use requests and settings.WEATHER_API_KEY)
        # In a real scenario, this would call get_weather_data() from the original code but refactored.
        temp = random.uniform(-5, 30)
        humidity = random.randint(30, 90)
        wind = random.uniform(0.5, 5.0)
        
        # Calculate approximate feels like (simplistic for demo)
        feels_like = temp - (wind * 0.5) + (humidity * 0.05)
        
        return {
            "temperature": round(temp, 1),
            "feels_like": round(feels_like, 1),
            "humidity": humidity,
            "rain_prob": random.randint(0, 100),
            "wind_speed": round(wind, 1),
            "description": "맑음" if humidity < 70 else "흐림"
        }

    @staticmethod
    def get_dust(region: str) -> Dict[str, Any]:
        pm10 = random.randint(10, 150)
        pm25 = random.randint(5, 80)
        
        status = "좋음"
        if pm25 > 75: status = "매우나쁨"
        elif pm25 > 35: status = "나쁨"
        elif pm25 > 15: status = "보통"
        
        return {
            "pm10": pm10,
            "pm25": pm25,
            "status": status
        }
