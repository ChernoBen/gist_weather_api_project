import pytest
import requests
from unittest.mock import patch
from weather_sdk.weather_sdk import WeatherSdk


# Test for successful weather data retrieval
@patch('weather_sdk.weather_sdk.requests.get')
def test_get_weather_data_success(mock_get):
    # Simulating a successful API response to get_weather_data
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
    # Simulating a connection error to get_weather_data
    mock_get.side_effect = requests.exceptions.ConnectionError
    
    sdk = WeatherSdk(api_key="fake_api_key")
    
    with pytest.raises(ValueError, match="Failed to retrieve forecast data"):
        sdk.get_weather_data('Itajai', 'br')

# Test for successful forecast data retrieval
@patch('weather_sdk.weather_sdk.requests.get')
def test_get_forecast_data_success(mock_get):
    # Simulating a successful API response for forecast to get_forecast_data
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "list": [
            {"main": {"temp": 22}, "dt_txt": "2024-10-03 12:00:00"},
            {"main": {"temp": 18}, "dt_txt": "2024-10-04 12:00:00"},
        ]
    }

    sdk = WeatherSdk(api_key="fake_api_key")
    result = sdk.get_forecast_data('Itajai', 'br')

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["average_temp"] == 22
    
# Test for timeout exception case   
@patch('weather_sdk.weather_sdk.requests.get')
def test_get_forecast_data_timeout(mock_get):
    # Simulando um erro de timeout
    mock_get.side_effect = requests.exceptions.Timeout
    
    sdk = WeatherSdk(api_key="fake_api_key")
    
    with pytest.raises(requests.exceptions.Timeout):
        sdk.get_forecast_data('Itajai', 'br')