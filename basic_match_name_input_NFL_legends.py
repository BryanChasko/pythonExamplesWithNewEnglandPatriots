

"""
Usage of Python's match statement. This file showcases the power of pattern matching in Python and how it can be used to simplify
conditional branching.

The user is prompted to enter their name, and based on the input, the program matches the name with predefined cases
using the match statement. If the name matches any of the cases, a corresponding message is printed. If the name does
not match any of the cases, a default message is printed.

 match handles multiple conditions, making the code more expressive and easier to understand.
 note this does not include exception handling and the probability of typos is immense
"""

name = input("What is your name? ")

match name.lower():
    case "barry sanders":
        print("You're a Lion through and through!")
    case "walter payton":
        print("Bear down, Chicago Bears!")
    case "joe montana":
        print("You're a 49er faithful!")
    case "larry fitzgerald":
        print("Rise up, Red Sea!")
    case "ray lewis":
        print("Representing the Ravens, always!")
    case "bruce matthews":
        print("Titan up!")
    case "dan marino":
        print("The Dolphins swim deep in your blood!")
    case "frank gauthier":
        print("Go Pack Go! You bleed green and gold!")
    case _:
        print("You might be a free agent, exploring your options!")