import requests
from bs4 import BeautifulSoup
import json
import os

with open("/home/wwtki/Documents/ship_specifications.json") as print_specifications:
    list_of_ship_specs = json.load(print_specifications)
    for ship3 in list_of_ship_specs:
        for item in ship3:
            if not(ship3[item] == None):
                print(item, ship3[item], end = ",")
        print()
