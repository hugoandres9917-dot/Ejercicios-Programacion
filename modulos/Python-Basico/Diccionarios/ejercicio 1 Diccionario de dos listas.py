#Cree un programa que cree un diccionario usando dos listas del mismo tamaño,
# usando una para sus keys, y la otra para sus values.

list_a = ["first_name","last_name","role"]
list_b = ["Hugo","Gonzalez","software engineer"]

diccionary = dict(zip(list_a, list_b))
print( diccionary)