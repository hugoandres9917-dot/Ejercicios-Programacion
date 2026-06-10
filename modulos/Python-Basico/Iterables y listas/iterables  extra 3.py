## Encontrar el menor valor en una lista sin usar la función min()

numbers_list = input("Ingrese una lista de numeros separados por comas: ")

# convertir la entrada en lista de enteros

my_list = [int(numb.strip()) for numb in numbers_list.split(",")]

min_value = my_list[0]
for numb in my_list:
    if numb < min_value:
        min_value = numb

print(f"El menor valor en la lista es: {min_value}")

