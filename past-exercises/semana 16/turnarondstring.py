#ejercicio 4 funciones

def turn_around_string (string):

    return string [::-1]

original_string = "el mundo de la programacion"
inverted_string = turn_around_string(original_string)
print(f'el string original es: {original_string}')
print(f'el string invertido es: {inverted_string}')