from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Модель, описывающая хранимую информацию о запросе. 
# Содержит информацию о времени запроса, содержание запроса - коордианты, результат - полученная температура.
class WeatherRequest(Base):
    __tablename__ = "weather_requests"
    
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    request_time = Column(DateTime, default=datetime.now())
    temperature = Column(Float)