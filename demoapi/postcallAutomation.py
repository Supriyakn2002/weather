import requests

# API endpoint
url = "https://reqres.in/api/users"

# Data to be sent in POST request
data = {
    "name": "Supriya",
    "email": "s@2002"
}

# Send POST request
for i in range(1,11):
 response = requests.post(url, json=data)
 print(f"Response Data({i}):")
 
 if response.status_code == 201:
    print(" POST Request Successful!\n")
    print(response.json())
 else:
    print(" Request Failed. Status Code:", response.status_code)
