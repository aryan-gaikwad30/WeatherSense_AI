def build_prompt(
    weather,
    forecast,
    air_quality,
    risk,
    comfort,
    health,
    question
):

    forecast_text = ""

    if forecast and forecast.get("success"):

        tomorrow = forecast["forecast"][0]

        forecast_text = f"""
Tomorrow Forecast

Temperature:
{tomorrow['temperature']}°C

Condition:
{tomorrow['description']}
"""

    prompt = f"""
You are WeatherSense AI, an intelligent weather assistant integrated into a Flask web application.

You help users make decisions using ONLY the provided weather data, forecast, AQI, comfort score, risk score, and health advisory.

Never invent weather information.

If the answer cannot be determined from the supplied data, clearly say so.

Keep answers concise, practical, and easy to understand.

Answer only using the weather information below.

Current Weather

City:
{weather['city']}

Temperature:
{weather['temperature']}°C

Feels Like:
{weather['feels_like']}°C

Humidity:
{weather['humidity']}%

Wind:
{weather['wind_speed']} km/h

Condition:
{weather['description']}

Air Quality

Estimated AQI:
{air_quality['estimated_aqi']}

Category:
{air_quality['category']}

Risk Score

{risk['score']}/100

Comfort Score

{comfort['score']}/100

Health Advisory

{chr(10).join(health)}

{forecast_text}

User Question

{question}

Instructions

1. Answer naturally.
2. Keep it under 150 words.
3. Give practical advice.
4. Do not invent weather data.
"""

    return prompt