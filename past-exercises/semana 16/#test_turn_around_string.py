#test_turn_around_string

import pytest   
from turnaroundstring import turn_around_string

def test_turn_around_string():
    #arrange

    original_string = "el mundo de la programacion"
    expected_result = "noicamargorp ed odnum le"

    #ACT
    
    result = turn_around_string(original)

    #assert

    assert result == expected_result

def test_turn_around_string_one_word():
    #arrange

    original = "Python"
    expected = "nohtyp"

    #act
    result =turn_around_string(original)

    #assert

    assert result == expected


def test_turn_around_string_same_letter():
    #arrange

    original = "AAA"
    expected = "AAA"

    #ACT

    result = turn_around_string(original)

    #assert

    assert result == expected

    
    
