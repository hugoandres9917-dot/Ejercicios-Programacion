#ejercicio 4 funciones
## Cree una función que le dé la vuelta a un string y lo retorne.
##Esto ya lo hicimos en iterables.
##“Hola mundo” → “odnum aloH”

def turn_around_string (string):

    return string [::-1]

original_string = "el mundo de la programacion"
inverted_string = turn_around_string(original_string)
print(f'el string original es: {original_string}')
print(f'el string invertido es: {inverted_string}')