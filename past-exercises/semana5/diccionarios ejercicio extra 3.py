products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
    
]


# Diccionario para acumular totales por categoría
total_for_category = {}

# Recorrer la lista de productos
for product in products:
    category = product['category']
    price = product['price']
    total_for_category[category] = total_for_category.get(category, 0) + price

# Mostrar el resultado
print(total_for_category)


