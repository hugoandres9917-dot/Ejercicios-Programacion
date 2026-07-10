#ejercicio 3 Validación de entrada antes de ordenar
#Cree una función que reciba una lista y valide:
    #Que todos los elementos sean números
    #Que no esté vacía
    #Luego aplique bubble_sort si pasa las validaciones
    #Si hay error, debe lanzar un mensaje apropiado

def validate_list(input_list):
    if not input_list:#valida que la lista no este vasia
        raise ValueError("Error: la lista esta vacia.")

    for element in input_list:# validar que todos los elementos sean numeros
        if not isinstance(element,( int, float)):
            raise TypeError(f"Error: Elemento invalido '{element}'. todos deben ser numeros.")
        return True # si pasa las validaciones
    
    
def bubble_sort_with_stats(list_to_sort):
    validate_list(list_to_sort)
    n = len(list_to_sort)
    
    for i in range(n -1):
        swapped = False
        
        for j in range(n -1 - i):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j+ 1], list_to_sort[j]
                swapped = True
        if not swapped:
            break
    return list_to_sort
#modo de uso
try:#lista normal
    testing_list = [1,0,2,3,4,9,6,7,8,5]
    sorted_list = bubble_sort_with_stats(testing_list)
    print("lista ordenada:", sorted_list)
except(ValueError, TypeError) as e:
    print(e)
    
try:# eror: lista vasia
    testing_list = []
    sorted_list = bubble_sort_with_stats(testing_list)
    print("lista ordenada:", sorted_list)
except(ValueError, TypeError) as e:
    print(e)
    
try:# elementos en lista no son todos numeros 
    testing_list = ["hello", 1, 3, "que tal"]
    sorted_list = bubble_sort_with_stats(testing_list)
    print("lista ordenada:", sorted_list)
except(ValueError, TypeError) as e:
    print(e)
    
    
    

