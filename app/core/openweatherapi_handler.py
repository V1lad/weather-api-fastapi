import requests
from app.core.settings import settings

# Класс обработки запросов к Weather API
class OpenWeatherAPI:
    def __init__(self):
        self.base_url = settings.OPENWEATHER_BASE_URL
        self.api_key = settings.OPENWEATHER_API_KEY
    
    def get_weather_by_coords(self, lat: float, lon: float) -> dict:
        try:
            url = f"{self.base_url}/weather"
            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "metric"
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.HTTPError as e:
            # Обработка ошибок HTTP
            raise Exception(f"Weather API error: {e}")
    
        except requests.exceptions.RequestException as e:
            # Обработка других ошибок
            raise Exception(f"Network error: {e}")