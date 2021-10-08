from bs4 import BeautifulSoup

f = open("products.xml", "rt")
bs = BeautifulSoup(f.read(), "xml")

for prod in bs.find_all("product"):
    name = prod.find("name").text
    price = int(prod.find("price").text)
    qoh = int(prod.find("qoh").text)

    print(f"{name:30} {price:8} {qoh:3}")

f.close()
