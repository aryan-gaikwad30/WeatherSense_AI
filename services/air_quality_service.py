"""
Air Quality Service

Handles communication with the
OpenWeather Air Pollution API.
"""

import requests

from config import Config

from ai.aqi_engine import (
    estimate_aqi,
    aqi_category,
    aqi_color
)


def get_air_quality(latitude, longitude):

    url = (
        f"{Config.AIR_POLLUTION_URL}"
        f"?lat={latitude}"
        f"&lon={longitude}"
        f"&appid={Config.OPENWEATHER_API_KEY}"
    )

    try:

        response = requests.get(url)
        data = response.json()

        if "list" not in data:
            return {
                "success": False,
                "message": "Unable to fetch air quality."
            }

        air = data["list"][0]

        # Raw OpenWeather AQI (1–5)
        aqi = air["main"]["aqi"]

        labels = {
            1: "Good",
            2: "Fair",
            3: "Moderate",
            4: "Poor",
            5: "Very Poor"
        }

        # Pollutants
        pm25 = air["components"]["pm2_5"]
        pm10 = air["components"]["pm10"]
        co = air["components"]["co"]

        # Estimated AQI
        estimated_aqi = estimate_aqi(pm25)
        category = aqi_category(estimated_aqi)
        color = aqi_color(estimated_aqi)

        return {

            "success": True,

            # Raw OpenWeather AQI
            "aqi": aqi,
            "label": labels.get(aqi, "Unknown"),

            # Estimated AQI
            "estimated_aqi": estimated_aqi,
            "category": category,
            "color": color,

            # Pollutants
            "pm2_5": pm25,
            "pm10": pm10,
            "co": co

        }

    except Exception as e:

        print(e)

        return {

            "success": False,
            "message": "Unable to fetch air quality."

        }