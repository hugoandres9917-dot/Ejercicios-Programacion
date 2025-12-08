#ejercicio 1 semana 14

class Node:
    def __init__(self, value ):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
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
        current = self.top
        while current is not None:
            print(current.value)
            current =current.next



    