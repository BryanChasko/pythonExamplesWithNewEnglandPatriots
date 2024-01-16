# using loops to make a football field representation

def main():
    # Call the function to print a football field with specified length and width.
    # Length: Number of rows, Width: Number of characters in each row.
    print_football_field(10, 20)

def print_football_field(length, width):
    """
    Prints a simple representation of a football field using loops.
    The field consists of end zones at both ends and yard lines in between.
    
    Parameters:
    length (int): The number of rows to represent the length of the field.
    width (int): The number of characters in each row to represent the width.
    """
    print_end_zone(width)  # Print the top end zone
    # Loop to print the yard lines. Subtract 2 from length for the top and bottom end zones.
    for _ in range(length - 2):
        print_yard_line(width)
    print_end_zone(width)  # Print the bottom end zone

def print_end_zone(width):
    """
    Prints an end zone line, which is a row in the football field.
    End zones are represented by a line of equal signs.
    
    Parameter:
    width (int): The width of the field/end zone.
    """
    print("=" * width)  # Use string multiplication to print equal signs across the width

def print_yard_line(width):
    """
    Prints a yard line, which is a row in the football field.
    Yard lines are represented by hashes with a central pipe symbol.
    
    Parameter:
    width (int): The width of the field/yard line.
    """
    # Create a yard line with hashes and a central pipe. 
    # The pipe symbol is positioned in the middle of the line.
    yard_line = "#" * (width // 2 - 1) + "|" + "#" * (width // 2 - 1)
    print(yard_line)

main()
