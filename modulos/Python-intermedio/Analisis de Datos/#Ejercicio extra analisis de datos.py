#Ejercicio extra analisis de datos 

#1. Los siguientes dos algoritmos hacen lo mismo: calcular la suma de los primeros n números naturales
#Versión 1:

def manual_add(n):
    result = 0
    for i in range(1, number + 1): #O(n) complejidad temporal el bucle recorre todos los numeros hasta n
        result += i #O(1) complejidad espacial solo usa una variable acumuladora
    return result
#Version 2
def add_formula(n):
    return number * (number + 1) // 2 #O(1) complejidad temporal hace las mismas operaciones sin importar el tamaño de n

#Preguntas:
#¿Cuál es la complejidad de cada versión?
#¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
#version 1 O(n) adecuada para valores pequeños de n pero es muy lenta si n es enorme
#version 2  O(1) siempre rapida incluso si n = 1000, 000, 000.

#2.Considere los siguientes dos algoritmos:
def linear_search(my_list, target):
    for item in my_list:# O(n) complejidad temporal peor caso O(n) mejor caso O(1)
        if item == target:#O(1) complejidad espacial: O(1)
            return True # funciona con cualquierlista no necesita estar ordenada
    return False #O(1)

def binary_search(my_list, target):
    low = 0
    high = len(lst) - 1
    while low <= high: #O(log n) complejidad temporal peor caso O(log n) mejor caso O(1) si elemento esta en el medio
        mid = (low + high) // 2 #O(1) complejidad espacial O(1)
        if my_list[mid] == target:# requiere que la lista este ordenanda previamente
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False  #O(1)

#Preguntas:
#¿Cuál es la complejidad de cada algoritmo?
#¿En qué condiciones conviene usar cada uno?
#¿Qué pasa si la lista no está ordenada?

#linear search sigue funcionando sin problema
#Binary search deja de ser valido puede devolver resultados incorrectos porque su logica depende de los elementos esten en orden
#lista desordenada - linaer search
#lista ordenada y grande Binary search


#3. Analice la siguiente función:

def print_all_pairs(my_dict):
    for key1 in my_dict: #O(n) bucle externo recorre todas las claves O(n)
        for key2 in my_dict:#O(n) bucle interno tambien y combinados O(n^2)
            print(f"{key1}-{key2}") #O(1) operacion constante

#Preguntas:
#¿Cuál es la complejidad temporal?
#¿Cuanto dura si hay 1 millón de claves?
# si n = 1,000,000 el algortimo imprime N^2 pares
#significa un trillon de impresiones no es viable
#complejidad temporal O(N^2)
#con un millon de claves el algoritmo es impractico porque genera un volumen de salida gigantesto

