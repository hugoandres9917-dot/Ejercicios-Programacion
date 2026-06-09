
#ejercicio 1 estructura de Datos Stack

#Cree una estructura de objetos que asemeje un Stack.
#Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
#Debe incluir un método para hacer print de toda la estructura.
#No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push (self, value):
        new = Node(value)
        new.next = self.top
        self.top = new
        
    def pop (self):
        if self.top is None:
            return None
        
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value
    
    def print(self):
        current = self.top #
        while current is not None:# 
            print(current.value)
            current = current.next
        
        
        
        