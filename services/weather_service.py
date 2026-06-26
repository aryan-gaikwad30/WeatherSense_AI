from urllib import response

import requests
from config import Config


def get_weather(city):
    url = Config.BASE_URL

    params = {
        "q": city,
        "appid": Config.OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    return response.json()