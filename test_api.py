import json

with open("forecast.json") as f:

    data = json.load(f)

first = data ["properties"]["timeseries"][0]

print(first["time"])
details = first["data"]["instant"]["details"]

print(first["time"])
print(details["air_temperature"])
print(details["wind_speed"])
print(details["relative_humidity"])
