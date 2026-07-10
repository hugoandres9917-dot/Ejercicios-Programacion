#Modifica el bubble_sort para que funcione de derecha a izquierda,
# ordenando los números menores primero (como en la imagen de abajo).

def bubble_sort_right_to_left(list_to_sort):
    n = len(list_to_sort)

    for i in range(n - 1):
        swapped = False
        
        for j in range(n -1, i, - 1):
            current_element = list_to_sort[j]
            previous_element = list_to_sort[j -1]
            
            print(f" --itercacion numero{i}, comparando{current_element}, con{previous_element}")
            
            if current_element < previous_element:
                list_to_sort[j], list_to_sort[j - 1] = list_to_sort[j - 1], list_to_sort[j]
                swapped = True
        if not swapped:
            break
#modo de uso
testing_list = [1, 0, 2, 3, 4, 9, 6, 7, 8, 5]
bubble_sort_right_to_left(testing_list)
print("Ya la lista esta ordenada:", testing_list)
