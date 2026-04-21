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

            