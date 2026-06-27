from flask import Flask, render_template, request, jsonify

from services.weather_service import (
    get_weather,
    get_forecast,
    get_weather_by_coordinates
)

from ai.weather_ai import generate_summary
from ai.risk_engine import calculate_risk
from ai.comfort_engine import calculate_comfort
from ai.health_engine import generate_health_advisory
from ai.prompt_builder import build_prompt
from ai.gemini_engine import ask_gemini

from services.air_quality_service import get_air_quality


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    weather = None
    forecast = None
    ai_summary = None
    risk = None
    comfort = None
    health = None
    air_quality = None
    city = None
    gemini_response = None

    if request.method == "POST":
        city = request.form.get("city")
    elif request.method == "GET":
        city = request.args.get("city")

    if city:
        weather = get_weather(city)

        if weather.get("success"):
            ai_summary = generate_summary(weather)
            risk = calculate_risk(weather)
            comfort = calculate_comfort(weather)
            health = generate_health_advisory(weather)
            air_quality = get_air_quality(
                weather["latitude"],
                weather["longitude"]
            )
            forecast = get_forecast(city)
            question = request.form.get("question")

            if question:
                prompt = build_prompt(
                    weather,
                    forecast,
                    air_quality,
                    risk,
                    comfort,
                    health,
                    question
                )
                gemini_response = ask_gemini(prompt)

    chart_labels = []
    chart_temps = []
    chart_humidity = []
    chart_wind = []

    if forecast and forecast.get("success"):
        chart_labels = [day["date"] for day in forecast["forecast"]]
        chart_temps = [day["temperature"] for day in forecast["forecast"]]
        chart_humidity = [day["humidity"] for day in forecast["forecast"]]
        chart_wind = [day["wind_speed"] for day in forecast["forecast"]]

    return render_template(
        "index.html",
        weather=weather,
        forecast=forecast,
        chart_labels=chart_labels,
        chart_temps=chart_temps,
        chart_humidity=chart_humidity,
        chart_wind=chart_wind,
        ai_summary=ai_summary,
        risk=risk,
        comfort=comfort,
        health=health,
        air_quality=air_quality,
        gemini_response=gemini_response
    )


@app.route("/location", methods=["POST"])
def location_weather():

    data = request.get_json()

    latitude = data.get("latitude")
    longitude = data.get("longitude")

    weather = get_weather_by_coordinates(latitude, longitude)

    if not weather["success"]:
        return jsonify(weather), 400

    forecast = get_forecast(weather["city"])

    ai_summary = generate_summary(weather)

    risk = calculate_risk(weather)

    comfort = calculate_comfort(weather)

    health = generate_health_advisory(weather)

    air_quality = get_air_quality(
        weather["latitude"],
        weather["longitude"]
    )

    return jsonify({

        "weather": weather,

        "forecast": forecast,

        "ai_summary": ai_summary,

        "risk": risk,

        "comfort": comfort,

        "health": health,

        "air_quality": air_quality

    })


if __name__ == "__main__":
    app.run(debug=True)