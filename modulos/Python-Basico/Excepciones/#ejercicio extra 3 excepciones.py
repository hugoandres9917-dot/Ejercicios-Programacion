#ejercicio extra 3

##Cree una función sumar_valores(lista) que:
##Reciba una lista de elementos (strings, enteros, flotantes mezclados)
##Intente convertir cada elemento a tipo float
##Si puede, sume el valor y muestre: "<valor> sumado correctamente"
##Si no puede, muestre: "Elemento inválido: <valor>"
##Al final, imprima la suma total

def sum_values(mixed_list):
    sum_total = 0.0
    for element in mixed_list:
        try:
            value = float(element)
            sum_total += value
            print(f"{element} sumado correctamente")
        except ValueError:
            print(f"Elemento invalido: {element}")
    print(f"Suma total: {sum_total}")
    
my_list = ["4", 'hola', 10, 5.2, "3.5", "mundo"]
sum_values(my_list)

