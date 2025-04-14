import requests

url = 'https://reqres.in/api/users?page=1'
response = requests.get(url)

if response.status_code == 200:
    print(" Request Successful!")
    print("Response JSON:")
    data = response.json()['data']

    print("Emails:\n")

    for user in data:
     print(user['email'],end="\n")

else:
    print(" Request Failed!")

