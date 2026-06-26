from flask import Flask, render_template, request
from services.weather_service import get_weather, get_forecast

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    forecast = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            weather = get_weather(city)
            forecast = get_forecast(city)

            for day in forecast.get("forecast", []):
                print(day)

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
        chart_wind=chart_wind
    )

if __name__ == "__main__":
    app.run(debug=True)