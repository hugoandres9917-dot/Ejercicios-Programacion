#test_funciones

# test_divide.py
import pytest
from funciones import divide

def test_divide_correct_value():
    assert divide(10, 2) == 5.0

def test_divide_to_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_with_string():
    with pytest.raises(TypeError):
        divide("10", 2)
