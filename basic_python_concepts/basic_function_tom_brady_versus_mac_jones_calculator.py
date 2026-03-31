# basic function example -- type hints (PEP 526), f-strings, __name__ guard
def main() -> None:
    x = float(input("to receive its square, enter a number we'll define as x: "))
    print(f"{x} squared is {square(x)}")


def square(n: float) -> float:
    return n ** 2


# football statistics comparison with weighted values
def compare_quarterbacks() -> None:
    # tom brady 2007 mvp season
    brady_td_2007: int = 50
    brady_int_2007: int = 8

    # mac jones 2023 season
    jones_td_2023: int = 10
    jones_int_2023: int = 12

    brady_score = calculate_weighted_score(brady_td_2007, brady_int_2007)
    jones_score = calculate_weighted_score(jones_td_2023, jones_int_2023)

    print(f"tom brady 2007 weighted score: {brady_score}")
    print(f"mac jones 2023 weighted score: {jones_score}")


def calculate_weighted_score(touchdowns: int, interceptions: int) -> int:
    # touchdowns positive, interceptions squared and negative --
    # crude model: emphasizes the cost of turnovers
    # results: tom -14, mac -134. doesn't capture td volume or pick-six impact.
    # see the rust version for a passer rating implementation.
    return touchdowns - (interceptions ** 2)


if __name__ == "__main__":
    main()
    compare_quarterbacks()
