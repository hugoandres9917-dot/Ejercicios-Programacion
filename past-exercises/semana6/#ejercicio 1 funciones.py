## ejercicio 1 funciones
## funcion imprime dos cosas, la primera y la segunda, pero la segunda funcion se llama dentro de la primera

def print_first_thing():
    print("imprimiendo primero")
    print_second_thing()


def print_second_thing():
    print("imprimiendo segundo ")

print_first_thing()