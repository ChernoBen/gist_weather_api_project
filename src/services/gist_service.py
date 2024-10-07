from src.utils.process_gist_content import process_gist_content
from src.adapters.weather_sdk_adapter import WeatherAdapter
from src.adapters.pygithub_adapter import PyGitHubAdapter
from src.utils.envs import EnvironmentConfig as envs
from src.utils.logging import log_error
from typing import List, Dict


class GistService:
    def __init__(self):
        try:
            self.weather = WeatherAdapter(envs.get("WEATHER_KEY"))
            self.github = PyGitHubAdapter(
                envs.get('GITHUB_KEY')
            )
        except Exception as e:
            log_error(e)
            raise e
    
    def create_new_gist(self,city: str,country: str) -> str:
        try:
            weather_now = self.weather.get_weather(
                city,
                country
            )
            weather_forecast = self.weather.get_forecast(
                city,
                country
            )
            content = self.__process_gist_content(
                weather_now,
                weather_forecast
            )
            url = self.github.add_comment_to_gist(content)
            return url
        except Exception as e:
            log_error(e)
            raise e

    def __process_gist_content(self,weather: dict,forecast: List[Dict]) -> str:
        return process_gist_content(weather,forecast)