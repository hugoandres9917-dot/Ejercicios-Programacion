#Dada la función:
    
def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2


#Cree un test que:
#Valide que dividir(10, 2) retorna 5.0
#Verifique que dividir por cero lanza un ValueError
#Valide que dividir con un string como parámetro también lanza TypeError