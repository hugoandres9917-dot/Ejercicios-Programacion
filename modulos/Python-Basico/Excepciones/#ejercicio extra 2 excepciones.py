#ejercicio extra 2 excepciones

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
