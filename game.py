import time
import random
import json

### TODO this little bit lays the framework for restorative effects (potions/ food)
### work on making variables uniform

def pot_effects():

    with open("items.json", "r") as jsonItems:
        data = json.load(jsonItems)
    with open("game_stats.json", "r") as jsonFile:
        data1 = json.load(jsonFile)

    health = data1["player_character"]["health"]
    pot = data["potions"]["sm_pot"]["rest_effects"]
    updt_health = health + pot

    data1["player_character"]["health"] = updt_health

    with open("game_stats.json", "w") as jsonFile:
        json.dump(data1, jsonFile)
    with open("items.json", "w") as jsonItems:
        json.dump(data, jsonItems)







def write():

    print("Hello, this is a test")

    with open("game_stats.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["player_character"]["name"] = input("What is your name? ")

    with open("game_stats.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    print("your name is " + (data["player_character"]["name"]))


# TODO pretty weak combat system, need to improve

def combat():

    with open("game_stats.json", "r") as jsonFile:
        data = json.load(jsonFile)
    while data["player_character"]["health"] >= 0:
        data["player_character"]["health"] = data["player_character"]["health"] - 1

    with open("game_stats.json", "w") as jsonFile:
        json.dump(data, jsonFile)








### TODO - define functions to load/ edit json file

# def json_read():
#     x = open("game_stats.json", "r")
#     y = x.read()
#     z = json.loads(y)
#
#     read = (z["player_character"]["health"])
#     print(read)
#
#
# json_read()

