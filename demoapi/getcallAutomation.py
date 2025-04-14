import requests

# API endpoint
url = "https://reqres.in/api/users?page=1"

# Loop to make the GET call 10 times
for i in range(1, 11):
    print(f"\n Request #{i}")

    response = requests.get(url)

    if response.status_code == 200:
        print(" Request Successful!")
        data = response.json()

        print(" Emails:")
        for user in data['data']:
            print(user['email'])
    else:
        print(" Request Failed. Status Code:", response.status_code)
