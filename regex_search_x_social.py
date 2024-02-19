import re # regular expression module
import colorama

""" logging is a better way to display messages to the user. It allows us to control the verbosity of
 the messages and the destination of the messages. """
from logging import info, INFO, basicConfig, error
from colorama import Fore
basicConfig(level=INFO, format="%(asctime)s - %(message)s")
info(f"\n{Fore.GREEN}Hello, friend. \nhttps://twitter.com/SweetFeet_White is James White's X Handle.{Fore.RESET}")

url = input("Paste a Patriots player's account X url here: ").strip()
if matches := re.search(r"^https?://(?:www\.)?(?:twitter|x)\.com/(\w+)$", url, re.IGNORECASE):
    info(f"The {Fore.RED}Patriots'{Fore.RESET} handle on X is: {Fore.BLUE}{matches.group(1)}{Fore.RESET}")
else:
    error(f"{url} is not a valid X url.")
