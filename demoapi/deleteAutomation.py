import requests

# URL for the DELETE call
url = "https://reqres.in/api/users/2"  # deleting user with ID 2

# Perform DELETE request 10 times
for i in range(1, 11):
    response = requests.delete(url)

    print(f"Response {i}:")
    if response.status_code == 204:
        print("  DELETE Request Successful! (No Content)\n")
    else:
        print("  DELETE Request Failed. Status Code:", response.status_code)
