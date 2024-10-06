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