from fastapi import FastAPI
from app.db.models import Base
from app.db.session import engine

# Создание таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Weather API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Weather API Service"}