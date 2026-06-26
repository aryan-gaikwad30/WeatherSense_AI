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

        for day in forecast["forecast"]:
            print(day)

    return render_template("index.html", weather=weather, forecast=forecast)


if __name__ == "__main__":
    app.run(debug=True)