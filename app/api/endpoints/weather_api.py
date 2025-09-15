from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.repository import WeatherRequestRepository
from app.core.openweatherapi_handler import OpenWeatherAPI
from app.api.pydantic_schemas import WeatherRequestBase, WeatherResponse
from app.db.models import WeatherRequest

router = APIRouter()

# Возвращает экземпляр объекта для запросов к внешнему API
def get_weather_api_connector():
    return OpenWeatherAPI()

# Возвращает экземпляр репозитория БД с новой сессией
def get_weather_repository(db: Session = Depends(get_db)):
    return WeatherRequestRepository(db)

# Обработка основного варианта использования - запроса с целью получения температуры
# С записью данных о запросе в базу данных
@router.post("/weather", response_model=WeatherResponse)
async def get_weather(
    request: WeatherRequestBase,
    openweatherapi_handler: OpenWeatherAPI = Depends(get_weather_api_connector),
    db: WeatherRequestRepository = Depends(get_weather_repository)
):
    if not (request.lat is not None and request.lon is not None and request.lon <= 180 and
        request.lon >= -180 and request.lat <= 90 and request.lat >= -90):
        raise HTTPException(
            status_code=400, 
            detail="Incorrect data is provided"
        )
    
    # Получаем данные от модуля работы с внешним API
    weather_data = openweatherapi_handler.get_weather_by_coords(request.lat, request.lon)
    
    # Создание записи в БД
    db_weather_request = WeatherRequest(
        latitude=request.lat,
        longitude=request.lon,
        temperature=weather_data["main"]["temp"]
    )
    
    return db.create(db_weather_request)



