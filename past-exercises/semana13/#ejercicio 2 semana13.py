#ejercicio 2 semana13

def secure_numbers(func):
    def wrapper (*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(F"Se esperaba un numero< pero se recibio {type(arg).__name__}")
        for arg  in kwargs.values():
            if not isinstance(arg, (int, float)):
                raise TypeError(F"Se esperaba un numero< pero se recibio {type(arg).__name__}")
        return func(*args, **kwargs)
    return wrapper

@secure_numbers
def Sum(a, b):
    return a + b

print(Sum(30, 20))