import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db.session import get_db
from app.db.models import Base

TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    # Создаем таблицы для тестов
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Полная очистка по закрытии
        Base.metadata.drop_all(bind=engine)
    
@pytest.fixture(scope="function")
def client(db_session):
    # Переопределяем зависимость базы данных
    def override_get_db():
        try:
            yield db_session
        finally:
            # Ничего, так как управление делегировано db_session
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()

@pytest.fixture(scope="function")
def mock_weather_api(mocker):
    mock = mocker.patch("app.api.endpoints.weather_api.OpenWeatherAPI")
    mock.return_value.get_weather_by_coords.return_value = {
        "main": {"temp": 18.2}
    }
    
    return mock