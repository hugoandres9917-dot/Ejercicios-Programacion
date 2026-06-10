#ejercicio semana 7
##Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
##1. Suma
##2. Resta
##3. Multiplicación
##4. División
##5. Borrar resultado
##Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
##Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b
    

def divide(a, b):
    return a / b
    
        
def calculator():
    current_numb = 0.0

    while True:
        print(f"\nNumero actual: {current_numb}")
        print("Que operacion desea elejir:")
        print("1. Suma","2. Resta," "3. Multiplicacion", "4. Dividision", "5. Ingresar un numero nuevo", "6. Salir de la calculadora") 

        option = input("Ingrese el número de operacion a realizar:")

        if option == '6':
            print("saliendo de la calculadora")
            break
        elif option == '5':
            current_numb = 0.0
            print("Numero actual reiniciado a 0.")  
        
        elif option in ['1', '2', '3', '4']:
            try:
                numb = float(input("Ingrese el numero a operar: "))
            except ValueError:
                print("Entrada invalida. Por favor, ingrese un numero valido.")
                continue

            if option == '1':
                current_numb = add(current_numb, numb)
            elif option == '2':
                current_numb = subtract(current_numb, numb)
            elif option == '3':
                current_numb = multiply(current_numb, numb)
            elif option == '4':
                try:
                    current_numb= divide(current_numb,numb)
                except ZeroDivisionError:
                    print("Error: division por cero no es posible")
                    
        else:
            print("Opcion no valida. Por favor, elija una opción del 1 al 6.")

    print(f"Resultado: {current_numb}")
    print("Gracias por usar la calculadora.")


if __name__ == "__main__":
    print("Bienvenido a la calculadora por linea de comando")
    calculator()


