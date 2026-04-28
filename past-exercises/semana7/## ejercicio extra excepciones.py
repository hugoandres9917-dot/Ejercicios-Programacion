## ejercicio extra excepciones

## programa que: Pida al usuario su nombre Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")

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
    
##Cree una función convertir_a_entero(lista) que: Reciba una lista de strings 
##Intente convertir cada elemento a entero usando int() Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás

def convert_to_int(numb_list):
    print("Resultado:")
    for element in numb_list:
        try:
            numb = int(element)
            print(f'"{element}" se convirtio a {numb}')
        except ValueError:
            print(f"No se pudo convertir el elemento: {element}")

my_list = ["10", "abc", "30", "5.2"]
convert_to_int(my_list)

##Cree una función sumar_valores(lista) que:
##Reciba una lista de elementos (strings, enteros, flotantes mezclados)
##Intente convertir cada elemento a tipo float
##Si puede, sume el valor y muestre: "<valor> sumado correctamente"
##Si no puede, muestre: "Elemento inválido: <valor>"
##Al final, imprima la suma total

def sum_values(mixed_list):
    sum_total = 0.0
    for element in mixed_list:
        try:
            value = float(element)
            sum_total += value
            print(f"{element} sumado correctamente")
        except ValueError:
            print(f"Elemento invalido: {element}")
    print(f"Suma total: {sum_total}")
    
my_list = ["4", 'hola', 10, 5.2, "3.5", "mundo"]
sum_values(my_list)

