import colorama
from logging import info, INFO, basicConfig, error
from colorama import Fore
basicConfig(level=INFO, format="%(asctime)s - %(message)s")

def main():
    """ (player_name, university) = get_player() """ # use a comma to create a tuple, similar ot a list but immutable. () add clarity this is a touple.
    player_tuple = get_player()
    if player_tuple[0] == "Tom Brady":
            player_tuple[0] = "🐐 Tom Brady"
    info(f'{Fore.BLUE}{player_tuple[0]} {Fore.GREEN}went to college at {Fore.RED}{player_tuple[1]}')

def get_player():
    player_name = input("Enter the player's name: ").strip()
    university = input("Where'd they play college ball? ").strip()
    return [player_name, university] # adding brackets around the return value makes it a list instead of a tuple.

if __name__ == "__main__":
    main()