import pytest
from app.db.repository import WeatherRequestRepository
from app.db.models import WeatherRequest

def test_create_weather_request(db_session):
    repository = WeatherRequestRepository(db_session)
    
    result = repository.create_weather_request(lat=23.2, lon=51.2, temp=15.4)
    
    assert result.id is not None
    assert result.latitude == 23.2
    assert result.longitude == 51.2
    assert result.temperature == 15.4
    
    # Проверяем, что запись сохранена в БД
    saved_request = db_session.query(WeatherRequest).first()
    assert saved_request.id == result.id
    assert saved_request.temperature == result.temperature