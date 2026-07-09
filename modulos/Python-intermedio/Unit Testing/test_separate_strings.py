#test_separatestrings

import pytest
from separate_strings import separate_strings

def test_separate_strings():
    #arrange

    text = "Ceniza-Baloo-Boris"
    expected = "Baloo-Boris-Ceniza"

    #act

    result = separate_strings(text)

    #assert 

    assert result == expected

def test_separate_strings_2():
    #arrange

    text = "zebra-manzana-mango"
    expected = "mango-manzana-zebra"

    #act

    result = separate_strings(text)

    #assert

    assert result == expected

def test_separate_string_3():
    #arrange

    text = "uno-dos-tres-cuatro"
    expected = "cuatro-dos-tres-uno"

    #act

    result = separate_strings(text)

    #assert

    assert result == expected