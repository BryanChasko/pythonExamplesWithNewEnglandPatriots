def main():
    """
    Main function to start the program.
    It prompts the user for the number of points the Patriots scored and prints it.
    Includes explanations for beginners about the control structures used.
    """
    patriots_score = get_patriots_score()
    if patriots_score is not None:
        print(f"The Patriots scored {patriots_score} points.")
    else:
        print("Roger Goodell seems to be interfering.")

def get_patriots_score():
    """
    This function prompts the user for the number of points scored by the Patriots.
    It only accepts the valid NFL values for scoring: 1 (extra point kick), 2 (xp conversion), 3 (field goal), 6 (touchdown).
    
    - A while loop is used to allow multiple attempts for the user to input a valid score.
    - A try-except block is used to handle cases where the input is not an integer.
    - If-else statements are used to check if the entered score is valid and to manage the flow of the program.
    """
    valid_scores = [1, 2, 3, 6]  # List of valid scores
    max_attempts = 3  # Maximum number of input attempts
    attempts = 0  # Counter for the number of attempts made

    while attempts < max_attempts:  # Loop until the number of attempts reaches max_attempts
        try:
            score = int(input("Enter the number of points the Patriots scored: "))  # Try to convert input to an integer
            if score in valid_scores:  # Check if the entered score is in the list of valid scores
                return score  # If valid, return the score
            else:
                print("Invalid score. Please enter 1, 2, 3, or 6.")  # Inform user of invalid input
        except ValueError:  # Handle the case where input is not an integer
            print("Invalid input. Please enter an integer.")
        
        attempts += 1  # Increment the attempt counter
        if attempts == max_attempts:  # Check if maximum attempts have been reached
            print("Maximum attempts reached.")  # Inform user that maximum attempts have been reached
            return None  # Return None to indicate failure to get a valid input

main()

