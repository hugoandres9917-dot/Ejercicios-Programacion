# Main
#ejercicio extra de ORM,
# Filtros avanzados con SQLAlchemy,
# Relaciones bidireccionales y acceso simplificado
# Seed inicial con datos falsos usando Faker

from database import init_db
from CRUD_manager import UserManager, VehicleManager, AddressManager
from faker import Faker

def populate_database():
    fake = Faker()
    print("\n--- Poblando la base de datos con datos de prueba ---")

    # Crear usuarios
    users = []
    for _ in range(20):
        name = fake.name()
        email = fake.unique.email() # Usamos unique para evitar duplicados de correo
        user = UserManager.create_user(name=name, email=email)
        users.append(user)

        # Crear direcciones para cada usuario (asegurando que algunas lleven la palabra "Calle")
        for _ in range(fake.random_int(min=1, max=3)):
            calle = f"Calle {fake.street_name()}" if fake.boolean() else fake.street_address()
            AddressManager.create_address(calle, fake.city(), user.id)
            
        # Crear vehiculos para cada usuario (0 a 3)
        brands = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan']
        for _ in range(fake.random_int(min=0, max=3)):
            VehicleManager.create_vehicle(fake.random_element(brands), fake.word(), user.id)
            
    # Crear vehiculos sin dueño (huerfanos) fuera del ciclo de usuarios
    brands = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan']
    for _ in range(5):  
        VehicleManager.create_vehicle(fake.random_element(elements=brands), fake.word(), user_id=None)
            
    print("Base de datos poblada con exito")
        
if __name__ == "__main__":
    # 1. Inicializar la base de datos (verifica y crea tablas si no existen)
    init_db()
    
    # Si la base de datos está vacia, la poblamos con Faker
    if not UserManager.get_all_users():
        populate_database()
    else:
        print("\n--- La base de datos ya contiene registros. Usando datos existentes... ---")

    print("\n--- EJERCICIOS EXTRA DE ORM ---")

    # 2. Probar la relación bidireccional y acceso simplificado (Ejercicio 2)
    all_users = UserManager.get_all_users()
    if all_users:
        user_test = all_users[0]
        print(f"\n--- PRUEBA RELACIONES PARA USUARIO ID: {user_test.id} ({user_test.name}) ---")
        UserManager.get_user_with_vehicles_and_addresses(user_id=user_test.id)
    else:
        print("No hay usuarios registrados en la base de datos.")

    # 3. Probar usuarios con multiples vehiculos (Ejercicio 1)
    print("\n--- USUARIOS CON MÁS DE UN VEHÍCULO ---")
    
    multiple_users = UserManager.get_users_with_multiple_vehicles()
    if multiple_users:
        for u in multiple_users:
            print(f"- {u.name} (ID: {u.id}) - Total autos: {len(u.autos)}")
    else:
        print("No se encontraron usuarios con multiples vehiculos.")

    # 4. Probar vehiculos sin dueño (Ejercicio 1)
    print("\n--- VEHICULOS SIN USUARIO ---")
    
    orphan_cars = VehicleManager.get_vehicles_without_user()
    if orphan_cars:
        for v in orphan_cars:
            print(f"- {v.brand} {v.model} (ID: {v.id})")
    else:
        print("No hay vehiculos huerfanos registrados.")
        
    # 5. Probar direcciones que contienen la palabra "Calle" (Ejercicio 1)
    print("\n--- DIRECCIONES QUE CONTIENEN 'Calle' ---")
    
    calle_addresses = AddressManager.get_addresses_by_street_substring("Calle")
    if calle_addresses:
        for addr in calle_addresses:
            print(f"- {addr.street}, {addr.city} (User ID: {addr.user_id})")
    else:
        print("No se encontraron direcciones con el criterio 'Calle'.")