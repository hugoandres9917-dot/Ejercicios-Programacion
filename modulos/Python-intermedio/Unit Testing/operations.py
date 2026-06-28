#Ejercicio extra pytest

   #Cree una clase de pruebas que contenga al menos 3 funciones que operen con números (como suma, promedio, conversión, etc.) y escriba:
   #Un caso con números positivos
  # Un caso con números negativos
   #Un caso con ceros


#operations

class Operations:
    def sum(self,  a, b):
        return a + b
    
    def average(self, list):
        if not list:
            return 0
        return sum(list) / len(list)
    
    def convert_integer(self, value):
        return int(value)
    
    