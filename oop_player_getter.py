from logging import info, INFO, basicConfig
from colorama import Fore
basicConfig(level=INFO, format="%(asctime)s - %(message)s")

def main(): # we don't call main till the end of the script, so its ok to call the class Patriot before we definet it
    player_dict = Patriot.get() # calling the class method get with the class name Patriot
    info(f'{player_dict}')

class Patriot:
    def __init__(self, player_name, university):
        self.player_name = player_name
        self.university = university

    def __str__(self):
        return f"{self.player_name} played college ball 🏈 for {self.university}"
    
    @classmethod # inside the Patriot function we create a class method "get" we can call without instantiating an object
    def get(cls):
        player_name = input("Enter the Patriot player's name: ")
        university = input(f"What University did {player_name} go to? ")
        return cls(player_name, university) # returns a new player_name and university as arguments to the class Patriot when get is called on Patriot.

if __name__ == "__main__":
    main()