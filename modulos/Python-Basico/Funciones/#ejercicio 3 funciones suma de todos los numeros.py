#ejercicio 3 funciones
##3. Cree una función que retorne la suma de todos los números de una lista.
##. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
##. [4, 6, 2, 29] → 41

def sum_total_numbers(numbers):
	total = 0
	for num in numbers:
		total += num
	return total

numb_list = [4, 6, 2, 29]

print(f"Lista de números: {numb_list}")

print(f"Suma total: {sum_total_numbers(numb_list)}")



