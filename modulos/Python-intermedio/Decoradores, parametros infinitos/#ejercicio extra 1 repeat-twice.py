#ejercicio extra 1

#Cree una función que imprima “Hola, [nombre]” dos veces:
#Cree un decorador @repeat_twice que haga que la función 
# decorada se ejecute dos veces seguidas, con los mismos argumentos

def repeat_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper  

@repeat_twice #decorador que hace que la función se ejecute dos veces
def greet(name):
    print(f"Hola yo soy, {name}")
    
# Ejemplo de uso

greet("Hugo")