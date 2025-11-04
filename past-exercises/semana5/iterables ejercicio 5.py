numbers_list =[]

for num in range (10):
    new_number = int(input(f'ingrese una lista de 10 numeros{num+1}:'))
    numbers_list.append(new_number)
if numbers_list:
    bigger_number = max(numbers_list)
    print("lista de numeros ingresada",numbers_list)
    print("el numero mas alto es:", bigger_number)
    
    