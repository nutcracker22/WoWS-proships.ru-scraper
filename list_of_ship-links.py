import requests
from bs4 import BeautifulSoup

url = "https://proships.ru/stat/ru/ships/"

overview_website = requests.get(url)
all_ships = BeautifulSoup(overview_website.text, "html.parser")

link_to_ships = []
list_of_ships = all_ships.find_all("div", class_ = "ships_ship")
for item in list_of_ships:
#    links_to_ships = item.find_all("a")
    for link in item.find_all("a"):
#        print(link.get("href"))
        link_to_ships.append(link.get("href"))
print(link_to_ships)
print(len(link_to_ships))



