## Calcular el promedio y filtrar valores mayores al promedio

numbers_list = input("Ingrese una lista de numeros separados por comas: ")

my_list = [int(numb.strip()) for numb in numbers_list.split(",")]

## calcular el promedio

average = sum(my_list) / len(my_list)

## filtrar valores mayores al promedio

filtered_values = [numb for numb in my_list if numb > average]

print(f"El promedio es: {average}")
print(f"Los valores mayores al promedio son: {filtered_values}")