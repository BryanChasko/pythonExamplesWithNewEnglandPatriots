# This file is an example of class-based inheritance in Python.
# As an object-oriented programming language, Python allows us to create classes and objects that can 
# inherit from other classes.

# Import logging and colors to make things pretty and informative
from logging import info, INFO, basicConfig, error
from colorama import Fore, Style
basicConfig(level=INFO, format="%(message)s")

# Create a main class to call the other classes
class Main:
    def __init__(self):
        self.football_players = football_players
        self.coaches = coaches
        self.get_players_and_coaches()

    def get_players_and_coaches(self):
        info(Style.BRIGHT + Fore.GREEN + "\nThe 2004 Patriots quarterbacks and their coaches were:")
        info(Style.RESET_ALL + "-" * 60)
        for player in self.football_players:
            info(Style.BRIGHT + Fore.BLUE + f"{player.name} {Fore.RESET}played {player.position_played}")
        for coach in self.coaches:
            info(Style.BRIGHT + Fore.BLUE + f"Coach {coach[0]} coached {Fore.MAGENTA}{coach[1]}")

# Create a reusable class to get the Patriot's name. This class method will be inherited by other classes
class Patriot2004:
    def __init__(self, name):
        if not name:
            error(Fore.RED + "Name is required") #raise ValueError("Name is required")
        self.name = name.strip()

class Football_Player(Patriot2004): # Our superclass is Patriot, and we establish Football_Player as a subclass
    def __init__(self, name, position_played):
        # We call the __init__ method of the superclass to get the name. We need to do this because we are overriding the
        # __init__ method in order to add the position_played attribute, referring to the initialization method of the superclass
        super().__init__(name) 
        self.position_played = position_played
    
class Coach(Patriot2004):
    def __init__(self, name, position_group_coached):
        self.position_group_coached = position_group_coached

# Define the list of quarterbacks and their positions
quarterbacks = [
    ("Tom Brady", "Quarterback"),
    ("Rohan Davey", "Quarterback"),
    ("Kliff Kingsbury", "Quarterback"),
    ("Kurt Kittner", "Quarterback"),
    ("Jim Miller", "Quarterback")
]

# Create Football_Player instances for each quarterback
football_players = [Football_Player(name, position) for name, position in quarterbacks]

# Define coaches
coaches = [
    ("Charlie Weis", "Offensive Coordinator"),
    ("Josh McDaniels", "Quarterbacks"),
    ("Jeff Weeks", "Assistant Strength and Conditioning"),
    ("Mike Woicik", "Strength and Conditioning"),
    ("Bill Belichick", "Head Coach, General Manager")
]

# Ask the user if they want to learn about the 2004 Patriots quarterbacks
user_input = input("Do you want to learn about the 2004 Patriots quarterbacks? (Y/N): ").strip().lower()
if user_input in ["y", "yes"]:
    if football_players: # Check if there are quarterbacks to display
        pass
else:
    info(Fore.RED + "Whatever, Jets fan.") 
    
# Call main to start the program
if __name__ == "__main__":
    Main()
