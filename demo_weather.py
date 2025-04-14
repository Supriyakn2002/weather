import requests

api_key = "6ae6374f708f42438ae93531250904"

city = input("Enter city name: ")

url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"\n Weather in {city.title()}:")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")
    print(f"Humidity: {data['current']['humidity']}%")
else:
    print(" Failed to retrieve weather data. Please check the city name or API key.")
