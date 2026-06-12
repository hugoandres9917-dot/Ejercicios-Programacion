# Ejercicio 1 Bubble_sort

#crea un bubble_sort por tu cuenta

def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    
    for i in range(n -1):
        swapped = False
        
        for j in range(n -1 - i):
            current_element = list_to_sort[j]
            next_element = list_to_sort[j + 1]
            
            print(f"--iteracion numero {i}, elemento actual {current_element}, elemento siguiente{next_element}")
            
            #realizamos el cambio de elemento en caso de el elemento siguiente sea mayor
            
            if current_element > next_element:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j+ 1], list_to_sort[j]
                swapped = True
        if not swapped:
            break
            
#modo de uso

testing_list = [1,0,2,3,4,9,6,7,8,5]
bubble_sort(testing_list)

print(testing_list)


                