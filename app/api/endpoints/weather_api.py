from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.repository import WeatherRequestRepository
from app.core.openweatherapi_handler import OpenWeatherAPI
from app.core.weather_service import WeatherService
from app.api.pydantic_schemas import WeatherRequestBase, WeatherResponse

router = APIRouter()

# Возвращает экземпляр объекта для запросов к внешнему API
def get_weather_api_connector():
    return OpenWeatherAPI()

# Возвращает экземпляр репозитория БД с новой сессией
def get_weather_repository(db: Session = Depends(get_db)):
    return WeatherRequestRepository(db)

# Возвращает экземпляр модуля бизнес-логики
def get_weather_service(
    weather_api: OpenWeatherAPI = Depends(get_weather_api_connector),
    repository: WeatherRequestRepository = Depends(get_weather_repository)
):
    return WeatherService(weather_api, repository)

# Обработка основного варианта использования - запроса с целью получения температуры
@router.post("/weather", response_model=WeatherResponse)
async def get_weather(
    request: WeatherRequestBase,
    weather_service: WeatherService = Depends(get_weather_service)
):
    if not (request.lat is not None and request.lon is not None and request.lon <= 180 and
        request.lon >= -180 and request.lat <= 90 and request.lat >= 90):
        raise HTTPException(
            status_code=400, 
            detail="Incorrect data is provided"
        )
        
    return weather_service.get_weather_by_coords(request.lat, request.lon)


