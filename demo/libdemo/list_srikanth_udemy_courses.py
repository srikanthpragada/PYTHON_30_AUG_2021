# Print all udemy course titles from srikanthtechnologies.com

from bs4 import BeautifulSoup
import requests

URL = "http://www.srikanthtechnologies.com"
resp = requests.get(URL)
contents = resp.text

bs = BeautifulSoup(contents, 'html.parser')

images = bs.find_all("img")
for img in images:
    source = img['src']
    if source.startswith("udemy"):
        title = img['title']
        pos = title.find("-")
        print(title[pos + 1:].strip())
        parent = img.parent   # Parent tag for img which is <a>
        print(URL + "/" + parent['href'])  # Convert relative URL to absolute

