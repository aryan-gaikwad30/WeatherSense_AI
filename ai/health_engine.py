"""
Health Advisory Engine

Generates health-related recommendations
based on current weather conditions.
"""


def generate_health_advisory(weather):

    if not weather:
        return None

    advice = []

    temp = weather["temperature"]
    humidity = weather["humidity"]
    wind = weather["wind_speed"]
    condition = weather["condition"]

    # Temperature

    if temp >= 40:

        advice.append(
            "💧 Drink at least 3-4 liters of water today."
        )

        advice.append(
            "🧴 Apply sunscreen before going outdoors."
        )

        advice.append(
            "😎 Wear sunglasses and a cap."
        )

    elif temp >= 32:

        advice.append(
            "💧 Stay hydrated throughout the day."
        )

    elif temp <= 10:

        advice.append(
            "🧥 Wear warm clothing."
        )

    # Humidity

    if humidity >= 80:

        advice.append(
            "🌫 High humidity may cause discomfort."
        )

    # Wind

    if wind >= 30:

        advice.append(
            "🌬 Strong winds expected. Secure loose belongings."
        )

    # Weather

    if condition == "Rain":

        advice.append(
            "☔ Carry an umbrella."
        )

    elif condition == "Thunderstorm":

        advice.append(
            "⚡ Avoid open outdoor areas."
        )

    elif condition == "Clear":

        advice.append(
            "🚶 Good weather for light outdoor activities."
        )

    return advice