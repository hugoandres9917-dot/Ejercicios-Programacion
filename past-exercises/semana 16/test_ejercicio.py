
#test_Bubble_sort

import pytest
from bubblesort import bubble_sort

def test_small_list():

    data = [3,1,2] #arrange
    expected = [1,2,3] 

    result = bubble_sort(data)# act

    assert result == expected #assert

def test_Longger_list():

    data = list(range(200, 0, -1)) #arrange
    expected = sorted(data)

    result = bubble_sort(data) # act    

    assert result == expected # assert

def test_empty_list():

    data = [] #arrange
    expected = []

    resurlt = bubble_sort(data) #act

    assert resurlt == expected #assert

def test_invalid_parameter_string():

    data = "Not a list" #arrange

    with pytest.raises(TypeError): #act & assert
        bubble_sort(data)

def test_invalid_parameter_number():

    data = 123 #arrange

    with pytest.raises(TypeError): #act & assert
        bubble_sort(data)

def test_invalid_parameter_none():

    data = None #arrange

    with pytest.raises(TypeError): #act & assert
        bubble_sort(data)


