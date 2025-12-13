#ejercicio 2 semana 15

def bubble_sort(list_to_sort):
    n = len(list_to_sort)

    for i in range(n - 1):
        for j in range(n -1, i, - 1):
            current_element = list_to_sort[j]
            previous_element = list_to_sort[j -1]

            print(f'--Pasada {i}, comparando {current_element}, con {previous_element}')

            if current_element < previous_element:
                list_to_sort[j], list_to_sort[j - 1] = list_to_sort[j - 1], list_to_sort[j]

my_testing_list = [2, 5, 3, 1, 4, 6, 9, 7, 8]
bubble_sort(my_testing_list)

print(my_testing_list)