import requests
import re
from bs4 import BeautifulSoup
import json


url = "https://proships.ru/stat/ru/ships/"

overview_website = requests.get(url)
all_ships = BeautifulSoup(overview_website.text, "html.parser")

#find all the links to ships in the overview website and create a list of them
link_to_ships = []
list_of_ships = all_ships.find_all("div", class_ = "ships_ship")
for item in list_of_ships:
    for link in item.find_all("a"):
        link_to_ships.append(link.get("href"))

#create the list of ship specifications
list_of_ship_specs = []

#loop through the list of ship-urls
for link in link_to_ships:
    website = requests.get(link)
    doc = BeautifulSoup(website.text, "html.parser")

    #retrieve ship specifications
    #each specification in a try-except-block, in case the spec is not found on the website
    ship_name = doc.h1.text
    try:
        health = int(doc.find("div", id="health").text)
    except:
        health = None
    try:
        max_speed = float(doc.find("div", id="maxspeed").text.split(" ")[0])
    except:
        max_speed = None
    try:
        sea_detect = float(doc.find("div", id="visibilityfactor").text.split(" ")[0])
    except:
        sea_detect = None
    try:
        air_detect = float(doc.find("div", id="visibilityfactorbyplane").text.split(" ")[0])
    except:
        air_detect = None
    try:
        gun_container = doc.find("section", id="GUN")
        for line in gun_container.find_all("span", text=re.compile("Caliber")):
            parent = line.find_parent('div')
            parents_parent = parent.find_parent("div")
            caliber_mm = parents_parent.find_all("div")[1].text
            main_caliber = int(caliber_mm.replace("m", ""))
    except:
        main_caliber = None
    try:
        he_pen = int(doc.find("div", id="gun_he_alphapiercinghe").text.replace("m", ""))
    except:
        he_pen = None
    with open("/home/wwtki/Documents/ship_IDs.json") as json_file_1:
        list_of_ship_IDs = json.load(json_file_1)
        ship_id = None
        tier = None
        for ship_IDs in list_of_ship_IDs:
            if ship_IDs["name"] == ship_name:
                ship_id = int(ship_IDs["ship_id"])
                tier = ship_IDs["tier"]

        with open("/home/wwtki/Documents/ship_armour.json") as json_file_3:
            list_of_ship_armour = json.load(json_file_3)
            armour_bow_stern = None
            armour_belt = None
            deck_armour= None
            armour_superstructure = None
            for ship_armour in list_of_ship_armour:
                if ship_armour["name"] == ship_name:
                    #tier = ship_armour["tier"]
                    armour_bow_stern = int(ship_armour["armour_bow_stern"])
                    armour_belt = int(ship_armour["armour_belt"])
                    deck_armour = int(ship_armour["deck_armour"])
                    armour_superstructure = int(ship_armour["armour_superstructure"])

            #create a dictionary entry for each ship and append it to the list
            ship = {
                'tier': tier,
                'nation': None,
                'ship_class': None,
                'name': ship_name,
                'ship_id': ship_id,
                'ship_health': health,
                'max_speed': max_speed,
                'sea_detect': sea_detect,
                'air_detect': air_detect,
                'main_caliber': main_caliber,
                'he_pen': he_pen,
                'armour_bow_stern': armour_bow_stern,
                'armour_belt': armour_belt,
                'deck_armour': deck_armour,
                'armour_superstructure': armour_superstructure
            }
            list_of_ship_specs.append(ship)

with open("/home/wwtki/Documents/ship_specifications.json", "w") as specifications:
        json.dump(list_of_ship_specs, specifications)
