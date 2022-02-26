import requests
import re
from bs4 import BeautifulSoup
import json
import os

#search folder to create a list of all json-files in that folder
list_of_json_files = []
for x in os.listdir("/run/media/wwtki/d60d4a36-099d-4b4a-b366-0d0a4d73ac33/home/noyb_pos/Documents/wows2/"):
    if x.endswith(".json"):
        list_of_json_files.append(x)
        list_of_json_files.sort()

#search folder to create a list of all html-files in that folder
list_of_html_files = []
for y in os.listdir("/run/media/wwtki/d60d4a36-099d-4b4a-b366-0d0a4d73ac33/home/noyb_pos/Documents/wows2/"):
    if y.endswith(".html"):
        list_of_html_files.append(y)
        list_of_html_files.sort()

#just run the following code, if the number of json-files matches the number of html-files
if len(list_of_json_files) == len(list_of_html_files):

    #create a list of ship-IDs
    list_of_shipIDs = []

    #at first loop through all json files, but use n as n-th element of the list,
    #to later look for the same element in the html-list
    for n in range(0, len(list_of_json_files)):
        with open("/run/media/wwtki/d60d4a36-099d-4b4a-b366-0d0a4d73ac33/home/noyb_pos/Documents/wows2/" + list_of_json_files[n]) as json_file:
            data = json.load(json_file)

            # at second open local html-file
            with open("/run/media/wwtki/d60d4a36-099d-4b4a-b366-0d0a4d73ac33/home/noyb_pos/Documents/wows2/" + list_of_html_files[n]) as f:
                local_html = BeautifulSoup(f, "html.parser")

                #find all player names from json and loop through them
                for player in data["vehicles"]:
                    ship_id = player["shipId"]
                    player_name = player["name"]

                    #find all player names in local html and loop through them
                    for player_list_html in local_html.find_all("span", class_="playerName textLink"):
                        player_html = player_list_html.text

                        #if player names from html and json match, then find and retrieve ship name
                        if player_html == player_name:
                            another_parent = player_list_html.find_parent("div")
                            another_parents_parent = another_parent.find_parent("div")
                            ship_container_name = another_parents_parent.find("span", class_ ="shipName")
                            ship_name = ship_container_name.text
                            ship_container_tier = another_parents_parent.find("span", class_="shipTier")
                            tier = ship_container_tier.text

                        ship = {
                                'tier': None,
#                                'nation': None,
                                'name': ship_name,
                                'ship_id': ship_id,
#                                'ship_health': None,
#                                'max_speed': None,
#                                'sea_detect': None,
#                                'air_detect': None,
#                                'main_caliber': None
                            }
                    list_of_shipIDs.append(ship)

    #remove duplicates from list
    res_list = [i for n, i in enumerate(list_of_shipIDs) if i not in list_of_shipIDs[n + 1:]]
    with open("/home/wwtki/Documents/ship_IDs.json", "w") as outfile:
        json.dump(res_list, outfile)
else:
    print(str(len(list_of_json_files)) + " .json files in this folder, but only " + str(len(list_of_html_files)) + " .html files.")
