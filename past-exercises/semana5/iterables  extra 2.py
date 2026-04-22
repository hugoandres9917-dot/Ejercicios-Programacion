## verificar si todos los elementos de una lista son positivos

numbers_list = input("Ingrese una lista de numeros separados por comas: ")

my_list = [int(number.strip()) for number in numbers_list.split(",")]

all_positive = True
for number in my_list:
    if number <= 0:
        all_positive = False
        break

if all_positive:
    print("Todos los numeros son positivos.")
else:
    print("Hay al menos un numero negativo o cero en la lista.")

    