from typing import List, Dict
from src.utils.word_mapper import get_word

def process_gist_content(weather_now: dict,weather_forecast: List[Dict]) -> str:
    translated_word = get_word(weather_now['clima'])
    weather = f"""
    {weather_now['temp']}°C e {translated_word} em {weather_now['city']} em {weather_now['dt']}."""
    
    forecast = f""" Média para os próximos dias: {weather_forecast[0]['average_temp']}°C em {weather_forecast[0]['dt']}"""
    
    for i in range(1,len(weather_forecast)):
        if i >= len(weather_forecast) -1:
            forecast += f" e {weather_forecast[i]['average_temp']}°C em {weather_forecast[i]['dt']}."
        else:
            forecast += f", {weather_forecast[i]['average_temp']}°C em {weather_forecast[i]['dt']}"
            
    return weather + forecast