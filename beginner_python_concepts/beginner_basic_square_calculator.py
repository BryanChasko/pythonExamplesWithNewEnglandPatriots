def main():
    x = int(input("Enter a number: "))
    print("Your number squared is", square(x))

def square(n):
    return n * n

#  lets test the square function of calculator.py in test_calculator.py
# we can check our test works by intentionally adding our number to itself rather 
# than squaring it. We can then run our test and see that it fails with pytest
# def test_square():
#         assert(square(2) == 4)
#         assert(square(0) == 0)
#         # below results in +  where -4 = square(-2) error from pytest
#         assert(square(-2) == 4)  

# when I import my function I want to make sure main isn't automatically called itself.
if __name__ == "__main__":
    main()
