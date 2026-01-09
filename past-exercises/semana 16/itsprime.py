#ejercicio 7 funciones

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






