# Libraries 101 reference: Python gives us the ability to share code with "modules".
# Modules are files that contain Python code. We can use code from modules by importing them.
# We can import modules in two ways:
from random import choice, shuffle
from logging import log, INFO, ERROR, WARNING, basicConfig
basicConfig(level=INFO, format='REFEREE:Alan Eck:%(message)s')

try:
    # lower converts letters to lowercase, strip removes whitespace
    user_call = ((input('Did Patriots Captain David Andrews call heads or tails?\n')).lower()).strip()
    if user_call not in ['heads', 'tails']:
        raise ValueError( f'The referee did not understand {user_call} as a coin side.')

    coin = choice(['heads', 'tails'])

    if user_call == coin:
        log(WARNING, f'The coin is {coin}, Patriots Ball.')
    else:
        log(INFO, f"It's {coin}, the Jets will take the ball.")
except ValueError as not_a_coin_error:
    log(ERROR,str(not_a_coin_error))


# alternate coin example
# from allows us to use only the choice function from the random module
""" from random import choice

coin = choice(['heads', 'tails'])
print(coin) """

# different random library example with import - shuffle the qb depth chart for the 2023 patriots

print("\nCheck your depth chart for today's starter:")
quarterbacks = ['Bailey Zappe', 'Mac Jones', 'Malik Cunningham', 'Nathan Rourke', 'Will Grier', 'Matt Corrall', 'Trace McSorley']
shuffle(quarterbacks)
for quarterback in quarterbacks:
    print(quarterback)
 

# alternate coin example 2
# import is a keyword that allows us to use code from other modules
# random is a module that contains functions for generating random numbers
""" import random

coin = random.choice(['heads', 'tails'])
print(coin)
 """