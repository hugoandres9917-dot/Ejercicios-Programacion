#ejercicio 2 semana 14

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #apuntar al siguiente
        self.prev = None #apuntar al anterior

class Deque:
    def __init__(self):
        self.head = None #primer nodo
        self.tail = None#ultimo
        self.size = 0 #cantidad

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