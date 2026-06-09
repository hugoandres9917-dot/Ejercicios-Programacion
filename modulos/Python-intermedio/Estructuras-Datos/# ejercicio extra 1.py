# ejercicio extra 1

#Cree una estructura que represente una cola básica (Queue) con objetos enlazados
#Restricción:
#no usar list, dict, tuple, collections
#Métodos requeridos:
#enqueue(data): agrega un nodo al final
#dequeue(): elimina y retorna el nodo del inicio
#print_all(): imprime todos los elementos de la cola en orden

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self. size = 0
        
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        
    def dequeue(self):
        if self.front is None:
            raise Exception("Queue is empty")
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return value
    
    def print_all(self):
        current = self.front
        show = ""
        while current is not None:
            show += str(current.data) + " "
            current = current.next
        print(show) 
        

# uso de la cola
# Crear una instancia de la cola
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.print_all()  

#prueba de eliminación
print("Elemento eliminado:", q.dequeue())
q.print_all()



