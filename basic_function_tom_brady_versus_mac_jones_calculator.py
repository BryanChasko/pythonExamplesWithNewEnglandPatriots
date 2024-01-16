# Basic Function Example
def main():
    x = float(input("To receive its square, enter a number we'll define as x: "))
    print(x, "squared is", square(x))

def square(variable_n):
    return variable_n ** 2

main()

# Football Statistics Comparison with Weighted Values
def compare_quarterbacks():
    # Tom Brady's 2007 MVP Season Stats
    brady_td_2007 = 50  # Touchdowns in 2007
    brady_int_2007 = 8   # Interceptions in 2007

    # Mac Jones' 2023 Season Stats
    jones_td_2023 = 10  # Touchdowns in 2023
    jones_int_2023 = 12  # Interceptions in 2023

    # Calculating weighted impact
    brady_score = calculate_weighted_score(brady_td_2007, brady_int_2007)
    jones_score = calculate_weighted_score(jones_td_2023, jones_int_2023)

    # Displaying the results
    print(f"Tom Brady's 2007 weighted score: {brady_score}")
    print(f"Mac Jones' 2023 weighted score: {jones_score}")

def calculate_weighted_score(touchdowns, interceptions):
    # Weighted calculation: touchdowns are positive, interceptions are squared and negative.
    # This emphasizes the negative impact of interceptions on a quarterback's performance.
    return touchdowns - (interceptions ** 2)

# this crude example results in Tom -14 and Mac -134, so obviously this
# isn't a very great comparison as it doesnt properly weight Tom's historic
# touchdowns that season, or the more important metric we're interested in,
# the impact of qb TD/INT ratio on the team's success. 2007 tom should receive
# extra weighting for his long touchdowns as Mac should receive extra weighting
# for his pick sixes thrown.

compare_quarterbacks()
