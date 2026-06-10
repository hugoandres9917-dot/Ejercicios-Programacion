#ejercicio extra 3

1. Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.
##  1. 5 → 15 (1 + 2 + 3 + 4 + 5)
##  2. 3 → 6 (1 + 2 + 3)
##  3. 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)


print("--Suma acumulativa desde 1 hasta numero ingresado--")

number = int(input("Digite el numero hasta el cual quiere sumar: "))
counter = 1
result = 0

while counter <= number:
    result  += counter
    counter += 1
print(f"El resultado de la suma de cada numero del 1 hasta {number} es: {result}")

