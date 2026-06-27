def build_prompt(
    weather,
    forecast,
    air_quality,
    risk,
    comfort,
    health,
    question,
    history=None
):
    # ==========================
    # Conversation History
    # ==========================

    history_text = ""

    if history:
        for item in history:
            if item["role"] == "user":
                history_text += f"User: {item['message']}\n"
            else:
                history_text += f"Assistant: {item['message']}\n"

    # ==========================
    # Forecast
    # ==========================

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

    # ==========================
    # Final Prompt
    # ==========================

    prompt = f"""
You are WeatherSense AI, an intelligent weather assistant integrated into a Flask web application.

You help users make decisions using ONLY the provided weather data, forecast, AQI, comfort score, risk score, health advisory and conversation history.

Never invent weather information.

If the answer cannot be determined from the supplied data, clearly say so.

Keep answers concise, practical and easy to understand.

==============================
Conversation History
==============================

{history_text}

==============================
Current Weather
==============================

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

==============================
Air Quality
==============================

Estimated AQI:
{air_quality['estimated_aqi']}

Category:
{air_quality['category']}

==============================
Risk Score
==============================

{risk['score']}/100

==============================
Comfort Score
==============================

{comfort['score']}/100

==============================
Health Advisory
==============================

{chr(10).join(health)}

==============================
Forecast
==============================

{forecast_text}

==============================
Current User Question
==============================

{question}

==============================
Instructions
==============================

1. Use the conversation history whenever it is relevant.
2. Use ONLY the supplied weather information.
3. Never invent weather conditions.
4. If the user asks a follow-up question like "What about tomorrow?" or "And in the evening?", use the previous conversation to understand the context.
5. Give practical advice.
6. Keep the answer under 150 words.
7. Answer naturally like a helpful weather assistant.
"""

    return prompt