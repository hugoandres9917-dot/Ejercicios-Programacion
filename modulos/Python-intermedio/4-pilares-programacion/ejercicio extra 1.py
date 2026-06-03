#Cree una clase Employee con los siguientes requisitos:
    #Atributos privados: _name, _salary
    #Use @property y @<atributo>.setter para:
        #Mostrar el nombre y el salario
        #Validar que el salario nunca sea negativo
#Cree un método promote que aumente el salario un porcentaje definido

class employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salary = value

    def promote(self, percentage):
        increase = self._salary * (percentage / 100)
        self._salary += increase
    
# ejemplo para prueba
try:
    employee1 = employee("Hugo", 50000)
    print(f" Empleado: {employee1.name}, Salario: {employee1.salary}") 
    
    employee1.promote(10) # Aumenta el salario en un 10%
    print(f" Empleado: {employee1.name}, Salario después de promoción: ${employee1.salary:.2f}")
    
    employee1.salary = -1000 # Intento de asignar un salario negativo

except ValueError as e:
    print(e)
    
    