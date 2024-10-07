import pytest
from unittest.mock import patch, MagicMock
from src.utils.envs import EnvironmentConfig as envs
from src.services.gist_service import GistService
from src.adapters.exceptions.weather_exceptions import WeatherException


# Testing the initialization of the GistService.
@patch('src.services.gist_service.WeatherAdapter')
@patch('src.services.gist_service.PyGitHubAdapter')
@patch('src.utils.envs.EnvironmentConfig')
def test_gist_service_initialization_success(mock_env, mock_github, mock_weather):
    mock_env.get.side_effect = lambda key: "fake_key" if key in ["WEATHER_KEY", "GITHUB_KEY"] else None
    service = GistService()
    
    assert service.weather is not None
    assert service.github is not None

# Testing the creation of a new gist service instance
@patch('src.services.gist_service.WeatherAdapter')
@patch('src.services.gist_service.PyGitHubAdapter')
@patch('src.utils.envs.EnvironmentConfig')
@patch('src.utils.process_gist_content')
def test_create_new_gist_success(mock_process_gist_content, mock_env, mock_github, mock_weather):
    mock_env.get.side_effect = lambda key: "fake_key" if key in ["WEATHER_KEY", "GITHUB_KEY"] else None
    mock_weather_instance = mock_weather.return_value
    mock_weather_instance.get_weather.return_value = {
        "city": "Itajai",
        "clima": "Clear",
        "temp": 25,
        "dt":"2024-09-30"
    }
    mock_weather_instance.get_forecast.return_value = [
        {"dt": "2024-10-01", "average_temp": 25},
        {"dt": "2024-10-02", "average_temp": 22}
    ]
    mock_process_gist_content.return_value = "Processed Gist Content"
    mock_github_instance = mock_github.return_value
    mock_github_instance.add_comment_to_gist.return_value = "http://gist.url"

    service = GistService()
    url = service.create_new_gist(city="Itajai", country="br")
    
# Testing if create_new_gist method raises a WeatherException
@patch('src.services.gist_service.WeatherAdapter')
@patch('src.services.gist_service.PyGitHubAdapter')
@patch('src.utils.envs.EnvironmentConfig')
def test_create_new_gist_failure(mock_env, mock_github, mock_weather):
    mock_env.get.side_effect = lambda key: "fake_key" if key in ["WEATHER_KEY", "GITHUB_KEY"] else None
    mock_weather_instance = mock_weather.return_value
    mock_weather_instance.get_weather.side_effect = WeatherException("Weather data error")
    
    service = GistService()
    
    with pytest.raises(WeatherException, match="Weather data error"):
        service.create_new_gist(city="Itajai", country="br")