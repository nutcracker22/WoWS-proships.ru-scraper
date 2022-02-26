import requests
from bs4 import BeautifulSoup
import json

url = "https://wiki.wargaming.net/en/Ship:Armor_thresholds"

website = requests.get(url)
doc4 = BeautifulSoup(website.text, "html.parser")

table = doc4.find_all("table", class_ = "wikitable")
#body = table.find
#print(len(table))
#print(table[3])

overmatch_list = []
for tr_armor in table[3].find_all("tr"):
#    td = line.find_all("td")
#    print(line)
    td = tr_armor.find_all("td")
#    print(td)
    if len(td) > 0:
        armor_thickness = int(td[0].text.split(" ")[1])
        overmatch_caliber = int(td[1].text.split(" ")[1])
        overmatch = {
            'armor_thickness': armor_thickness,
            'overmatch_caliber': overmatch_caliber
        }
        overmatch_list.append(overmatch)
with open("/home/wwtki/Documents/armour_penetration.json", "w") as outfile:
    json.dump(overmatch_list, outfile)

