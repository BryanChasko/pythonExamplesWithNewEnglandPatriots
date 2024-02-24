import csv
from logging import INFO, basicConfig, info

basicConfig(level=INFO, format="%(message)s")

patriots_players = []

with open("names.csv") as file:
      reader = csv.DictReader(file)
      for row in reader: 
           patriots_players.append({"name": row["name"], "position": row["position"], "college": row["college"], "highschool": row["highschool"], "hometown": row["hometown"], "homestate": row["homestate"]})

for patriots_player in sorted(patriots_players, key=lambda patriots_player: patriots_player["homestate"], reverse=True):
    info(f"{patriots_player['name']} is a {patriots_player['position']} from {patriots_player['hometown']},{patriots_player['homestate']}")

""" example 1 from logging import INFO, basicConfig, info

basicConfig(level=INFO, format="%(message)s")

patriots_players = []

with open("names.csv") as file:
    for line in file:
        name,position,college,highschool,hometown,homestate= line.rstrip().split(",")
        patriots_player = {
            "name": name,
            "position": position,
            "college": college,
            "highschool": highschool,
            "hometown": hometown,
            "homestate": homestate
        }
        patriots_players.append(patriots_player)


for patriots_player in sorted(patriots_players, key=lambda patriots_player: patriots_player["homestate"], reverse=True):
    info(f"{patriots_player['name']} is a {patriots_player['position']} from {patriots_player['hometown']},{patriots_player['homestate']}") """

""" example 2 from logging import INFO, basicConfig, info

basicConfig(level=INFO, format="%(message)s")

with open("names.csv") as file:
    for line in file:
        name,position,college,highschool,hometown,homestate= line.rstrip().split(",")
        info(f"{name} is a {position} from {hometown},{homestate}") """