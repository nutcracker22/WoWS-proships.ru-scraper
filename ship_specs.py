import requests
from bs4 import BeautifulSoup

url = "https://proships.ru/stat/ships/4216/"

website = requests.get(url)
doc = BeautifulSoup(website.text, "html.parser")

ship_name = doc.h1.text

# try:
#     health = doc.find("div", id="health").text
# except:
#     health = None
# try:
#     max_speed = doc.find("div", id="maxspeed").text.split(" ")[0]
# except:
#     max_speed = None
# try:
#     sea_detect = doc.find("div", id="visibilityfactor").text.split(" ")[0]
# except:
#     sea_detect = None
# try:
#     air_detect = doc.find("div", id="visibilityfactorbyplane").text.split(" ")[0]
# except:
#     air_detect = None
# try:
#     gun_container = doc.find("section", id="GUN")
#     for line in gun_container.find_all("span", text=re.compile("Caliber")):
#         parent = line.find_parent('div')
#         parents_parent = parent.find_parent("div")
#         caliber_mm = parents_parent.find_all("div")[1].text
#         caliber = caliber_mm.replace("m", "")
# except:
#     caliber = None

try:
    he_pen = doc.find("div", id="gun_he_alphapiercinghe").text.replace("m", "")
except:
    he_pen = None
print(he_pen)

#print(doc)


#armour_pen = {}
#try:
#    first_step = doc.find('div', 'aria-label'="A chart.")
#    find_all("span", text=re.compile("Caliber")):
#    ("div", id="visibilityfactorbyplane")
#    g_tags = doc.find_all('div') #, attrs={"aria-label": True})
#    print(g_tags)
#    print(first_step)
#    armour_pen = doc.find("div", id="health").text
#except:
#    health = None


#print(ship_name, health, max_speed, sea_detect, air_detect, caliber)

