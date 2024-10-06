import pytest
import requests
from unittest.mock import patch
from weather_sdk.weather_sdk import WeatherSdk


# Test for successful weather data retrieval
@patch('weather_sdk.weather_sdk.requests.get')
def test_get_weather_data_success(mock_get):
    # Simulating a successful API response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "weather": [{"main": "Clear"}],
        "main": {"temp": 25}
    }
    
    sdk = WeatherSdk(api_key="fake_api_key")
    result = sdk.get_weather_data('Itajai','br')
    
    assert result["clima"] == "Clear"
    assert result["temp"] == 25
    assert result["city"] == 'Itajai'
    
#Test for weather data connection error
@patch('weather_sdk.weather_sdk.requests.get')
def test_get_weather_data_connection_error(mock_get):
    # Simulando um erro de conexão
    mock_get.side_effect = requests.exceptions.ConnectionError
    
    sdk = WeatherSdk(api_key="fake_api_key")
    
    with pytest.raises(ValueError, match="Failed to retrieve forecast data"):
        sdk.get_weather_data('Itajai', 'br')