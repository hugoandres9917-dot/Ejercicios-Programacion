#ejercicio 7 funciones

#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
#Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

def its_prime(numb):
    if numb < 2:
        return False
    for digit_numb in range(2, int(numb**0.5) + 1):
        if numb % digit_numb == 0:
            return False
    return True

def getting_prime_numb(numb_list):
    prime_list = []
    for numb in numb_list:
        if its_prime(numb):
            prime_list.append(numb)
    return prime_list


numblist = [1, 4, 6, 7, 13, 9, 67]
the_prime_numbs = getting_prime_numb(numblist)
print(f"Lista de numeros {numblist} los numeros primos de la lista son : {the_prime_numbs}")






