# ejercicio extra 2

#Cree una clase LinkedList con los métodos:
#insert_front(data): Inserta al inicio
#insert_back(data): Inserta al final 
#delete(data): Elimina el primer nodo con el valor dado
#print_all(): Imprime todos los valores

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insert_front(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size += 1
        
        
    def insert_back(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = new
        self.size += 1


    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return

        actual = self.head
        while actual.next is not None:
            if actual.next.data == data:
                actual.next = actual.next.next
                self.size -= 1
                return
            actual = actual.next

    def print_all(self):
        current = self.head
        show = ""
        while current is not None:
            show += f"[{current.data}]"
            if current.next is not None:
                show += " -> "
            current =current.next
        print(show if show else "lista vacia")
        
        
#como aplicarlo

linked_list = LinkedList()
linked_list.insert_front(10)
linked_list.insert_back(20)
linked_list.insert_front(5)
linked_list.insert_back (30)

linked_list.print_all()

#eliminando elemento 

linked_list.delete(10)
linked_list.print_all()
        
        
        