#ejercicio 2 Double Ended Queue 

#Cree una estructura de objetos que asemeje un Double Ended Queue.
#Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
#Debe incluir un método para hacer print de toda la estructura.
#No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Deque
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def push_left(self, data):
        new = Node(data)
        
       if self.head is None: #vasio
            self.head = new
            self.tail = new
        
        else:
            new.next = self.head #conectando nuevo con anterior
            self.head.prev = new# conectando anterior con nuevo
            self.head = new #head nuevo
        
        self.size += 1

    
    def push_right(self, data):
        new =Node(data)

        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            new.prev =self.tail
            self.tail.next = new
            self.tail = new
        
        self.size += 1

    def pop_left(self):
        if self.head is None: # vasio
            return None
        
        value = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return value
    
    def pop_right(self):
        if self.tail is None:
            return None
        
        value = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return value
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def print_deque(self):
        actual = self.head
        show = ""
        while actual is not None:
            show += f"[{actual.data}]"
            if actual.next is not None:
                show += "<->"
            actual = actual.next
        print(show if show else "Deque vacio")   


d = Deque()
d.push_left(10)
d.push_right(20)
d.push_left(5)
d.push_right(30)

d.print_deque()

print("Eliminado al frente", d.pop_left())
print("Eliminado atras:", d.pop_right())
d.print_deque()

