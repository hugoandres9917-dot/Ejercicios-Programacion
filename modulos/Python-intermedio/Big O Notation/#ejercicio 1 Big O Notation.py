#ejercicio 1 Big O Notatio
#bubble sort

def bubble_sort(list_to_sort):
    n = len(list_to_sort)#o(n)
    
    for i in range(n -1):#o(n)
        swapped = False
        
        for j in range(n -1 - i):#o(n^2)
            current_element = list_to_sort[j]#o(1)
            next_element = list_to_sort[j + 1]# o(1)
            
            print(f"--iteracion numero {i}, elemento actual {current_element}, elemento siguiente{next_element}")# o(1)
                        
            if current_element > next_element: #o(1)
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j+ 1], list_to_sort[j]# o(1)
                swapped = True #o(1)
        if not swapped:#o(n)
            break#o(n)

testing_list = [1,0,2,3,4,9,6,7,8,5] #o(n)
bubble_sort(testing_list)#o(n)

print(testing_list)# o(n)