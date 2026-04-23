#ejercio 2 A funciones

## alcance del scope de las variables, variables locales y globales
## Intente acceder a una variable definida dentro de una función desde afuera.
def def_function():
    def_variable = 8
    print(def_variable)

def_function()

print (def_function)


#ejercicio 2 B funciones
##Intente acceder a una variable global desde una función y cambiar su valor.
global_variable = " hello"

print(f'variable global {global_variable}')

def modified_variable():
    global global_variable
    global_variable = global_variable = " goodbay"
    print(f' nuevo valor {global_variable}')

modified_variable()

print(f'valor final de variable global {global_variable}')
