from xml.etree.ElementTree import indent

import requests

url = 'https://reqres.in/api/users'

# Data to send in the request body
data = {
    "name": "Supriya",
    "email": "s@2002"
}

# Sending the POST request
response = requests.post(url, json=data)

# Checking if the request was successful (201 = Created)
if response.status_code == 201:
    print(" User Created Successfully!")
    print("Response:")
    print(response.json())
else:
    print(" Request Failed!")



