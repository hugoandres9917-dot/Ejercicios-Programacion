#ejercicio extra 2

##Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario y
# calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos
# faltarían para llegar a 10 minutos. Si es mayor, muestre “*Mayor*”. Si es exactamente igual,
# muestre “*Igual*”.
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