#ejercicio extra 1 excepciones

## programa que: Pida al usuario su nombre Si el nombre es numérico (isdigit()),
# haga raise ValueError("El nombre no puede ser un número")

def ask_name():
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un numero") ##raise para lanzar la excepcion
    return name
try:
    user = ask_name()
    print(f"hola {user}")
except ValueError as e: ## captura cualquier error del tipo ValueError y lo asigna a la variable e
    print(e)
    
## pida su edad Si no es un número válido, capture el ValueError y muestre un mensaje   

def ask_age():
    age = input("Ingrese su edad: ")
    if not age.isdigit(): ## isdigit() revisa si el string es un numero, si no lo es, se lanza la excepcion
        raise ValueError("La edad debe ser un numero")
    return int(age)
try:
    user_age = ask_age()
    print(f"Tu edad es {user_age}")
except ValueError as e:
    print(e)
    
##Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"


def ask_name():
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un numero")
    return name

def ask_age():
    age = input("Ingrese su edad: ")
    if not age.isdigit():
        raise ValueError("La edad debe ser un numero")
    return int(age)

try:
    user = ask_name()
    user_age = ask_age()
    print(f"Hola {user}, su edad es {user_age}")
except ValueError as e:
    print(e)