import logging
from termcolor import colored

# Set the logging level to print to console
logging.basicConfig(level=logging.DEBUG, format=colored('%(asctime)s - %(levelname)s - %(message)s', 'green'))

# Get a logger instance for this module defined on the (file) name.
logger = logging.getLogger(__name__)

def greet_visitor():
    """This function greets the user and demonstrats python logging levels."""

logger.info("INFO: begin greeting user \n")

try: 
    # Ask user for their cat's name, format the input to demonstrate pythons built in string functions
    # see https://docs.python.org/3/library/stdtypes.html#string-methods
    # Remove leading and trailing spaces (strip), capitalize first letter of each name (title)

    patriots_player_name = input("What's your receiver's name? \n").strip().title()

    logger.debug(f"DEBUG: input received patriots_player_name = {patriots_player_name} \n")

    print("Throw " + patriots_player_name + " the football. \n")

except Exception as catname_error:
    logger.error(f"ERROR: {catname_error}")
    raise # re-raise the exception for further handling

# Call the greet_user function.
greet_visitor()

# Demonstrate logging messages at each level
logger.debug(colored("DEBUG message", "blue"))
logger.info(colored("INFO message", "green"))
logger.warning(colored("WARNING message", "yellow"))
logger.error(colored("ERROR message", "red"))
logger.critical(colored("CRITICAL message", "magenta", attrs=["bold"]))

