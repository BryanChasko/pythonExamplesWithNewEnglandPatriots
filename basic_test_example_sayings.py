from logging import INFO, info, basicConfig
basicConfig(level=INFO, format='%(asctime)-15s %(message)s')

def main():
    hello("friend")
    goodbye("friend")

def hello(name):
    info(f'Hello {name}!')

def goodbye(name):
    info(f'Goodbye {name}!')

# This line checks if this file is the entry point of the program. 
# If it is, it calls the main function. This allows the code in the main function 
# to be used as a module in other scripts without being executed when the module is imported.

if __name__ =='__main__':
    main()