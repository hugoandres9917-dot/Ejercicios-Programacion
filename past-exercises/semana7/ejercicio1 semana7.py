#ejercicio semana 7 modificado

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b
    

def divide(a, b):
    return a / b
    
        
def calculator():
    current_numb = 0

    while True:
        print(f"\nNúmero actual: {current_numb}")
        print("Que operacion desea elejir:")
        print("1. Suma:")
        print("2. Resta:")
        print("3. Multiplicacion:")
        print("4. Dividision:")
        print("5. Ingresar un numero nuevo:")
        print("6. Salir de la calculadora:")

        option = input("Ingrese el número de operacion a realizar:")

        if option == '1':
            try:
                numb= int(input("Ingrese el número a sumar: "))
                current_numb = add(current_numb, numb)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        elif option == '2':
            try:
                numb= int(input("Ingrese el número a restar: "))
                current_numb = subtract(current_numb, numb)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        elif option == '3':
            try:
                numb= int(input("Ingrese el número a multiplicar: "))
                current_numb = multiply(current_numb, numb)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        elif option == '4':
            try:
                numb = int(input("Ingrese el número a dividir: "))
                current_numb= divide(current_numb,numb)
            except ZeroDivisionError:
                print("Error: division por cero no es posible")
        elif option == '5':
            try:
                current_numb = int(input("Ingrese el nuevo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        elif option == '6':
            print("¡saliendo de la calculadora")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")
        
    print(f"Numero actual {current_numb}")
calculator()

