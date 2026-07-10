#ejercio 2 A funciones

## alcance del scope de las variables, variables locales y globales
## Intente acceder a una variable definida dentro de una función desde afuera.
from inspect import Traceback


def def_function():
    def_variable = 8
    print(def_variable)

def_function()

print (def_variable)

-- este será el error que se muestra al intentar acceder a una variable local desde fuera de la función, ya que no es posible acceder a ella.

--PS C:\Users\hugoa\OneDrive\Documentos\Academia Lyfter> & C:\Users\hugoa\AppData\Local\Microsoft\WindowsApps\python3.13.exe "c:/Users/hugoa/OneDrive/Documentos/Academia Lyfter/past-exercises/semana6/Untitled-2.py"

--Traceback (most recent call last):
File "c:\Users\hugoa\OneDrive\Documentos\Academia Lyfter\past-exercises\semana6\Untitled-2.py", line 7, in <module>
print (def_variable)
^^^^^^^^^^^^
NameError: name 'def_variable' is not defined
PS C:\Users\hugoa\OneDrive\Documentos\Academia Lyfter> 


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
