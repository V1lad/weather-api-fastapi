from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WeatherRequestBase(BaseModel):
    lat: Optional[float] = None
    lon: Optional[float] = None

class WeatherResponse(BaseModel):
    id: int
    latitude: Optional[float]
    longitude: Optional[float]
    request_time: datetime
    temperature: float
    
    class Config:
        from_attributes = True