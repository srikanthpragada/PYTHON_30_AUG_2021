import requests

resp = requests.get("https://restcountries.com/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details. Status Code ->", resp.status_code)
    exit()

countries = resp.json()  # array of json objects to list of dict

for country in countries:
    name = country['name']
    if 'capital' in country:
        capital = country['capital']
    else:
        capital = 'None'

    print(f"{name:50} {capital}")
