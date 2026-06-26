"""
Weather Risk Engine (Explainable AI)

Calculates a weather risk score (0–100) using
rule-based expert system logic.

It also returns the reasoning behind the score,
making the prediction explainable (XAI).
"""


def calculate_risk(weather):

    if not weather:
        return None

    score = 0
    reasons = []

    temp = weather["temperature"]
    humidity = weather["humidity"]
    wind = weather["wind_speed"]
    condition = weather["condition"]

    # ----------------------------
    # Temperature
    # ----------------------------

    if temp >= 45:
        score += 35
        reasons.append({
            "factor": f"Temperature ({temp}°C)",
            "impact": "+35"
        })

    elif temp >= 40:
        score += 25
        reasons.append({
            "factor": f"Temperature ({temp}°C)",
            "impact": "+25"
        })

    elif temp >= 35:
        score += 15
        reasons.append({
            "factor": f"Temperature ({temp}°C)",
            "impact": "+15"
        })

    elif temp <= 5:
        score += 20
        reasons.append({
            "factor": f"Temperature ({temp}°C)",
            "impact": "+20"
        })

    else:
        reasons.append({
            "factor": f"Temperature ({temp}°C)",
            "impact": "+0"
        })

    # ----------------------------
    # Humidity
    # ----------------------------

    if humidity >= 90:
        score += 20
        reasons.append({
            "factor": f"Humidity ({humidity}%)",
            "impact": "+20"
        })

    elif humidity >= 75:
        score += 12
        reasons.append({
            "factor": f"Humidity ({humidity}%)",
            "impact": "+12"
        })

    else:
        reasons.append({
            "factor": f"Humidity ({humidity}%)",
            "impact": "+0"
        })

    # ----------------------------
    # Wind
    # ----------------------------

    if wind >= 40:
        score += 20
        reasons.append({
            "factor": f"Wind ({wind} km/h)",
            "impact": "+20"
        })

    elif wind >= 25:
        score += 10
        reasons.append({
            "factor": f"Wind ({wind} km/h)",
            "impact": "+10"
        })

    else:
        reasons.append({
            "factor": f"Wind ({wind} km/h)",
            "impact": "+0"
        })

    # ----------------------------
    # Weather Condition
    # ----------------------------

    if condition == "Thunderstorm":
        score += 30
        reasons.append({
            "factor": "Weather Condition (Thunderstorm)",
            "impact": "+30"
        })

    elif condition == "Rain":
        score += 15
        reasons.append({
            "factor": "Weather Condition (Rain)",
            "impact": "+15"
        })

    elif condition == "Snow":
        score += 20
        reasons.append({
            "factor": "Weather Condition (Snow)",
            "impact": "+20"
        })

    elif condition == "Drizzle":
        score += 8
        reasons.append({
            "factor": "Weather Condition (Drizzle)",
            "impact": "+8"
        })

    else:
        reasons.append({
            "factor": f"Weather Condition ({condition})",
            "impact": "+0"
        })

    # ----------------------------
    # Final Score
    # ----------------------------

    score = min(score, 100)

    if score <= 20:
        level = "Excellent"
        color = "green"

    elif score <= 40:
        level = "Low"
        color = "lime"

    elif score <= 60:
        level = "Moderate"
        color = "orange"

    elif score <= 80:
        level = "High"
        color = "darkorange"

    else:
        level = "Extreme"
        color = "red"

    return {
        "score": score,
        "level": level,
        "color": color,
        "reasons": reasons
    }