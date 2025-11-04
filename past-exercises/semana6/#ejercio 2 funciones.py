#ejercio 2 A funciones

def def_funcion():
    def_variable = 8
    print(def_variable)

def_funcion()

print (def_funcion)






#ejercicio 2 B funciones

global_variable = " hello"

print(f'variable global {global_variable}')

def modified_variable():
    global global_variable
    global_variable = global_variable = " goodbay"
    print(f' nuevo valor {global_variable}')

modified_variable()

print(f'valor final de variable global {global_variable}')
