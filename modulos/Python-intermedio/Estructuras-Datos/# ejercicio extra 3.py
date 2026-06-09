# ejercicio extra 3

#Lista doblemente enlazada
#Requisitos:
#Cada nodo debe tener referencia al siguiente y al anterior
#Métodos:
#append(data): Agrega al final
    #Salida (print_forward):
    #Salida (print_bacward)
#prepend(data): Agrega al inicio
    #Salida(print_forward):
    #Salida(print_backward):
#delete(data): Elimina el primer nodo con ese valor
    #Salida(print_forward):
    #Salida(print_backward):
#print_forward() y print_backward(): Imprime en ambas direcciones

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, data):
        new = Node(data)
        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        self.size += 1
        
    
    def prepend(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self.size += 1
        
        
    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is None:# es el head
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current.next is None:# es el tail
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1
                return
            current = current.next
            
    
    def print_forward(self):
        current = self.head
        show = ""
        while current is not None:
            show += f"[{current.data}]"
            if current.next is not None:
                show += " <-> "
            current = current.next
        print(show if show else "Lista vacia")
        
        
    def print_backward(self):
        current = self.tail
        show = ""
        while current is not None:
            show += f"[{current.data}]"
            if current.next is not None:
                show += " <-> "
            current = current.next
        print(show if show else "Lista vacia")
        
# Metodo de uso 

doubly_linkedlist = DoublyLinkedList()

doubly_linkedlist.append(10)
doubly_linkedlist.append(20)
doubly_linkedlist.prepend(5)

doubly_linkedlist.print_forward()
doubly_linkedlist.print_backward()

#ELIMIANDO NODO

doubly_linkedlist.delete(10)
doubly_linkedlist.print_forward()
doubly_linkedlist.print_backward()


            