from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WeatherRequestBase(BaseModel):
    lat: Optional[float] = None
    lon: Optional[float] = None

class WeatherResponse(BaseModel):
    temperature: float
    
    class Config:
        from_attributes = True