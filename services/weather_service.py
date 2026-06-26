import requests
from config import Config


def get_weather(city):
    params = {
        "q": city,
        "appid": Config.OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(Config.BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return {
            "success": False,
            "message": data.get("message", "Something went wrong.")
        }

    return {
        "success": True,
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "visibility": data["visibility"],
        "wind_speed": data["wind"]["speed"],
        "condition": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }