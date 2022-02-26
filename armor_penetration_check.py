import json


#get own ship name
own_ship = "Bismarck"
with open("/run/media/wwtki/d60d4a36-099d-4b4a-b366-0d0a4d73ac33/home/noyb_pos/Games/wargaming-game-center/drive_c/Games/World_of_Warships/replays/0.10.11.0/tempArenaInfo.json") as current_battle:
    list_of_competitors = json.load(current_battle)
    list_of_competing_ships = []
    for player in list_of_competitors["vehicles"]:
        # player["relation"] == 0 means it is the player itself
        if player["relation"] == 0:
            own_ship_id = player["shipId"]

        #player["relation"] == 2 means it is an enemy ship
        if player["relation"] == 2:
            list_of_competing_ships.append(player["shipId"])

print(own_ship_id, list_of_competing_ships)


#get enemy ship name
enemy_ship = "Bismarck"


#check shell type
shell_type = "HE"

extended_list_of_competing_ships = []
with open("/home/wwtki/Documents/ship_specifications.json") as ship_specifications:
    list_of_ship_specifications = json.load(ship_specifications)
    for ship in list_of_ship_specifications:
#        if ship["name"] == own_ship:
        if ship["ship_id"] == own_ship_id:
            own_ship_caliber = ship["main_caliber"]
            own_he_pen = ship["he_pen"]
#        if ship["name"] == enemy_ship:
        if ship["ship_id"] in list_of_competing_ships:
            enemy_ship_id = ship["ship_id"]
            enemy_armour_bow_stern = ship["armour_bow_stern"]
            enemy_armour_belt = ship["armour_belt"]
            enemy_deck_armour = ship["deck_armour"]
            enemy_armour_superstructure = ship["armour_superstructure"]
            extended_ship = {
            "enemy_ship_id": enemy_ship_id,
            "enemy_armour_bow_stern": enemy_armour_bow_stern,
            "enemy_armour_belt": enemy_armour_belt,
            "enemy_deck_armour": enemy_deck_armour,
            "enemy_armour_superstructure": enemy_armour_superstructure
            }
            extended_list_of_competing_ships.append(extended_ship)

print(extended_list_of_competing_ships)
#check for AP overmatch

with open("/home/wwtki/Documents/armour_penetration.json") as armour_penetration:
    list_of_overmatch = json.load(armour_penetration)
    for item in list_of_overmatch:
        if own_ship_caliber >= item["overmatch_caliber"]:
#            print(own_ship_caliber, item["overmatch_caliber"])
            own_overmatch = item["armor_thickness"]
#            print(own_overmatch)
armour_bow_stern_overmatch_on_enemy = False
armour_belt_overmatch_on_enemy = False
deck_armour_overmatch_on_enemy = False
armour_superstructure_overmatch_on_enemy = False
if own_overmatch > enemy_armour_bow_stern:
    armour_bow_stern_overmatch_on_enemy = True
if own_overmatch > enemy_armour_belt:
    armour_belt_overmatch_on_enemy = True
if own_overmatch > enemy_deck_armour:
    deck_armour_overmatch_on_enemy = True
if own_overmatch > enemy_armour_superstructure:
    armour_superstructure_overmatch_on_enemy = True


#check for HE
armour_bow_stern_he_pen_on_enemy = False
armour_belt_he_pen_on_enemy = False
deck_armour_he_pen_on_enemy = False
armour_superstructure_he_pen_on_enemy = False
if own_he_pen > enemy_armour_bow_stern:
    armour_bow_stern_he_pen_on_enemy = True
if own_he_pen > enemy_armour_belt:
#    print(own_he_pen, armour_belt_pen_on_enemy, enemy_armour_belt)
    armour_belt_he_pen_on_enemy = True
#    print(armour_belt_pen_on_enemy)
if own_he_pen > enemy_deck_armour:
    deck_armour_he_pen_on_enemy = True
if own_he_pen > enemy_armour_superstructure:
    armour_superstructure_he_pen_on_enemy = True

print("own ship,", "own main caliber,", "own HE-pen,", "own overmatch")
print(own_ship, own_ship_caliber,own_he_pen, own_overmatch)
print("AP overmatch:", own_overmatch, ", own HE-pen:", own_he_pen)
print("bow,", "belt,", "deck,", "superstructure,", "stern")
print(enemy_armour_bow_stern, enemy_armour_belt, enemy_deck_armour, enemy_armour_superstructure, enemy_armour_bow_stern)
print("HE-pen:", armour_bow_stern_he_pen_on_enemy, armour_belt_he_pen_on_enemy, deck_armour_he_pen_on_enemy, armour_superstructure_he_pen_on_enemy, armour_bow_stern_he_pen_on_enemy)
print("AP overmatch:", armour_bow_stern_overmatch_on_enemy, armour_belt_overmatch_on_enemy, deck_armour_overmatch_on_enemy, armour_superstructure_overmatch_on_enemy, armour_bow_stern_overmatch_on_enemy)