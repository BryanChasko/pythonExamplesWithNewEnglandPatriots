import colorama
from logging import info, INFO, basicConfig, error
from colorama import Fore
basicConfig(level=INFO, format="%(asctime)s - %(message)s")

class Patriot: # class is a built in function in python that allows us to create a new object
    def __init__(self, player_name, university): # __init__ is python's function for creating a new object, which must reference itself first if it is to contain multiple objects
        self.player_name = player_name # self is a reference to the object itself, and it is required to access variables that belong to the class
        self.university = university # this is how objects constructed in memory will look to store instance variables (attributes)
        
""" a method is a function that belongs to a class, and it is called an attribute when it is a variable that belongs to a class
in this case, player_name and university are attributes of the Patriot class, and they belong to the object player_dict
and they are accessed using the self reference, and they are set to the values of the arguments passed to the __init__ function 
methods are relevant to object oriented programming in that they allow us to create objects that contain both data and functions that operate on that data
"""

def main():
    player_dict = get_player()
    info(f'{Fore.BLUE}{player_dict.player_name} {Fore.GREEN}played college ball at {Fore.RED}{player_dict.university}{Fore.RESET}')

def get_player():    
    player_name = input("Enter a player's name: ").strip() # here's where we construct the object to store in our init function in memory
    university = input("Enter the player's university: ").strip()
    return Patriot(player_name, university) # we return the object to the main function

if __name__ == "__main__":
    main()