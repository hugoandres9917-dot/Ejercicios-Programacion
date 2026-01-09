#test_cont_letter

import pytest
from contletter import cont_cappital_lower_letter

def test_cont_cappital_lower_letter():
    #arrange

    text = "Funcione Dentro De La Programacion"
    expected = (3, 26)

    #act

    result = cont_cappital_lower_letter(text)

    #assert

    assert result == expected


def test_cont_cappital_lowwer_letter_2():
    #arrange

    text = "AAAaaa"
    expected = (3, 3)

    #act

    result = cont_cappital_lower_letter(text)

    #assert

    assert result == expected


def test_cont_cappital_lower_letter_3():
    #arrange

    text = "123!@#"
    expected = (0, 0)

    #act

    result = cont_cappital_lower_letter(text)

    #assert

    assert result == expected

    