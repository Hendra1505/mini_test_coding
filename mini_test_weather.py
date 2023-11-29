import requests as req
from datetime import datetime

url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "q": "Jakarta",
    "appid": "bfe0650a525e5de81893acd214b01a75",  
    "units": "metric",
    "cnt": 5 
}

res = req.get(url, params=params)

if res.status_code == 200:
    data = res.json()
    print("Weather Forecast:")
    for forecast in data['list']:
        timestamp = forecast['dt']
        date = datetime.utcfromtimestamp(timestamp)
        day_name = date.strftime('%A')
        formatted_date = date.strftime('%Y-%m-%d')
        temperature = forecast['main']['temp']
        print(f"{day_name}, {formatted_date}: {temperature}°C")
else:
    print("There is no update about weather today")