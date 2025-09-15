from pydantic import BaseModel

class WeatherRequestBase(BaseModel):
    lat: float
    lon: float

class WeatherResponse(BaseModel):
    temperature: float
    
    class Config:
        from_attributes = True