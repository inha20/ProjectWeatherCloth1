from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .database import get_db, init_db, UserModel, ClothingLogModel
from .models import User, UserCreate, FullReport, WeatherInfo, DustInfo, RecommendationResult
from .services.weather_service import WeatherService
from .services.recommendation_service import RecommendationService

app = FastAPI(title="Weather Cloth API")

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to Weather Cloth API"}

@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.user_id == user.user_id).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/recommend/{user_id}", response_model=FullReport)
def get_recommendation(user_id: str, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    weather = WeatherService.get_weather(user.region)
    dust = WeatherService.get_dust(user.region)
    
    # Simple score adjustments based on health/sensitivity
    # In a full impl, we'd fetch health data too.
    recommendation = RecommendationService.get_recommendation(
        temp=weather["feels_like"],
        humidity=weather["humidity"],
        rain=weather["rain_prob"],
        sensitivity=user.cold_sensitivity
    )
    
    return FullReport(
        user_name=user.name,
        weather=WeatherInfo(**weather),
        dust=DustInfo(**dust),
        adjusted_temp=weather["feels_like"],
        recommendation=recommendation
    )
