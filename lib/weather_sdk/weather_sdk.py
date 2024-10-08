import requests
from datetime import datetime
from lib.weather_sdk.utils.utils import normalize_temperatures

class WeatherSdk:
    def __init__(self,api_key):
        self.api_key = api_key
        self.city_endpoint = 'https://api.openweathermap.org/data/2.5/'
    
    def get_weather_data(self,city,country):
        response = self.__get_city_data(city,country,type='weather?')
        if response is None:
            raise ValueError("Failed to retrieve forecast data")
        try:
            return {
                "dt":self.__format_day_month(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"),
                "clima":response["weather"][0]["main"],
                "temp":int(response["main"]["temp"]),
                "city":city
            }
        except Exception as e:
            raise e
        
    def get_forecast_data(self,city,country):
        data = []  
        forecast_response = self.__get_city_data(city,country,type='forecast?')
        if forecast_response is None:
            raise ValueError("Failed to retrieve forecast data")
        try:  
            for item in forecast_response["list"]:
                data.append(
                    {
                        "temp":int(item["main"]["temp"]),
                        "dt":self.__format_day_month(item["dt_txt"])
                    }
                )
            return normalize_temperatures(data)
        except Exception as e:
            raise e
        
    def __get_city_data(self,city,country,type):
        try:
            end_point = self.city_endpoint + type + f"q={city},{country}&APPID={self.api_key}&units=metric"
            response = requests.get(end_point)
            response.raise_for_status()
            res = response.json()
            return res 
        except requests.exceptions.ConnectionError as errc:
            print(f"Connection error: {errc}") 
            
    def __format_day_month(self,date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return date_obj.strftime('%d/%m')