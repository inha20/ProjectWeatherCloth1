from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from .config import settings

engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"
    
    user_id = Column(String(50), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    region = Column(String(50), default="서울")
    cold_sensitivity = Column(Integer, default=3)
    heat_sensitivity = Column(Integer, default=3)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class ClothingLogModel(Base):
    __tablename__ = "clothing_logs"
    
    log_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), ForeignKey("users.user_id"))
    date = Column(Date, nullable=False)
    outer_wear = Column(String(100))
    top = Column(String(100))
    bottom = Column(String(100))
    shoes = Column(String(100))
    accessory = Column(String(200))
    temperature = Column(Float)
    feels_like = Column(Float)
    feedback = Column(Integer)  # -1 (추움), 0 (적당), 1 (더움)
    created_at = Column(DateTime, default=datetime.now)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
