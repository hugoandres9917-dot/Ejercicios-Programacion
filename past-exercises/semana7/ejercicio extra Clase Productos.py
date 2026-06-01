#ejercicio Cree una clase Product con:
#Nombre, precio y cantidad
#Cree una clase Inventory que:
#Guarde productos en una lista
#Tenga métodos para:
#Agregar un producto
#Mostrar todos los productos
#Calcular el valor total del inventario

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"{self.name} - Precio: {self.price} - Cantidad: {self.quantity}"    

class Inventory:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def show_products(self):
        for product in self.products:
            print(product)
            
    def calculate_total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        return total
    
try:
    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Smartphone", 500, 10)
    
    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)
    
    inventory.show_products()
    print("Valor total del inventario: ", inventory.calculate_total_value())
except Exception as e:
    print("Error: ", e)
    
    