## ejercicio extra 1

## Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
## Ejemplo:
## Entrada: "programacion"
## "Ingrese el carácter que desea buscar:" "o"
## Salida:
## "Se a encontrado 2 veces el carácter"


def cont_character(text, character):
    return text.count(character) ## linea cuenta cuantas veces aparace el caracter en el texto, metodo count que hace mas legible el codigo

text = input("Ingrese un texto: ")
character = input("Ingrese el caracter que desea buscar: ")

cont = cont_character(text, character)

print(f"Se han encontrado {cont} veces el caracter '{character}'")