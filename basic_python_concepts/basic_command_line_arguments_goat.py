"""
Introducing command-line arguments.
sys.argv is a list of command-line arguments.
 when you execute python3 goat.py "Tom Brady"
 argv[0] is the file name"goat.py", the 2nd argument retrieved is the value you enter after the file name
"""
from sys import argv
from logging import basicConfig, info, error, INFO

# We're too cool for' print statements so we set up logging and set the level to info to display
# info messages and above in the terminal

basicConfig(level=INFO, format='%(asctime)s %(levelname)s:%(message)s')

if len(argv) < 2:
    error("you forgot the name of the GOAT")
elif len(argv) > 3:
    error("First or First and Last Only")
    exit(1)

full_name = ' '.join(argv[1:3])
# slice is a subset of a list, taking a subset from argv as a slice staring at element 1 to 3 to take first and last name
for arg in argv[1:]:
    pass
info(f"the goat is {full_name}")

""" retrieving first name only: info(f"the GOAT is", {argv[1]})   """



""" # alternate command line argument example with exception handling
try:
    info("the GOAT is", argv[1])
except IndexError:
    error("Too few arguments")
 """