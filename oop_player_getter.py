from logging import info, INFO, basicConfig
from colorama import Fore
basicConfig(level=INFO, format="%(asctime)s - %(message)s")

class Patriot:
    def __init__(self, player_name, university, university_mascot=None):
        if not player_name:
            raise ValueError(f'{Fore.RED}"Player name cannot be empty.{Fore.RESET}"')
        if player_name.strip().lower() in ["tom", "brady"]:
            player_name = "\nThe GOAT 🐐: Tom Brady"
        if university.strip().lower() == "michigan":
            university = f"{Fore.BLUE}M{Fore.RESET}ichigan"
            university_mascot = "Wolverines"
        elif university.lower() == "nmsu":
            university_mascot = "Aggies"
        elif university.lower() == "ohio state":
            university_mascot = "Buckeyes"
        elif university.lower() == "lsu":
            university_mascot = "Tigers"
        elif university.lower() == "alabama":
            university_mascot = "Roll Tide"
        else:
            university_mascot = "Football Team"
        self.player_name = player_name
        self.university = university
        self.university_mascot = university_mascot

    def __str__(self):
        return f"{self.player_name} played college ball 🏈 for the {self.university} {self.university_mascot}"
    
    def university_emoji(self):
        match self.university_mascot.lower():
            case "wolverines":
                return '🐾🐻'
            case "aggies":
                return '🐮🔔'
            case "buckeyes":
                return '🌰'
            case "tigers":
                return '🐯'
            case "roll tide" | "crimson tide" | "alabama":
                return '🐘'
            case None | "football team" | "football":
                return '🎓'
        
""" a method is a function that belongs to a class, and it is called an attribute when it is a variable that belongs to a class
in this case, player_name and university are attributes of the Patriot class, and they belong to the object player_dict
and they are accessed using the self reference, and they are set to the values of the arguments passed to the __init__ function 
 methods are relevant to object oriented programming in that they allow us to create objects that contain both data and functions that operate on that data
"""

def main():
    player_dict = get_player()
    info(f'{player_dict} {player_dict.university_emoji()}')

def get_player():    
    player_name = input("Enter a player's name: ").strip() # here's where we construct the object to store in our init function in memory
    university = input("Enter the player's university: ").strip()
    return Patriot(player_name, university) # we return the object to the main function

if __name__ == "__main__":
    main()