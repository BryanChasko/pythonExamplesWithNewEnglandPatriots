"""
Understanding Operational Overloading and Special Method Names in Python  🐍
🏈 Utilizing career passing leaders for the New England Patriots, this script demonstrates the concept of operational
overloading and special method names in Python. It defines a Quarterback class to represent football quarterback
statistics and uses special method names to provide custom behavior for built-in operators such as +, -, *, /, etc.

Concepts Covered:
- Operational overloading: The ability to define custom behavior for built-in operators such as +, -, *, /, etc. for
user-defined classes.
- Special method names: Methods in Python that have double underscores before and after their names, e.g., __init__,
__str__, __add__, etc. These methods are also known as "magic methods" or "dunder methods" and provide functionality
to emulate built-in behavior within user-defined classes.

What to Look for in the File:
1. Class Definition: The definition of the Quarterback class, which represents football quarterback statistics.
2. Initialization Method (__init__): Explanation of how instance variables are initialized using the __init__ method.
3. String Representation Method (__str__): Implementation of the __str__ method to provide a string representation of
Quarterback objects.
4. Addition Method (__add__): Explanation of how the __add__ method overloads the addition operator (+) to combine
statistics of Quarterback objects.
5. Object Creation: Creation of Quarterback objects with relevant statistics for New England Patriots quarterbacks.
6. Total Statistics: Calculation of total statistics by adding the statistics of all quarterbacks using the overloaded
addition operator.
7. Logging and Color Highlighting: Usage of logging module to display quarterback statistics with color highlighting for
better readability.

By studying this file, you will gain a clear understanding of how operational overloading and special method names work
in Python, along with practical examples demonstrating their usage in a real-world scenario.
"""

# Importing necessary modules for logging and color highlighting
from logging import info, INFO, basicConfig
from colorama import Fore

# Setting up logging configuration
basicConfig(level=INFO, format="%(message)s")

# Defining a class for representing quarterback statistics
class Quarterback:
    def __init__(self, name, games, completion_percentage, yards, touchdowns, regular_season_wins, playoff_wins):
        """
        2. Constructor method to initialize a Quarterback object with relevant statistics.
        """
        # Assigning values to instance variables
        self.name = name
        self.games = games
        self.completion_percentage = completion_percentage
        self.yards = yards
        self.touchdowns = touchdowns
        self.regular_season_wins = regular_season_wins
        self.playoff_wins = playoff_wins
    
    def __str__(self):
        """
        3. Special method to represent the Quarterback object as a string.
        """
        # Formatting string representation
        return f"{self.name}: {self.completion_percentage}% complete for {self.yards} yards, " \
               f"with {self.touchdowns} touchdowns in\n{self.games} games, winning {self.regular_season_wins}, " \
               f"including {self.playoff_wins} playoff wins"
    
    def __add__(self, other):
        """
        4. Special method to overload the addition operator (+) for Quarterback objects.
        """
        # Calculating total statistics by adding corresponding attributes
        total_games = self.games + other.games
        total_yards = self.yards + other.yards
        total_touchdowns = self.touchdowns + other.touchdowns
        total_completion_percentage = (self.completion_percentage + other.completion_percentage) / 2
        total_regular_season_wins = self.regular_season_wins + other.regular_season_wins
        total_playoff_wins = self.playoff_wins + other.playoff_wins
        # Creating and returning a new Quarterback object with combined statistics
        return Quarterback("Total", total_games, total_completion_percentage, total_yards, total_touchdowns,
                           total_regular_season_wins, total_playoff_wins)

# Data for New England Patriots quarterbacks
brady = Quarterback("Tom Brady", 285, 63.8, 74571, 541, 219, 30)
bledsoe = Quarterback("Drew Bledsoe", 124, 56.3, 29657, 166, 63, 4)
grogan = Quarterback("Steve Grogan", 149, 52.3, 26886, 182, 75, 5)
parilli = Quarterback("Babe Parilli", 94, 47.2, 16747, 132, 44, 4)
eason = Quarterback("Tony Eason", 72, 58.4, 10732, 60, 28, 3)
plunkett = Quarterback("Jim Plunkett", 61, 48.5, 9932, 62, 23, 2)

# Total statistics
total_stats = brady + bledsoe + grogan + parilli + eason + plunkett # (👈) using the overloaded addition operator

# Logging the quarterback statistics with color highlighting
info(Fore.CYAN + str(plunkett))
info(Fore.RED + str(eason))
info(Fore.YELLOW + str(parilli))
info(Fore.MAGENTA + str(grogan))
info(Fore.BLUE + str(bledsoe))
info(f'{Fore.GREEN}{brady}')
info(Fore.WHITE + str(total_stats))
