import requests

# URL for the PUT call
url = "https://reqres.in/api/users/2"  # updating user with ID 2

# Data to update = payload
payload = {
    "name": "Supriya",
    "job": "student"
}

# Make the PUT request
response = requests.put(url, json=payload)

# Check the response
if response.status_code == 200:
    print(" PUT Request Successful!\n")
    print(" Updated Data:")
    print(response.json())
else:
    print(" PUT Request Failed. Status Code:", response.status_code)
