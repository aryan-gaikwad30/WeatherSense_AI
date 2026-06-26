from ai.comfort_engine import calculate_comfort

sample = {
    "temperature": 32,
    "humidity": 55,
    "wind_speed": 10,
    "condition": "Clear"
}

print(calculate_comfort(sample))