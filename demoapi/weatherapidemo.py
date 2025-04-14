"""import requests

city = "Bangalore"
url = f"https://wttr.in/{city}?format=3"  # simple one-line weather

response = requests.get(url)

if response.status_code == 200:
    print("🌤️ Current Weather:")
    print(response.text)
else:
    print(" Could not fetch weather.")"""

import requests

api_key = "6ae6374f708f42438ae93531250904"  # replace with your actual API key
city = "Bangalore"
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f" {city} Weather:")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")
    print(f"Humidity: {data['current']['humidity']}%")
else:
    print(" Failed to retrieve weather data.")

