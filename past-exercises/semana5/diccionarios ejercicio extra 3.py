products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
    
]


# Diccionario para acumular totales por categoría
total_por_categoria = {}

# Recorrer la lista de productos
for producto in products:
    categoria = producto['category']
    precio = producto['price']
    total_por_categoria[categoria] = total_por_categoria.get(categoria, 0) + precio

# Mostrar el resultado
print(total_por_categoria)


