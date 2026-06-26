from ai.health_engine import generate_health_advisory

sample = {

    "temperature":41,

    "humidity":70,

    "wind_speed":12,

    "condition":"Clear"

}

print(generate_health_advisory(sample))