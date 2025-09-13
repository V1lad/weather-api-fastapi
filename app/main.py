from fastapi import FastAPI
from app.db.models import Base
from app.db.session import engine
from app.api import weather_api

# Создание таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Weather API", version="1.0.0")

app.include_router(weather_api.router, prefix="/api/v1", tags=["weather"])

@app.get("/")
async def root():
    return {"message": "Weather API Service"}