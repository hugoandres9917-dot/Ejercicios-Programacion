#semana 15 ejercicio 2 parte 2
# analizar las funciones usando la BIG O NOTATION


def print_numbers_times_2(numbers_list):
	for number in numbers_list:# 0(n)
		print(number * 2)#0(n)
		

def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:#0(n)
		for element_b in list_b:# 0(n^2)
			if element_a == element_b:#0(n^2)
				return True#0(n^2)
				
	return False#0(n)

def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)#0(1)
	for index in range(min(list_len, 10)):#0(1)
		print(list_to_print[index])#0(1)
		
def generate_list_trios(list_a, list_b, list_c):
	result_list = []#0(1)
	for element_a in list_a:#0(n)
		for element_b in list_b:#0(n^2)
			for element_c in list_c:#0(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}')#0(1)
				
	return result_list #0(1)