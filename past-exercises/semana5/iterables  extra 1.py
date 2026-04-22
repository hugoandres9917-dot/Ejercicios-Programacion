## ejercicios extra iterables

## programa Conter cuantas veces aparece un numero en una lista

numbers_list = input("Ingrese una lista de numeros separados por comas: ")

my_list = [int(number.strip()) for number in numbers_list.split(",")]

number_to_find = int(input("Ingrese el numero a buscar: "))

count = my_list.count(number_to_find)

print(f"El numero {number_to_find} aparece {count} veces en la lista.")