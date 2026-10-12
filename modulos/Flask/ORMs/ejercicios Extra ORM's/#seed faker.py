#seed faker

import random
from faker import Faker
from database import init_db
from CRUD_manager import UserManager, AddressManager, VehicleManager

fake = Faker()

def run_seed():
    init_db()  # Inicializa la base de datos y crea las tablas
    print("poblando base de datos mediante faker...")
    
    
    #crear 20 usuarios.
    
    users =[]
    for _ in range(20):
        user =UserManager.create_user(
            name=fake.name(),
            email=fake.email()
        )   
        users.append(user)
        
    #crear 1 o 2 direciones para cada usuario
    for user in users:
        for _ in range(random.randint(1, 2)):
            address = AddressManager.create_address(
                street=fake.street_address(),
                city=fake.city(),
                user_id=user.id
            )
            
    #crear 0 a 3 automoviles para cada usuario
    brands = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
    for _ in range(25):
        assigned_user = random.choice(users)
        VehicleManager.create_vehicle(
            brand=random.choice(brands),
            model=fake.word(),
            user_id=assigned_user.id
        )   
        
    #crear 5 automoviles sin usuario asociado
    for _ in range(5):
        VehicleManager.create_vehicle(
            brand=random.choice(brands),
            model=fake.word(),
            user_id=None
        )
        
    print("Base de datos poblada con éxito.")
    
if __name__ == "__main__":
    run_seed()
    #
    