
#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.


def only_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(F"Se esperaba un numero< pero se recibio {type(arg).__name__}")
        for arg  in kwargs.values():
            if not isinstance(arg, (int, float)):
                raise TypeError(F"Se esperaba un numero< pero se recibio {type(arg).__name__}")
        return func(*args, **kwargs)
    return wrapper

@only_numbers
def suma(a, b):
    return a + b

print(suma(2, 3))
print(suma(a=2, b=3))  # Esto funciona correctamente
print(suma(2, '3'))  # Esto arroja una excepción type error string no es un numero
