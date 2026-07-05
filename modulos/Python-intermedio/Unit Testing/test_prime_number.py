#test_its_prime

import pytest
from prime_number import its_prime, getting_prime_numb

def test_prime_number():

    #arrange

    numb = 7
    expected = True

    #act

    result = its_prime(numb)

    #assert
    assert result == expected

def test_its_prime_2():
    #arrange

    numb = 9
    expected = False

    #act

    result = its_prime(numb)

    #assert

    assert result == expected

def test_getting_prime_numb():
    #arrange

    numblist = [1, 4, 6, 7, 13, 9, 67]
    expected = [7, 13, 67]

    #act

    result = getting_prime_numb(numblist)

    #assert

    assert result == expected
    



