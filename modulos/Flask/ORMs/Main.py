# Main

#ejercicios de ORMs

#setup de SQLAIchemy, adjunte un screenshot de la validacion de la version de la bibilioteca

##print(f"Versión de SQLAlchemy: {sqlalchemy.__version__}")

#####Versión de SQLAlchemy: 2.1.1##

##2. Plantee una base de datos con tablas para usuarios, direcciones y automoviles.


from database import init_db
from CRUD_manager import UserManager, VehicleManager, AddressManager

# PRUEBA DE EJECUCION         
            
if __name__ == "__main__":
    #  Crear tablas si no existen
    init_db()

    print("\n--- 1. Usuarios")
    u1 = UserManager.create_user("Hugo Alvarado", "hugo@example.com")
    u2 = UserManager.create_user("Maria Lopez", "maria@example.com")
    print(f"Usuarios creados: {u1}, {u2}")
    
    UserManager.update_user(u1.id, name="Hugo A. Alvarado")
    UserManager.delete_user(u2.id)

    print("\n--- 2. AUTOMOVILES ---")
    v1 = VehicleManager.create_vehicle("Toyota", "Corolla")
    v2 = VehicleManager.create_vehicle("Honda", "Civic")
    print(f"Automoviles creados: {v1}, {v2}")
    
    VehicleManager.update_vehicle(v1.id, model="Corolla Hybrid")
    VehicleManager.delete_vehicle(v2.id)

    print("\n--- 3. DIRECCIONES ---")
    addr1 = AddressManager.create_address("Av. Central 123", "San José", u1.id)
    addr2 = AddressManager.create_address("Calle 5", "Heredia", u1.id)
    print(f"Direcciones creadas: {addr1}, {addr2}")
    
    AddressManager.update_address(addr1.id, street="Av. Central 456")
    AddressManager.delete_address(addr2.id)

    print("\n--- 4. ASOCIAR VEHICULO ---")
    v1_associated = VehicleManager.assign_vehicle_to_user(v1.id, u1.id)
    print(f"Vehiculo asociado: {v1_associated}")

    print("\n--- 5. CONSULTA USUARIOS ---")
    print(UserManager.get_all_users())
    
    print("\n--- 6. CONSULTA AUTOMOVILES ---")
    print(VehicleManager.get_all_vehicles())

    print("\n--- 7. CONSULTA DIRECCIONES ---")
    print(AddressManager.get_all_addresses())