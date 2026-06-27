from ai.prompt_builder import build_prompt
from ai.gemini_engine import ask_gemini

weather = {
    "city": "Delhi",
    "temperature": 35,
    "feels_like": 39,
    "humidity": 70,
    "wind_speed": 12,
    "description": "Cloudy"
}

forecast = {
    "success": True,
    "forecast": [
        {
            "temperature": 33,
            "description": "Light rain"
        }
    ]
}

air_quality = {
    "estimated_aqi": 71,
    "category": "Satisfactory"
}

risk = {
    "score": 28
}

comfort = {
    "score": 65
}

health = [
    "Stay hydrated",
    "Wear light clothing"
]

prompt = build_prompt(
    weather,
    forecast,
    air_quality,
    risk,
    comfort,
    health,
    "Should I go jogging today?"
)

print(ask_gemini(prompt))