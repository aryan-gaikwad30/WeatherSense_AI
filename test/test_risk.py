from ai.risk_engine import calculate_risk

sample = {
    "temperature": 41,
    "humidity": 78,
    "wind_speed": 18,
    "condition": "Clear"
}

print(calculate_risk(sample))