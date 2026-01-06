#test_ejercicio_2

def sum_total_numbers(num_1, num_2,num_3,num_4):
	print(num_1 + num_2 + num_3 + num_4)

sum_total_numbers(4,6,2,29)

import pytest
from sum_total_numbers import sum_total_numbers


def test_sum_total_numbers():
    #arrange
    num_1, num_2, num_3, num_4 = 4, 6, 2, 29

    #act
    result = sum_total_numbers(num_1, num_2, num_3, num_4)

    #assert

    assert result == 41


def test_sum_total_small_numbers():
    #arrange

    num_1, num_2, num_3, num_4 = 1, 2, 1, 4

    #act

    result = sum_total_numbers(num_1, num_2, num_3, num_4)

    #assert

    assert  result == 8 

def test_sum_total_big_numbers():
    #arrange

    num_1, num_2, num_3, num_4 = 300, 450, 1030, 680

    #act

    result = sum_total_numbers(num_1, num_2, num_3, num_4)

    #assert

    assert result == 2460





    



