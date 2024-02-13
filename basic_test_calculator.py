# lets test the square function of calculator.py
from logging import basicConfig, INFO, error, info
# lets import the funciton as a module
from beginner_basic_square_calculator import square
from pytest import raises

# set logging to info
basicConfig(level=INFO, format="%(message)s")

# lets test our square function
def test_positive():
    assert(square(2) == 4)  
    assert(square(3) == 9)
    info("Positive tests passed")  # log that all tests passed

def test_negative():
    # lets test the square function
    assert(square(-2) == 4)
    assert(square(-3) == 9)
    info("Negative tests passed")  # log that all tests passed

def test_zero():
    assert(square(0) == 0)
    info("Zero tests passed")  # log that all tests passed

def test_str():
    with raises(TypeError):
        square("cat")