import pytest
from unittest.mock import patch, MagicMock
from src.adapters.weather_sdk_adapter import WeatherAdapter
from src.adapters.weather_sdk_adapter import WeatherException



# Testing the initialization of the WeatherAdapter
@patch('src.adapters.weather_sdk_adapter.WeatherSdk')
def test_weather_adapter_initialization_success(mock_weather_sdk):
    mock_instance = MagicMock()
    mock_weather_sdk.return_value = mock_instance
    
    adapter = WeatherAdapter(access_key="fake_access_key")
    
    assert adapter.weather == mock_instance

# Testing WeatherAdapter when it raises an error
@patch('src.adapters.weather_sdk_adapter.WeatherSdk')
def test_weather_adapter_initialization_failure(mock_weather_sdk):
    mock_weather_sdk.side_effect = Exception("Initialization error")
    
    with pytest.raises(WeatherException, match="Initialization error"):
        WeatherAdapter(access_key="fake_access_key")

# Testing getting weather data
@patch('src.adapters.weather_sdk_adapter.WeatherSdk')
def test_get_weather_success(mock_weather_sdk):
    mock_instance = mock_weather_sdk.return_value
    mock_instance.get_weather_data.return_value = {
        "city": "Itajai",
        "clima": "Clear",
        "temp": 25
    }
    
    adapter = WeatherAdapter(access_key="fake_access_key")
    result = adapter.get_weather(city="Itajai", country="br")
    
    assert result["city"] == "Itajai"
    assert result["clima"] == "Clear"
    assert result["temp"] == 25

# Testing weather data retrieval failure in WeatherAdapter
@patch('src.adapters.weather_sdk_adapter.WeatherSdk')
def test_get_weather_failure(mock_weather_sdk):
    mock_instance = mock_weather_sdk.return_value
    mock_instance.get_weather_data.side_effect = Exception("Weather data error")
    
    adapter = WeatherAdapter(access_key="fake_access_key")
    
    with pytest.raises(WeatherException, match="Weather data error"):
        adapter.get_weather(city="Itajai", country="br")
        
        
# Testing the retrieval of weather forecast
@patch('src.adapters.weather_sdk_adapter.WeatherSdk')
def test_get_forecast_success(mock_weather_sdk):
    mock_instance = mock_weather_sdk.return_value
    mock_instance.get_forecast_data.return_value = [
        {"day": "2024-10-01", "temp": 25},
        {"day": "2024-10-02", "temp": 22}
    ]
    
    adapter = WeatherAdapter(access_key="fake_access_key")
    result = adapter.get_forecast(city="Itajai", country="br")
    
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["day"] == "2024-10-01"
    assert result[0]["temp"] == 25