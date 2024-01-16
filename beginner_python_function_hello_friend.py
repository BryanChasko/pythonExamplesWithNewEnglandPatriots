def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="friend"):
    print("Hello,", to)

main()