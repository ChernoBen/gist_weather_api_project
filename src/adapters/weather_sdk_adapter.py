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
        pass
    
    def get_forecast(self,city: str,country: str) -> List[Dict]:
        pass