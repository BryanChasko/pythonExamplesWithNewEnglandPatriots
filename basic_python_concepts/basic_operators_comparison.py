print("This program will compare two numbers.")
x = int(input("What number would you like to store as x? "))
y = int(input("What number would you like to store as y? "))

if x == y:
    print(x, "is equal to", y)
elif x < y or x > y:
    print(x, "is not equal to", y)
else:
    print("Something unexpected happened and we were unable to compare ", x, "to ", y)
