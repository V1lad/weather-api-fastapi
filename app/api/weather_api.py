from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.db.session import get_db
from app.db.repository import WeatherRequestRepository
from app.external_api.openweather_api import OpenWeatherAPI
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
