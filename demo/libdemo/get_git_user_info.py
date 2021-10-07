import requests

resp = requests.get("https://api.github.com/users/srikanthpragada")
if resp.status_code != 200:
    print("Sorry! Could not get details. Status Code ->", resp.status_code)
    exit()

details = resp.json()  # json to dict

print(details['name'])
print(details['company'])
print(details['location'])
