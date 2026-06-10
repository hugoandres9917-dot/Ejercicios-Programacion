## ejercicio extra 3 funciones

##Cree una función que reciba un string y retorne cuántas vocales contiene

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1
    return count

text = input("Ingrese un texto: ")
vowel_count = count_vowels(text)

print(f"El numero de vocales en el texto es: {vowel_count}")
