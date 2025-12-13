#ejercicio 1 semana 15

def bubble_sort(list_to_sort):
    n = len(list_to_sort) #0(n)

    for i in range(n - 1):# 0(n)
        for j in range(n -1- i):# 0(n^2)
            current_element = list_to_sort[j] #0(n^2)
            next_element = list_to_sort[j + 1]

            print(f'--iteracion {i}, Elemento actual {current_element}, Segundo elemento{next_element}')# 0(n^2)

            if current_element > next_element: #0(n^2)
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j] #0(n^2)


my_testing_list  = [2, 5, 7, 1, 4, 8, 3, 6, 9 ] #0(n)
bubble_sort(my_testing_list) #0(n)

print(my_testing_list)# 0(n)