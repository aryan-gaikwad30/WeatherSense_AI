"""
Outdoor Comfort Score Engine

Calculates how comfortable the weather is
for outdoor activities.

Score:
0   = Very Poor
100 = Excellent
"""

def calculate_comfort(weather):

    if not weather:
        return None

    score = 100

    temp = weather["temperature"]
    humidity = weather["humidity"]
    wind = weather["wind_speed"]
    condition = weather["condition"]

    # Temperature

    if temp >= 42:
        score -= 45

    elif temp >= 38:
        score -= 30

    elif temp >= 34:
        score -= 18

    elif temp <= 5:
        score -= 40

    elif temp <= 12:
        score -= 20

    # Humidity

    if humidity >= 90:
        score -= 20

    elif humidity >= 75:
        score -= 10

    # Wind

    if wind >= 40:
        score -= 25

    elif wind >= 25:
        score -= 12

    # Weather Condition

    if condition == "Thunderstorm":
        score -= 50

    elif condition == "Rain":
        score -= 25

    elif condition == "Snow":
        score -= 30

    elif condition == "Drizzle":
        score -= 12

    score = max(0, min(score, 100))

    if score >= 85:
        level = "Excellent"

    elif score >= 70:
        level = "Good"

    elif score >= 50:
        level = "Moderate"

    elif score >= 30:
        level = "Poor"

    else:
        level = "Very Poor"

    return {
        "score": score,
        "level": level
    }