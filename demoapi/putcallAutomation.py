import requests

# URL for the PUT call
url = "https://reqres.in/api/users/2"  # updating user with ID 2

# Data to update
payload = {
    "name": "Supriya",
    "job": "Cybersecurity Engineer"
}

# Make the PUT request
for i in range(1,11):
 response = requests.put(url, json=payload)

 print(f"Response {i}:")
# Check the response
 if response.status_code == 200:
    print(" PUT Request Successful!\n")
    print(" Updated Data:")
    print(response.json())
 else:
    print(" PUT Request Failed. Status Code:", response.status_code)
