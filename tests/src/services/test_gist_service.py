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

