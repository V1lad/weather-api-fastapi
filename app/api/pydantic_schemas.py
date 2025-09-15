from pydantic import BaseModel

# Для валидации запросов с целью получения температуры
class WeatherRequestBase(BaseModel):
    lat: float
    lon: float

# Для валидации ответа сервера с температурой
class WeatherResponse(BaseModel):
    temperature: float
    
    class Config:
        from_attributes = True