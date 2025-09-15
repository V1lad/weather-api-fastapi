from sqlalchemy.orm import Session
from app.db.models import WeatherRequest

# Репозиторий для работы с базой данных
class WeatherRequestRepository:
    def __init__(self, db: Session):
        self.db = db
    
    # Создаёт запись о запросе, вовращает полученный результат
    def create_weather_request(self, lat:float, lon:float, temp:float) -> WeatherRequest:
        weather_request = WeatherRequest(
            latitude=lat,
            longitude=lon,
            temperature=temp
        )
            
        self.db.add(weather_request)
        self.db.commit()
        self.db.refresh(weather_request)
        return weather_request
    
        