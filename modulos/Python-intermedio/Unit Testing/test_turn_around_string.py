#test_turn_around_string

from turn_around_string import turn_around_string

def test_turn_around_string():
    #arrange

    original_string = "el mundo de la programacion"
    expected_result = "noicamargorp al ed odnum le"

    #ACT
    
    result = turn_around_string(original_string)

    #assert

    assert result == expected_result

def test_turn_around_string_one_word():
    #arrange

    original = "Python"
    expected = "nohtyP"

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

    
    
