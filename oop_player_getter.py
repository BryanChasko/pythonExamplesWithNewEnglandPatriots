import colorama
from logging import info, INFO, basicConfig, error
from colorama import Fore
basicConfig(level=INFO, format="%(asctime)s - %(message)s")

class Player: 
    ...  # creating a class called Player

def main():
    player_dict = get_player()
    info(f'{Fore.BLUE}{player_dict.player_name} {Fore.GREEN}went to college at {Fore.RED}{player_dict.university}{Fore.RESET}')

def get_player():    
    player_dict = Player() # placing a player_dict data type object into our Player class
    player_dict.player_name =input("What's your favorite patriot player's name? ")
    player_dict.university = input("Where'd they play college ball? ")
    return player_dict

if __name__ == "__main__":
    main()