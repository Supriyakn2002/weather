import requests

# URL for the DELETE call
url = "https://reqres.in/api/users/2"  # Deleting user with ID 2

# Make the DELETE request
response = requests.delete(url)

# Check the response
if response.status_code == 204:
    print(" DELETE Request Successful! (No Content Returned)")
else:
    print(" DELETE Request Failed. Status Code:", response.status_code)
