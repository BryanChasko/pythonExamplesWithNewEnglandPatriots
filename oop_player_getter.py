import colorama
from logging import info, INFO, basicConfig, error
from colorama import Fore
basicConfig(level=INFO, format="%(asctime)s - %(message)s")

def main():
    """ (player_name, university) = get_player() """ # use a comma to create a tuple, similar ot a list but immutable. () add clarity this is a touple.
    player_dict = get_player()
    if "tom" in player_dict["player_name"].lower() or "brady" in player_dict["player_name"].lower():
        player_dict["player_name"] = "🐐 The GOAT: Tom Brady"
    info(f'{Fore.BLUE}{player_dict["player_name"]} {Fore.GREEN}went to college at {Fore.RED}{player_dict["university"]}{Fore.RESET}')

def get_player():    
    player_name = input("Enter the player's name: ").strip().lower()
    university = input("Where'd they play college ball? ").strip()
    return {"player_name": player_name, "university": university}

if __name__ == "__main__":
    main()