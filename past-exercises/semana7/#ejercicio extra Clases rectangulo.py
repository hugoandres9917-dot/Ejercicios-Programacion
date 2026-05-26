#ejercicio extra 1

#Cree una clase Rectangle que:
#Tenga atributos width y height
#Tenga un método get_area() que retorne el área
#Tenga un método get_perimeter() que retorne el perímetro
#Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado.

class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("El ancho y la altura no pueden ser negativos.")
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
try:
    height = float(input("Ingrese la altura del rectangulo: "))
    width = float(input("Ingrese el ancho del rectangulo: "))
    rectangle = Rectangle(width, height)
        
    print("El area del rectangulo es: ", rectangle.get_area())
    print("El perimetro del rectangulo es: ", rectangle.get_perimeter())
except ValueError as e:
    print("Error: ", e)