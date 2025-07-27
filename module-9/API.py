# Cameron Zimmer
# Module 9.2 Assignment

import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

if response.status_code == 200:
    print("OpenNotify API connection successful.")
else:
    print(f"Connection failed with status code: {response.status_code}")

data = response.json()
print("\nFormatted Astronaut Output:")
print(f"There are {data['number']} people in space:\n")
for person in data['people']:
    print(f"- {person['name']} is on the {person['craft']}")
