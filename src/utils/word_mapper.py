
weather_conditions = {
    "clear": "céu limpo",
    "clouds": "nublado",
    "rain": "chuva",
    "drizzle": "garoa",
    "thunderstorm": "tempestade",
    "snow": "neve",
    "mist": "neblina",
    "smoke": "fumaça",
    "haze": "nevoeiro",
    "fog": "nevoeiro",
    "sand": "areia",
    "dust": "poeira",
    "ash": "cinzas",
    "squall": "rajada",
    "tornado": "tornado",
}

def get_word(word: str) -> str:
    for key,value in weather_conditions.items():
        if key == word.lower():
            return value
    return word