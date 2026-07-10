#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
#Pista: investigue de que otras maneras se puede usar el range.

my_string = "Bienvenidos a Costa Rica"

for index in range(len(my_string)-1,-1,-1):
    print(my_string[index])