from src.adapters.exceptions.weather_exceptions import WeatherException
from lib.weather_sdk.weather_sdk import WeatherSdk
from typing import List, Dict


class WeatherAdapter:
    def __init__(self,access_key: str):
        try:
            self.weather = WeatherSdk(access_key)
        except Exception as e:
            raise WeatherException(e)
                
    def get_weather(self,city: str,country: str) -> dict:
        """
        Gets information about the weather for the current day.
        :param city: target city for the query.
        :param country: country code for the target query.
        :raises WeatherException: If an error occurs while querying the weather.
        """
        try:
            weather_response = self.weather.get_weather_data(city,country)
            return weather_response
        except Exception as e:
            raise WeatherException(e)
    
    def get_forecast(self,city: str,country: str) -> List[Dict]:
        pass