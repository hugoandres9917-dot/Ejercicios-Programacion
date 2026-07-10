#ejercicio 6 funciones

#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def separate_strings(string):
    words = string.split('-')
    organized_word = sorted(words)
    result = '-'.join(organized_word)
    return result

my_words_are = "Ceniza-Baloo-Boris"
my_new_organized_words = separate_strings(my_words_are)
print(f"mis palabras sin organizar: '{my_words_are }'")
print(f"mis palabras organizadas alfabeticamente y separada por guiones: '{my_new_organized_words}'")