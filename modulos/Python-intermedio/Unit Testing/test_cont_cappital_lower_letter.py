#test_cont_letter
#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    #1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    #2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

import pytest
from cont_cappital_lower_letter import cont_cappital_lower_letter

def test_cont_cappital_lower_letter():
    #arrange

    text = "Funcione Dentro De La Programacion"
    expected = (5, 25)

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

    