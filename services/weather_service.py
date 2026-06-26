import requests
from config import Config
from datetime import datetime


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
        "visibility": round(data["visibility"] / 1000, 1),
        "wind_speed": round(data["wind"]["speed"] * 3.6, 1),
        "condition": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }
def get_forecast(city):

    params = {
        "q": city,
        "appid": Config.OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(
        Config.FORECAST_URL,
        params=params
    )

    data = response.json()

    if response.status_code != 200:
        return {
            "success": False,
            "message": data.get("message", "Something went wrong.")
        }

    forecast = []

    for item in data["list"]:

        if "12:00:00" in item["dt_txt"]:

            forecast.append({

                "date": datetime.strptime(
                     item["dt_txt"],
                     "%Y-%m-%d %H:%M:%S"
                        ).strftime("%a"),

                "temperature": item["main"]["temp"],

                "temp_min": item["main"]["temp_min"],

                "temp_max": item["main"]["temp_max"],

                "description": item["weather"][0]["description"],

                "icon": item["weather"][0]["icon"],

                "humidity": item["main"]["humidity"],

                "wind_speed": round(item["wind"]["speed"] * 3.6, 1),

            })

    return {
        "success": True,
        "forecast": forecast
    }