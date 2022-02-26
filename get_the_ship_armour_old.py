import requests
from bs4 import BeautifulSoup
import re
import csv
url = "https://proships.ru/stat/ships/4248/"

website = requests.get(url)
doc = BeautifulSoup(website.text, "html.parser")

#specify the header of the csv-file:
header = ['', 'Ship name', '', 'Bow/Stern', 'armour belt', 'deck', 'superstructure']

#create writable csv-file:
with open('/home/wwtki/Documents/ship_armour.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)

#all armour data is inside <div class="iner_container">
    iner = doc.find("div", class_ = "iner_container")
#print(len(iner))
#print(iner)
    tables = iner.find_all("table")
#print(tables)
#print(len(tables))

#inside iner_container are four tables with armour for each ship class: BBs, CVs, cruisers, DDs.
#So we need to loop through all four tables.
    for table in tables:
        for tr in table.find("tbody").find_all("tr", class_="item"):
            armour = []
            for td in tr:
                armour.append(td.text.strip())
            writer.writerow(armour)


#for tr in iner.find_all("tr", class_ = "item"):
#    for td in tr:
#        print(td)

#print(len(divs))
