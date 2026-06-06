#Cree una clase de User que:
    #Tenga un atributo de date_of_birth.
    #Tenga un property de age.
#Luego cree un decorador para funciones que acepten un User 
#como parámetro que se encargue de revisar si el User es mayor de edad
#y arroje una excepción de no ser así.

from datetime import date #

class User:
    def __init__(self, date_of_birth: date):#
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()# Obtener la fecha actual
        years = today.year - self.date_of_birth.year# Calcular la edad en años
        if  ( today.month, today.day)<(self.date_of_birth.month, self.date_of_birth.day):# Verificar si el cumpleaños aún no ha ocurrido este año
            years  -= 1 # Restar un año si el cumpleaños aún no ha ocurrido este año
        return years
    

def require_adult(func):# Decorador para verificar si el usuario es mayor de edad
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, User):# Verificar si el primer argumento es una instancia de User
            raise TypeError("El primer argumento debe ser un objeto User.")
        if user.age < 18:# Verificar si el usuario es menor de edad
            raise PermissionError("El usuario no es mayor de edad.")
        return func(user, *args, **kwargs)
    return wrapper

@require_adult
def access_restrict(user):# Función de ejemplo que requiere un usuario adulto para acceder
    return f"Acceso concedido a usuario de {user.age} años."

#prueba de la función decorada con usuarios de diferentes edades

if __name__ == "__main__":# Crear usuarios de diferentes edades
    adult = User(date(2000, 5, 10))
    under_age = User (date(2010, 7, 15))
try:
    print(access_restrict(adult))
    print(access_restrict(under_age))
except PermissionError as e:
    print(f"Error: {e}")
    

