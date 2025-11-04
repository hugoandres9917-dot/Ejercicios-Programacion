secret_number = 9
counter = 0

while (counter != secret_number): 
        new_try = int(input("adivine un numero del 1 al 10"))
        counter += 1
        if new_try!= secret_number:
            print("incorrecto, vamos de nuevo")
        else:
            print (f'9 nuestro numero secreto lo adivinaste en {counter}intentos')