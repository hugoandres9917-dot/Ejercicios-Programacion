#ejercicio 5 funciones
#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
##“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def cont_cappital_lower_letter(text):
    cappital = 0
    lower_case = 0

    for caracter in text:
        if caracter.isupper():
            cappital += 1
        elif caracter.islower():
            lower_case += 1

    print(f"Número de mayúsculas: {cappital}")
    print(f"Número de minúsculas: {lower_case}")


my_string = "Funciones Dentro De La Programacion"
cont_cappital_lower_letter(my_string)
