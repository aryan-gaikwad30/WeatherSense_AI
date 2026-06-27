from ai.aqi_engine import estimate_aqi, aqi_category

pm25 = 42.5

aqi = estimate_aqi(pm25)

print(aqi)

print(aqi_category(aqi))