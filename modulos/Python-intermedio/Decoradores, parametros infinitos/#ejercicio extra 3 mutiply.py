#ejercicio extra 3 

#Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
#A esta función se le debe combinar dos decoradores:
    #@log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
    #@validate_numbers: revisa que todos los argumentos sean numéricos
    
    
from datetime import datetime# con esta librería se obtiene la fecha actual

def log_call(fun):#
    def wrapper(*args, **kwargs):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Llamando a la función: {fun.__name__} en fecha {date}")
        print(f"args: {args}, kwargs: {kwargs}")
        
        result = fun(*args, **kwargs)   
        
        print(f"El resultado de la función {fun.__name__} es: {result}")
        return result
    return wrapper

def validate_numbers(fun):# decorador para validar que los argumentos sean numéricos
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"El argumento {arg} no es un número válido.")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"El argumento {key} con valor {value} no es un número válido.")
        return fun(*args, **kwargs)
    return wrapper        
        

@log_call
@validate_numbers
#decoradores para la función multiply
def multiply(a, b):
    return a * b


#Ejemplo de uso
if __name__ == "__main__":
    try:
        result = multiply(5, 3)
        print(f"Resultado: {result}")
        
        # Esto lanzará un error porque "abc" no es un número
        result = multiply(5, "abc")
    except ValueError as e:
        print(e)
