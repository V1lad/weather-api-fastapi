from sqlalchemy.orm import Session
from typing import Optional, List
from app.db.models import WeatherRequest

class WeatherRequestRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, weather_request: WeatherRequest) -> WeatherRequest:
        self.db.add(weather_request)
        self.db.commit()
        self.db.refresh(weather_request)
        return weather_request
    
        