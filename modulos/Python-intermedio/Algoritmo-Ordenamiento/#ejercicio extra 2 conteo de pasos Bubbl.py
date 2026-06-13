#ejercicio extra 2 conteo de pasos Bubble_sort_steps
#modifique su implementacion de bubble_sort para que:
    #cuente cuantas iteraciones (pasadas) realiza el algortimo
    #cuente cuantos intercambios se hicieron en total
    
def bubble_sort_with_stats(list_to_sort):
    n = len(list_to_sort)
    total_swaps = 0 #contador 2 de intercambios
    total_passes = 0   # contador de pasadas externas
    
    for i in range(n -1):
        swapped = False
        total_passes += 1    # pasada extrena
        
        for j in range(n -1 - i):
            current_element = list_to_sort[j]
            next_element = list_to_sort[j + 1]
            
            print(f"--iteracion numero {i}, elemento actual {current_element}, elemento siguiente{next_element}")
            
            #realizamos el cambio de elemento en caso de el elemento siguiente sea mayor
            
            if current_element > next_element:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j+ 1], list_to_sort[j]
                swapped = True
                total_swaps += 1 #pasa interna intercambios
        if not swapped:
            break
    print(f"\nTotal de pasadas realizadas: {total_passes}")
    print(f"Total de intercambios realizados: {total_swaps}")
    return list_to_sort

#modo de uso

testing_list = [1,0,2,3,4,9,6,7,8,5]
sorted_list = bubble_sort_with_stats(testing_list)

print("lista ordenada:", sorted_list)


