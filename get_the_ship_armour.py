import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://proships.ru/stat/ships/4248/"

website = requests.get(url)
doc = BeautifulSoup(website.text, "html.parser")

#create an empty list of ship armour:
ship_armour = []

#all armour data is inside <div class="iner_container">
iner = doc.find("div", class_ = "iner_container")
tables = iner.find_all("table")
#print(tables)
#print(len(tables))

#inside iner_container are four tables with armour for each ship class: BBs, CVs, cruisers, DDs.
#So we need to loop through all four tables.
for table in tables:
    for tr in table.find("tbody").find_all("tr", class_="item"):
        td = tr.find_all("td")
        ship = {
#            'tier': td[0].text.strip().split(" ", 1)[0],
            'name': td[0].text.strip().split(" ", 1)[1],
            'armour_bow_stern': td[1].text.strip(),
            'armour_belt': td[2].text.strip(),
            'deck_armour': td[3].text.strip(),
            'armour_superstructure': td[4].text.strip(),
        }
        ship_armour.append(ship)
with open("/home/wwtki/Documents/ship_armour.json", "w") as outfile:
    json.dump(ship_armour, outfile)

