#ejercicio 6 funciones

def separate_strings(string):
    words = string. split('-')
    organized_word = sorted(words)
    resultado = '-'. join(organized_word)
    return resultado

my_words_are = "Ceniza-Baloo-Boris"
my_new_organized_words = separate_strings(my_words_are)
print(f"mis palabras sin organizar: '{my_words_are }'")
print(f"mis palabras organizadas alfabeticamente y separada por guiones: '{my_new_organized_words}'")