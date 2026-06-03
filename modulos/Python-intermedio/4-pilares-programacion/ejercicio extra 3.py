#Cree una clase base Vehicle con los atributos:
        #_brand
        #_year
        #Agregue un método get_info() que devuelva una descripción del vehículo.
#Luego cree dos clases hijas:
        #Car
        #Motorcycle
    #Cada una debe agregar su propio atributo (por ejemplo, doors o type) y 
    # sobrescribir el método get_info() para incluir esta información adicional.
    
class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
        
    def get_info(self):
        return f"Marca: {self._brand}, Año: {self._year}"
    
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)# Llamamos al constructor de la clase base para inicializar los atributos brand y year
        self._doors = doors
        
    def get_info(self):
        base_info = super().get_info()## Llamamos al método get_info() de la clase base para obtener la información básica del vehículo
        return f"{base_info}, Puertas: {self._doors}"
    
class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year) # Llamamos al constructor de la clase base para inicializar los atributos brand y year
        self._type = type
        
    def get_info(self):
        base_info = super().get_info() # Llamamos al método get_info() de la clase base para obtener la información básica del vehículo
        return f"{base_info}, Tipo: {self._type}"
    

# Ejemplo de uso
car = Car("Toyota", 2020, 4)
motorcycle = Motorcycle("Honda", 2019, "Deportiva")

print(car.get_info()) # Imprime la información del automóvil, incluyendo el número de puertas
print(motorcycle.get_info()) # Imprime la información de la motocicleta, incluyendo el tipo

