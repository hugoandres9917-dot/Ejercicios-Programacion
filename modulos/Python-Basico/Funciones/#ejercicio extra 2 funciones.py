## ejercicio extra 2 funciones

##Cree una función que reciba una lista de palabras y un número n,
## y retorne una nueva lista con solo las palabras que tengan más de n letras

def filter_words_by_length(words, n):
    new_list = []
    for word in words:
        if len(word) > n:
            new_list.append(word)
    return new_list

words = input("Ingrese una lista de palabras separadas por comas: ").split(",") ## metodo split para convertir el string en una lista de palabras, separadas por comas
n = int(input("Ingrese el numero n de letras: "))

filtered = filter_words_by_length(words, n)

print(f"Lista Original: {words}")

print(f"Lista Filtrada: {filtered}")

