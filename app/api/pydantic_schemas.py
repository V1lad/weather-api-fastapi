from pydantic import BaseModel
from typing import Optional

class WeatherRequestBase(BaseModel):
    lat: Optional[float] = None
    lon: Optional[float] = None

