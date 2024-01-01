import pytest
from calculator import Calculator

@pytest.mark.basic
def test_addition():
    assert Calculator.add(2, 3) == 5

@pytest.mark.basic
def test_subtraction():
    assert Calculator.subtract(5, 3) == 2

def test_multiply():
    assert Calculator.multiply(10, 4) == 40