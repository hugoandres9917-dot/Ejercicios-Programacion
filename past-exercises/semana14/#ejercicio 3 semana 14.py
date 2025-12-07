#ejercicio 3 semana 14

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)

        if self.root is None:
            self.root = new
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    return
                current = current.right

    def print_tree(self):
        self._print_inorder(self.root)
        print()  # salto de línea final

    def _print_inorder(self, node):
        if node is None:
            return
        
        self._print_inorder(node.left) # Recorrer hijo izquierdo

        print(f"[{node.data}]", end=" ") # 
        
        self._print_inorder(node.right)


tree = BinaryTree() #aqui lo ponemos en uso

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

tree.print_tree()