import os
import json
import urllib.request
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=48.14&lon=17.10"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "IvanLinuxWeather/0.1"})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            
        os.system("logger 'Weather API called successfully'")
        
        first = data["properties"]["timeseries"][0]
        details = first["data"]["instant"]["details"]
        
        return render_template(
            "index.html",
            temperature=details["air_temperature"],
            wind=details["wind_speed"],
            humidity=details["relative_humidity"],
            city="Bratislava"
        )
    except Exception as e:
        os.system(f"logger 'WEATHER API ERROR: {e}'")
        return f"Error loading weather data: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
