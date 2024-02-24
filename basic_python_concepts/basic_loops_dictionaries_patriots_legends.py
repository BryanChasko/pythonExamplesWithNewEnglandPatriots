# patriots_legends.py

# Demonstrating loops and dictionaries with New England Patriots legends

# Create a list of dictionaries, each holding a player's name, position, and college
patriots_legends = [
    {"name": "John Hannah", "position": "Offensive Guard", "college": "Alabama"},
    {"name": "Tom Brady", "position": "Quarterback", "college": "Michigan"},
    {"name": "Andre Tippett", "position": "Linebacker", "college": "Iowa"},
    {"name": "Gino Cappelletti", "position": "Wide Receiver/Kicker", "college": "Minnesota"},
    {"name": "Steve Grogan", "position": "Quarterback", "college": "Kansas State"}
]

# Loop through the list of dictionaries and print each player's information
for legend in patriots_legends:
    print(legend["name"], ", Position: ", legend["position"], ", College: ", legend["college"])

"""
Example 2: Using a list for a more focused output

# Create a list of just the players' names
players_names = [legend["name"] for legend in patriots_legends]

# Print each player's name preceded by their number in the list
for i in range(len(players_names)):
    print(i + 1, players_names[i])
"""