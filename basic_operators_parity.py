# parity.py

def main():
    x = int(input("Enter a number to determine if it's even or odd:"))
    if is_even(x):
        print(x, "is even")
    else:
        print(x, "is odd")
    
def is_even(n):
       #if our number is divisible by 2 then it is even 
    return n % 2 == 0

main()
    