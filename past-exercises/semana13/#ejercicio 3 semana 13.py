#ejercicio 3 semana 13

from datetime import date

class User:
    def __init__(self, date_of_birth: date):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        if  ( today.month, today.day)<(self.date_of_birth.month, self.date_of_birth.day):
            years  -= 1
        return years
    

def require_adult(func):
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("El primer argumento debe ser un objeto User.")
        if user.age < 18:
            raise PermissionError("El usuario no es mayor de edad.")
        return func(user, *args, **kwargs)
    return wrapper

@require_adult
def access_restrict(user):
    return f"Acceso concedido a usuario de {user.age} años."

#para probar

if __name__ == "__main__":
    adult = User(date(2000, 5, 10))
    under_age = User (date(2010, 7, 15))
try:
    print(access_restrict(adult))
    print(access_restrict(under_age))
except PermissionError as e:
    print(f"Error: {e}")
    

