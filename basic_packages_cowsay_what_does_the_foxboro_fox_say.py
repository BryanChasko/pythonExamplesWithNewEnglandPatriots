
# Packages demonstration, packages are installable into your local environment.
# For example, we're going to use cowsay in this example (pypi.org/project/cowsay/).
# You must run `pip install cowsay` to install cowsay into your local environment.
# We'll import fox which will present an ASCII fox saying whatever you type after the file name.
from cowsay import fox
# sys is a built-in package, no need to install it.
# argv is a list of arguments passed to the script.
# argv[0] is the name of the script librariestemp.py.
# argv[1] is the first argument passed to the script, which you must pass (i.e., your name).
from sys import argv 
from random import choice
from logging import basicConfig, INFO, info

# set contants for when the user inputs more than one word or no words when running the script.
FOXBORO_FOX_SAYING_1 = "Ring-ding-ding-ding-dingeringeding! Gering-ding-ding-ding-dingeringeding! Gering-ding-ding-ding-dingeringeding!"
FOXBORO_FOX_SAYING_2 = "To be honest, I-- I often feel I've got nothing interesting to say"

# configure logging sine we hate print statements
basicConfig(
    level=INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# \n bumps the question onto its own line
info("\n The Foxboro Fox Says")

# len is a built-in function that returns the length of an object, in this case the number of arguments passed to the script.
# i.e., if you run `python librariestemp.py position_one`, len(argv) will be 1, where the filename librariestemp.py is 0.
if len(argv) == 2:
    fox(argv[1])
else:
    fox(choice([FOXBORO_FOX_SAYING_1, FOXBORO_FOX_SAYING_2]))
    