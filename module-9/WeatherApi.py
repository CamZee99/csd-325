# Cameron Zimmer
# Module 9.2 Assignment

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true"
response = requests.get(url)

if response.status_code == 200:
    print("Weather API connection successful.")
else:
    print(f"Connection failed with status code: {response.status_code}")

print("\nUnfromat Weather Output:")
print(response.text)

data = response.json()
weather = data['current_weather']
print("\nFormatted Weather Output:")
print(f"Temperature: {weather['temperature']}°C")
print(f"Windspeed: {weather['windspeed']} km/h")
print(f"Time: {weather['time']}")
