## ejercicio sintaxis extra

##Pasa los Ejercicios de Pseudocodigo previamente creados a código:
##Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
##Si el precio es menor a 100, el descuento es del 2%.
##Si el precio es mayor o igual a 100, el descuento es del 10%.
##Ejemplos:
##120 → 108
##40 → 39.2



print("-----jercicio Calculo de descuento del producto-----")

product_price = float(input("Ingrese precio del producto: "))

if product_price < 100:
    discount = product_price * 0.02
else:
    discount = product_price * 0.10

total_price = product_price - discount

print(f"El precio del producto con descuento es de {total_price}")

##ejercicio extra 2
##Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “*Mayor*”. Si es exactamente igual, muestre “*Igual*”.
##1. *Ejemplos*:
##1. 1040 → Mayor
##2. 140 → 460
##3. 600 → Igual
##4. 599 → 1

print("-- Comprar segundos con minutos--")

seconds =  int(input("Indique los segundos de la hora en este momento: "))

ten_minutes = 10 * 60

if seconds < ten_minutes:
    result = ten_minutes - seconds
    print("Segundos faltanntes para 10 minutos:")
    print(result)
elif seconds > ten_minutes:
    print("Es mayor a 10 minutos")
else:
    print("Es igual a 10 minutos")


##Ejerecicio 3 
##  1. Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.
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



##Cree un diagrama de flujo que tenga un numero secreto del 1 al 10,
##y le pida al usuario adivinar ese número. El algoritmo no debe 
##terminar hasta que el usuario adivine el numero

import random

secret_number = random.randint(1, 10)
counter = 0
new_try = None

while (new_try != secret_number): 
        new_try = int(input("adivine un numero del 1 al 10: "))
        counter += 1
        if new_try != secret_number:
            print("incorrecto, vamos de nuevo")
        else:
            print (f'{secret_number}  es nuestro numero secreto lo adivinaste en {counter}intentos')

##Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.
##Ejemplos:
##23, 30, 768 → Correcto (hay un 30)
##10, 15, 5 → Correcto (10 + 15 + 5 = 30)
##35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)

print('--Verificar si algun numero es 30 o si la suma de los numeros da 30--')

number1 = int(input("Digite el primer numero: "))
number2 = int(input("Digite el segundo numero: "))
number3 = int(input("Digite el tercer numero: "))

if number1 == 30 or number2 == 30 or number3 == 30 or (number1 + number2 + number3) == 30:
     print("Correcto")
else:
    print("Incorrecto")

##Convertidor de unidades de temperatura
##Pida al usuario ingresar una temperatura en Celsius
##Conviértala a Fahrenheit y Kelvin
##Muestre los tres valores

print("--convertidor de unidades de temperatura--")

celsius = float(input("Ingrese la temperatura en celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")


##Tabla de multiplicar personalizada
##Pida al usuario un número del 1 al 10
##Muestre su tabla de multiplicar del 1 al 12

print("--Tabla de multiplicar personalizada--")

number = int(input("Digite un numero del 1 al 10 para mostrar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {number}:")
for i in range(1, 13):
     result = number * i
     print(f"{number} x {i} = {result}")


