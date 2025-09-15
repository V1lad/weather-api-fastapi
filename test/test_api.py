import pytest
from unittest.mock import patch

def test_get_weather_by_coords_not_mock(client):
    response = client.post("/api/v1/weather", json={"lat": 53, "lon": 37.6173})
    
    assert response.status_code == 200
    data = response.json()
    
    assert (data["temperature"] > -90 and data["temperature"] < 120)
    
def test_get_weather_by_coords_not_mock_incorrect(client):
    response = client.post("/api/v1/weather", json={"lat": -100, "lon": 37.6173})
    
    assert response.status_code == 400
    data = response.json()
    
    assert data["detail"] == "Incorrect data is provided"
    
    
def test_get_weather_by_coords_mock(client, mock_weather_api):
    response = client.post("/api/v1/weather", json={"lat": 55.7558, "lon": 37.6173})
    
    assert response.status_code == 200
    data = response.json()
    mock_weather_api.return_value.get_weather_by_coords.assert_called_once_with(55.7558, 37.6173)
    assert data["temperature"] == 18.2
    

