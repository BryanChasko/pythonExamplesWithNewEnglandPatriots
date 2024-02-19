import re # regular expression module
import colorama

""" logging is a better way to display messages to the user. It allows us to control the verbosity of
 the messages and the destination of the messages. """
from logging import info, INFO, basicConfig
from colorama import Fore
basicConfig(level=INFO, format="%(asctime)s - %(message)s")
info(f"\n{Fore.GREEN}Hello, friend. {Fore.RESET}")

#take input from user when running format_name.py
player_name = input("Enter the name of your favorite\nNew England Patriot of any era: ").strip()
if matches := re.search(r"^(.+), *(.+)$", player_name): # := is the walrus operator, it assigns the value of the expression to the left of the operator to the variable to the right of the operator
     player_name = f"{matches.group(2)} {matches.group(1)}"
info(f"One of your all time favorite {Fore.BLUE}New {Fore.RED}England Patriots{Fore.RESET} is {Fore.BLUE}{player_name}{Fore.RESET}.") # leverage formatted string to display the name variable with color

