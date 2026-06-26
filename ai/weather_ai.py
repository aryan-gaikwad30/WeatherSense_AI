"""
AI Recommendation Engine

Generates explainable weather recommendations
using rule-based expert system logic.
"""


def generate_summary(weather):

    if not weather:
        return None

    temp = weather["temperature"]
    humidity = weather["humidity"]
    wind = weather["wind_speed"]
    condition = weather["condition"]

    result = {}

    # Weather Summary
    if temp >= 40:
        result["weather"] = "Extreme heat is expected today."
    elif temp >= 32:
        result["weather"] = "Hot weather is expected today."
    elif temp >= 20:
        result["weather"] = "Pleasant weather is expected."
    else:
        result["weather"] = "Cold weather is expected."

    # Clothing
    if temp >= 35:
        result["clothing"] = "Wear light cotton clothing."
    elif temp >= 20:
        result["clothing"] = "A light jacket is optional."
    else:
        result["clothing"] = "Wear warm clothing."

    # Activity
    if condition == "Rain":
        result["activity"] = "Indoor activities are recommended."
    elif temp >= 38:
        result["activity"] = "Outdoor activities are best before 10 AM or after 5 PM."
    else:
        result["activity"] = "Good weather for outdoor activities."

    # Hydration
    if temp >= 35:
        result["hydration"] = "Drink plenty of water today."
    else:
        result["hydration"] = "Stay hydrated."

    # Warning
    if temp >= 40:
        result["warning"] = "Avoid prolonged exposure to direct sunlight."
    elif wind >= 25:
        result["warning"] = "Strong winds are expected."
    elif humidity >= 85:
        result["warning"] = "High humidity may cause discomfort."
    else:
        result["warning"] = "No significant weather warnings."

    return result