#Cree una clase abstracta de Shape que:
    #Tenga los métodos abstractos de calculate_perimeter y calculate_area.
    #Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
    #Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.
    
from abc import ABC, abstractmethod
import math

class Shape(ABC):  #Clase abstracta de Shape
    @abstractmethod
    def calculate_perimeter(self): #Método abstracto para calcular el perímetro
        pass
    
    @abstractmethod # Método abstracto para calcular el área
    def calculate_area(self): 
        pass
    
class Circle(Shape): #Clase Circle que hereda de Shape
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_perimeter(self):# El perímetro de un círculo se calcula como 2 * pi * radio
        return 2 * math.pi * self.radius
    
    def calculate_area(self): # El área de un círculo se calcula como pi * radio^2
        return math.pi * (self.radius ** 2)
    
class Square(Shape): #Clase Square que hereda de Shape
    def __init__(self, side):
        self.side = side
        
    def calculate_perimeter(self):
        return 4 * self.side # El perímetro de un cuadrado se calcula como 4 * lado
    
    def calculate_area(self): # El área de un cuadrado se calcula como lado^2
        return self.side ** 2
    
class Rectangle(Shape): #Clase Rectangle que hereda de Shape
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_perimeter(self): # El perímetro de un rectángulo se calcula como 2 * (ancho + alto)
        return 2 * (self.width + self.height)
    
    def calculate_area(self): # El área de un rectángulo se calcula como ancho * alto
        return self.width * self.height
    
shapes = [Circle(5), Square(4), Rectangle(6, 3)] #Lista de objetos de tipo Shape (Circle, Square y Rectangle)

for shape in shapes: #
    print("Perimetro:", shape.calculate_perimeter())
    print("Area", shape.calculate_area())
    

