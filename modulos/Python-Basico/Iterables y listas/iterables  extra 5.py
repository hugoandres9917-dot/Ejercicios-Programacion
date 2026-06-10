## Filtrar palabras con mas de 4 letras

words =[]
for i in range(5):
    word = input(f"Ingrese la palabra {i+1}: ")
    words.append(word)

## nueva lita con palabras con mas de 4 letras

new_words = []
for word in words:
    if len(word) > 4:
        new_words.append(word)

print("lista Original: ", words)
print("Palabras con más de 4 letras: ", new_words)

