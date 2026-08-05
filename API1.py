import requests

import json

url = 'http://ip-api.com/json/'

response = requests.get(url).json()

print(response)

for key, value in response.items():
    print(f"{key} -- {value}")

print(json.dumps(response, indent=2))

print(f"You are In This City: {response['city']}")

