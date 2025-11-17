#semana 11 ejercicio 1

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius **2)

circle1 = Circle(10)
print(F"El area del circulo es: {circle1.get_area():.2f}") 