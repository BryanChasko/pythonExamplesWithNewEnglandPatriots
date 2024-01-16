# gronk.py
# Demonstrating loops by printing "GRONK SPIKE 🏈!!!" a specified number of times.

def main():
    number_of_scores = get_number_of_scores()
    gronk_spike(number_of_scores)

def get_number_of_scores():
    """
    This function prompts the user to enter the number of times Rob Gronkowski scores.
    It ensures that the entered number is positive.
    """
    while True:  # An infinite loop that keeps asking until a valid input is given.
        try:
            n = int(input("How many times does Rob Gronkowski score? "))
            if n > 0:
                return n  # If the number is positive, return it and break out of the loop.
        except ValueError:
            print("Please enter a valid integer.")  # Handle non-integer inputs.

def gronk_spike(n):
    """
    Prints "GRONK SPIKE 🏈!!!" n times, where n is the number of times Gronkowski scores.
    """
    for _ in range(n):  # A for loop that iterates n times.
        print("GRONK SPIKE 🏈!!!", end=" ")  # Print the celebration message for each score.

main()

"""  
Simpler examples of while loops
# Simplest method
print("GRONK SPIKE 🏈!!! " * 10)

# While Loop Demo
i = 1
while i <= 3:
    print("GRONK SPIKE 🏈!!!", end=" ")
    i += 1

# For Loop Demo with a List
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("GRONK SPIKE 🏈!!!", end=" ")

# For Loop Demo with a Range
# Using _ as we don't care about the name of our variable, just want to use range
for _ in range(10):
    print("GRONK SPIKE 🏈!!!", end=" ")
 """