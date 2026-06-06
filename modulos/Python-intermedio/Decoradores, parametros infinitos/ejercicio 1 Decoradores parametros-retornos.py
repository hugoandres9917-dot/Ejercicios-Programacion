
#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def debug(func):
    def wrapper(*args, **kwargs): 
        print(f"Ejecutando {func.__name__}")
        print(f"args = {args}")
        print(f"kwargs = {kwargs}")

        result = func(*args, **kwargs)# Ejecuta la función original y guarda su resultado

        print(f"Retorno de {func.__name__}: {result}") #mostrar retorno de la función original

        return result
    return wrapper #Devuelve la función decorada

@debug
def sum(a, b):#Función de ejemplo para probar el decorador
    return a + b#Suma dos números y devuelve el resultado

@debug
def greet(name, greeting="Hola, que tal?"):#Función de ejemplo para probar el decorador
    return f"{greeting}, {name}!"#Devuelve un saludo personalizado

#ejemplo de uso de las funciones decoradas

sum(4, 9)
greet("Hugo", greeting="Buenas tardes")

