#ejercicio 1 semana 15

def bubble_sort(list_to_sort):
    n = len(list_to_sort) # O(n)

    for i in range(n - 1):# O(n)
        swapped = False

        for j in range(n -1- i):# O(n^2)
            current_element = list_to_sort[j] # O(1)
            next_element = list_to_sort[j + 1] # O(1)

            print(f'--iteracion {i}, Elemento actual {current_element}, Segundo elemento{next_element}')# 0(1)

            if current_element > next_element: # O(1)
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j] # O(1)
                swapped = True #O(1)
        if not swapped:#O(n)
            break #o(n)

my_testing_list  = [1,0,2,3,4,5,6,7,8,9 ] #0(n)
bubble_sort(my_testing_list) #0(n)

print(my_testing_list)# 0(n)