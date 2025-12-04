#ejercicio 1 semana 13

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con:")
        print(f"args = {args}")
        print(f"kwargs = {kwargs}")

        result = func(*args, **kwargs)

        print(f"Retorno de {func.__name__}: {result}")

        return result
    return wrapper

@debug
def sum(a, b):
    return a + b

@debug
def greet(name, greeting="Hola"):
    return f"{greeting}, {name}!"

sum(4, 9)
greet("Hugo", greeting="Buenas")


