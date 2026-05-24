#Cree una clase de Circle con:
#Un atributo de radius (radio).
#Un método de get_area que retorne su área.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius #Atributo de radio

    def get_area(self): #Método para calcular el área del círculo
        return math.pi * (self.radius **2)

circle1 = Circle(10)
print(F"El area del circulo es: {circle1.get_area():.2f}") 