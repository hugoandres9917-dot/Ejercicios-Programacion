#ejercicio 1 Big O Notatio
#bubble sort

def bubble_sort(list_to_sort):
    n = len(list_to_sort)#o(1)
    
    for i in range(n -1):#o(n)
        swapped = False
        
        for j in range(n -1 - i):#o(n)
            current_element = list_to_sort[j]#o(1)
            next_element = list_to_sort[j + 1]# o(1)
            
            print(f"--iteracion numero {i}, elemento actual {current_element}, elemento siguiente{next_element}")# o(1)
                        
            if current_element > next_element: #o(1)
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j+ 1], list_to_sort[j]# o(1)
                swapped = True #o(1)
        if not swapped:#o(1)
            break#o(1)

testing_list = [1,0,2,3,4,9,6,7,8,5] #o(1)
bubble_sort(testing_list)#o(1)

print(testing_list)# o(1)
#cada bucle individual es O(n)
# complejidad acumuladad O(n^2)