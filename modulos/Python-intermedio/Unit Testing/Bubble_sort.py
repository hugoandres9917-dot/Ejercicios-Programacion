#ejercicio 1 semana 15

def bubble_sort(list_to_sort):
    n = len(list_to_sort) 

    for i in range(n - 1):
        swapped = False

        for j in range(n -1- i):
            current_element = list_to_sort[j] 
            next_element = list_to_sort[j + 1] 

            print(f'--iteracion {i}, Elemento actual {current_element}, Segundo elemento{next_element}')

            if current_element > next_element: 
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j] 
                swapped = True 
        if not swapped:
            break 
    return list_to_sort


if __name__ == "__main__":
    my_testing_list  = [1,0,2,3,4,5,6,7,8,9 ] 
    bubble_sort(my_testing_list) 

    print(my_testing_list)