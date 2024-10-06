import pytest
from unittest.mock import patch, MagicMock
from src.adapters.weather_sdk_adapter import WeatherAdapter
from src.adapters.weather_sdk_adapter import WeatherAdapter



# Testing the initialization of the WeatherAdapter
@patch('src.adapters.weather_sdk_adapter.WeatherSdk')
def test_weather_adapter_initialization_success(mock_weather_sdk):
    mock_instance = MagicMock()
    mock_weather_sdk.return_value = mock_instance
    
    adapter = WeatherAdapter(access_key="fake_access_key")
    
    assert adapter.weather == mock_instance