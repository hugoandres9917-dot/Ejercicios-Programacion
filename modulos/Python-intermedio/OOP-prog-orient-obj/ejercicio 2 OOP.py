#Cree una clase de Bus con:
#Un atributo de max_passengers.
#Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
#Un método para bajar pasajeros uno por uno (en cualquier orden).

class Person: #la persona que sube
    def __init__(self, name):
        self.name = name    

class Bus: # el autobus
    def  __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self,person):
        if len(self.passengers) < self.max_passengers:#revisa la lista de cantidad de pasajeros si aun quedan espacios            self.passengers.append(person)#agrega el pasajero
            print(f"{person.name} ha subido al autobus. ")
        else:
            print("El autobus es lleno. No se puede subir mas personas. ")

    def remove_passenger(self):
        if self.passengers:#revisa la lista de pasajeros
            person = self.passengers.pop()#elimina al pasajero indicado en los parenticis indicado mas abajo
            print(f"{person.name} ha bajado del autobus. ")
        else:
            print("No hay pasajeros para bajar. ")#no quedan pasajeros que bajar

person1 = Person("Hugo")
person2 = Person("Betzabeth")#creamos a las persona para subir al bus
person3 = Person("Josua")
bus = Bus(2)#capacidad max del bus
bus.add_passenger(person1)#agregamos personas
bus.add_passenger(person2)
bus.add_passenger(person3)#este no subira
bus.remove_passenger()#bajamos personas
bus.remove_passenger()
bus.remove_passenger()#aqui nos indicara que no queda nadie en el autobus