# class methods are methods that are not bound to an instance of a class, but to the
# class itself. They are called with the class name, not an instance of the class.
# The @classmethod decorator is used to define a class method.
#  The first argument of a class method is always the class itself, by convention it is named cls.

from logging import info, INFO, basicConfig
import random
from colorama import Fore
basicConfig(level=INFO, format="%(asctime)s - %(message)s")
info(f"\n{Fore.GREEN}Hello, friend. {Fore.RESET}")

class Playcall:
    plays = ["inside zone run", "outside zone run", "quick pass", "shot pass", "play action", "screen", "draw", "trick play"]

    @classmethod # establishing a class method instead of the default variable method requiring instantiating an object
    def sort(cls, situation):
        info(f"{situation} let's call a {random.choice(cls.plays)}")  

Playcall.sort("1st Down") # calling the class method sort with the class name Playcall and the situation "1st Down" as arguments


