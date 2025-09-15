from app.external_api.openweather_api import OpenWeatherAPI
from app.db.models import WeatherRequest
from app.db.repository import WeatherRequestRepository

# Получает информацию от внешнего API
class WeatherService:
    def __init__(self, weather_api: OpenWeatherAPI, repository: WeatherRequestRepository):
        self.weather_api = weather_api
        self.repository = repository
    
    def get_weather_by_coords(self, lat: float, lon: float) -> WeatherRequest:
        # Получаем данные от модуля работы с внешним API
        weather_data = self.weather_api.get_weather_by_coords(lat, lon)
        
        # Создание записи в БД
        db_weather_request = WeatherRequest(
            latitude=lat,
            longitude=lon,
            temperature=weather_data["main"]["temp"]
        )
        
        return self.repository.create(db_weather_request)