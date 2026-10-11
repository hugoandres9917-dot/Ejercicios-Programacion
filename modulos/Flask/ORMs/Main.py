# Main

#ejercicios de ORMs

#setup de SQLAIchemy, adjunte un screenshot de la validacion de la version de la bibilioteca

##print(f"Versión de SQLAlchemy: {sqlalchemy.__version__}")

#####Versión de SQLAlchemy: 2.1.1##

##2. Plantee una base de datos con tablas para usuarios, direcciones y automoviles.


from database import init_db
from CRUD_manager import UserManager, VehicleManager, AddressManager

if __name__ == "__main__":
    init_db()# 1. Valida si las tablas existen y las crea solo si no existen (sin borrar datos previos)
    print("\n--- 1. Usuarios ---")
    try:
        u1 = UserManager.create_user("Hugo Alvarado", "hugo@example.com")
        print(f"Usuario creado: {u1}")
    except ValueError:
        # Si ya existe en la base de datos persistente, lo recuperamos para continuar la prueba
        u1 = UserManager.get_all_users()[0]
        print(f"Usuario recuperado (ya existia): {u1}")

    try:
        u2 = UserManager.create_user("Maria Lopez", "maria@example.com")
        print(f"Usuario creado: {u2}")
    except ValueError:
        u2 = UserManager.get_all_users()[1] if len(UserManager.get_all_users()) > 1 else u1
        print(f"Usuario recuperado (ya existia): {u2}")
    UserManager.update_user(u1.id, name="Hugo A. Alvarado")
    
    print("\n--- 2. AUTOMOVILES ---")
    v1 = VehicleManager.create_vehicle("Toyota", "Corolla")
    v2 = VehicleManager.create_vehicle("Honda", "Civic")
    print(f"Automoviles creados: {v1}, {v2}")
    VehicleManager.update_vehicle(v1.id, model="Corolla Hybrid")
    VehicleManager.delete_vehicle(v2.id)

    print("\n--- 3. DIRECCIONES ---")
    addr1 = AddressManager.create_address("Av. Central 123", "San José", u1.id)
    if addr1:
        print(f"Dirección creada: {addr1}")
        AddressManager.update_address(addr1.id, street="Av. Central 456")
        
    print("\n--- 4. ASOCIAR VEHICULO ---")
    v1_associated = VehicleManager.assign_vehicle_to_user(v1.id, u1.id)
    print(f"Vehiculo asociado: {v1_associated}")

    print("\n--- 5. CONSULTA USUARIOS ---")
    print(UserManager.get_all_users())
    
    print("\n--- 6. CONSULTA AUTOMOVILES ---")
    print(VehicleManager.get_all_vehicles())

    print("\n--- 7. CONSULTA DIRECCIONES ---")
    print(AddressManager.get_all_addresses())