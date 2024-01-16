"""
The script demonstrates the use of Python comparison operators for validating input and controlling program flow.

This Python script is designed for football players (New England Patriots in my imagination :-D) players to report their 
Rate of Perceived Exertion (RPE) as they come off the field. RPE, on a scale of 1-10, is used by training staff to monitor player fatigue levels. 

Comparison operators used in relation to RPE score:
- "==" (Equality): Checks if the number of entries has reached the maximum limit.
- "!=" (Inequality): Could be used for validating non-matching conditions (not directly used here).
- "<=" (Less than or equal to): Validates that the RPE score is not more than the maximum value (10).
- ">=" (Greater than or equal to): Ensures that the RPE score is not less than the minimum value (1).
- "<" (Less than): Controls the while loop to limit the number of entries.

You'll need to install Colorama for aesthetics. if this is confusing, instructions for a basic setup without Colorama (used for aesthetics):
1. Remove 'from colorama import Fore, Style, init, deinit' line.
2. Delete 'init()' and 'deinit()' function calls.
3. Replace or remove 'Fore.*' and 'Style.RESET_ALL' in print statements.
"""

import logging
from colorama import Fore, Style, init, deinit

# Initialize colorama for colored console output
init()

# Configure logging to write to a file with specific format and level
logging.basicConfig(filename='player_rpe.log', level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Create a console handler to output logs to the console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create a formatter for the console handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter)

# Add the console handler to the logger
logger = logging.getLogger(__name__)
logger.addHandler(ch)

# Dictionary to track player RPE entries
player_rpe_counts = {}

# Function to record a player's RPE score
def record_rpe(player_name, rpe):
    # Check if the player is already in the dictionary 'player_rpe_counts'.
    # If not, initialize their entry with an empty list. This uses a dictionary 
    # to map each player's name to their list of RPE scores.
    if player_name not in player_rpe_counts:
        player_rpe_counts[player_name] = []

    # Append the new RPE score to the list associated with the player's name.
    # This allows for storing multiple RPE scores per player.
    player_rpe_counts[player_name].append(rpe)

    # Log the new RPE entry for the player. This uses Python's logging module to 
    # maintain a record of activities, which is helpful for debugging and tracking.
    logger.info("Player: %s, RPE: %s, Entries: %d", player_name, rpe, len(player_rpe_counts[player_name]))

    # Print a confirmation message indicating that the RPE entry has been recorded.
    # The message includes dynamic data (player's name and their total entries).
    # 'Fore.GREEN' and 'Style.RESET_ALL' from Colorama are used for colored output.
    print(f"{Fore.GREEN}Entry recorded for {player_name}. Total entries: {len(player_rpe_counts[player_name])}{Style.RESET_ALL}")

# Function to display RPE results
def display_rpe_results():
    # Print a header message indicating the end of a quarter and beginning of results display.
    print("\nEnd of the first quarter. RPE Results:")

    # Iterate over each player and their scores in the 'player_rpe_counts' dictionary.
    # 'items()' is used to access both the key (player name) and value (scores list).
    for player, scores in player_rpe_counts.items():
        # Calculate the average RPE for each player. 'sum(scores)' adds up all the RPE scores,
        # and 'len(scores)' gives the total count, giving the mean RPE score.
        average_rpe = sum(scores) / len(scores)

        # Print each player's average RPE and total entries.
        # String formatting is used to display the player's name, their average RPE (to 2 decimal places),
        # and the total number of entries. 'Fore.YELLOW' is used for colored output.
        print(f"{Fore.YELLOW}{player}: Average RPE: {average_rpe:.2f}, Total Entries: {len(scores)}{Style.RESET_ALL}")


# Main function where the program starts execution
def main():
    entry_count = 0
    max_entries = 4 # we stop after 4 entries as the "end of the quarter" for the sake of this example
    while entry_count < max_entries:  # Loop continues as long as entry_count is less than max_entries
        try:
            player_name = input("What's your name,?: ").strip()
            if not player_name:  # Checks if player name is not empty
                raise ValueError("Player name cannot be empty.")
            rpe_str = input("On a scale of 1-10, how hard do you feel you worked on the prior drive? ").strip()
            rpe = int(rpe_str)
            if not 1 <= rpe <= 10:  # Validates that rpe is between 1 and 10, inclusive
                raise ValueError("Sorry I only understand numbers 1 thru 10.")

            record_rpe(player_name, rpe)
            entry_count += 1  # Increments the entry count
        except ValueError as e:
            logger.error(e)
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

    display_rpe_results()

if __name__ == "__main__":
    main()

# Deinitialize colorama
deinit()
