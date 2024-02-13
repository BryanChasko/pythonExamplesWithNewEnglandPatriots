from beginner_main_function_hello_friend import hello

def test_default():
    assert(hello() == "Hello, friend. ")

def test_argument():
    assert(hello("friend") == "Hello, friend. ")
    ,