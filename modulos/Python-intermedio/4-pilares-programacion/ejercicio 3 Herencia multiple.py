
#Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

#ejercicio de herencia multiple

# en la herencia multiple una clase secundaria
#puede heredar de mas de una clase padre
#esto es util cuando queremos combinar funcionalidades de diferentes clases
#reutilizando codigo y evitando la duplicacion
#relacion entre clases evitando la re escritura de metodos


# creamos clase padre 1
class Student(object):
    def __init__(self, name, age): #definimos el constructor de la clase
        self.name = name #asignamos el nombre al atributo name
        self.age = age #asignamos la edad al atributo age

# creamos clase padre 2
class Institution(object):
    def institutioninfo(self): 
        print("Estudio en Lyfter team, Desarrollo de Software") #definimos un metodo para mostrar la informacion del instituto
        
# creamos clase secundaria que hereda de Student e Institution
class SoftwareEngineer(Student, Institution):
    def Presentationinfo(self):
        print(f"Hola, soy {self.name} y tengo {self.age} años") #sobrescribimos el metodo institution_info para personalizarlo
        
# atributos y metodos de la clase SoftwareEngineer

# creamos una instancia de la clase SoftwareEngineer

Hugo = SoftwareEngineer("Hugo", 38) #indicamos argumentos edad y nombre

#llamamos a los metodos 

Hugo.Presentationinfo() #llamamos al metodo Presentationinfo para mostrar la informacion del estudiante
Hugo.institutioninfo() #llamamos al metodo institutioninfo para mostrar la informacion del instituto