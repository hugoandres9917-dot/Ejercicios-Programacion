#ejercicio extra 2

#Cree un decorador @requires_login que:
    #Verifique si la variable global user_logged_in es True
    #Si no lo es, debe lanzar una excepción "Usuario no autenticado"
    #Si lo es, la función decorada se ejecuta normalmente
    


user_logged_in = False
    
def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:# verificamos si la variable global user_logged_in es False
            raise Exception("Usuario no ha sido autenticado")
        return func(*args, **kwargs)# si es True, se ejecuta la función decorada normalmente
    return wrapper

#Ejemplo de uso del decorador
@requires_login
def view_profile():
    return "Bienvenido al perfil del usuario"

#caso 1: usuario no autenticado

try:
    print(view_profile())
except Exception as e:
    print(e)

#caso 2: usuario autenticado

user_logged_in = True
try:
    print(view_profile())
except Exception as e:
    print(e)
    
    
