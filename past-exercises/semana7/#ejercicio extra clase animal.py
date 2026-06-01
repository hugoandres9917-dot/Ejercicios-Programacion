#ejercicio extra clase animal
#Cree una clase base Animal y dos clases hijas Dog y Cat:
#Animal debe tener nombre y método speak() que retorne "Hace un sonido"
#Dog debe sobrescribir speak() para decir "Guau"
#Cat debe sobrescribir speak() para decir "Miau"


class Animal:
    def __init__(self, name):
        self.name = name 
        
    def speak(self):
        return "Hace un sonido"
    
class Dog(Animal):
    def speak(self):
        return "Guau"
    

class Cat(Animal):
    def speak(self):
        return "Miau"
    
try:
    dog_name = input("Ingrese el nombre del perro: ")
    cat_name = input("Ingrese el nombre del gato: ")
    
    dog = Dog(dog_name)
    cat = Cat(cat_name)
    
    print(dog.speak())
    print(cat.speak())
except Exception as e:
    print("Error: ", e)
    
        