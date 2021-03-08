import pytest
#from domain.models import calculator
from domain.models.calculator import Calculator
from domain.exceptions import ArgumentoInvalidException

def test_calculator_sums_with_2_params():
    #arrange
    a = 10
    b = 20
    expectation = 30

    #act
    result = Calculator.sum(a, b)

    #assert
    assert result == expectation

def test_calculaor_sums_with_notnumber_fail_with_argumentoinvalidexception():
    #arrange
    a = 'notnumber'
    b = 2

    with pytest.raises(ArgumentoInvalidException):
        #act
        result = Calculator(a, b).sum()

