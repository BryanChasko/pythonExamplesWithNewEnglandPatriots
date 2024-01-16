# meower.py
# demonstrating loops by printing "meow" 10 times. we can use while.

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How many times to meow? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow", end=" ")
main()

""" # For Loop Demo with a Range
while True:
    n = int(input("How many times does the cat meow? "))
    if n > 0:
        break

for _ in range(n):
    print("meow", end=" ") """

""" 
# Simplest method
print("meow " * 10)
# For Loop Demo with a Range 
# using _ as we dont care about the name of our variable, just want to use range
for _ in range(10):
    print("meow", end=" ")
 """
""" # For Loop Demo with a List
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("meow", end=" ") """


""" # While Loop Demo
i=1
while i <= 3:
    print("meow", end=" ")
    i += 1 """