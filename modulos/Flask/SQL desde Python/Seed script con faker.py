#Seed script con faker

##generar al menos 200 usuarios y 100 automóviles falsos
##inserte estos datos automáticamente en las tablas usuarios y automoviles
##cree 50 y 150 registros aleatorios en la tabla alquileres, simulando un histórico de alquileres

import random
import psycopg2
from faker import Faker

#conneccion a la base de datos

DB_CONF = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Antonella60",
    "host": "localhost",
    "port": "5432"
}

fake = Faker('es_ES')

def seed_database():
    conn = None
    try:
        conn =psycopg2.connect(**DB_CONF)
        cursor = conn.cursor()
        cursor.execute("SET search_path TO lyfter_car_rental;")
    
        print("Poblando usuarios...")
        users_data = []
        user_statuses = ['active', 'inactive', 'suspended', 'delinquent']
        for _ in range(200):#agregar 200 usuarios
            profile = fake.simple_profile()
            users_data.append((
                fake.name(),
                fake.unique.email(),
                fake.unique.user_name(),
                fake.password(length=12),
                fake.date_of_birth(minimum_age=18, maximum_age=75),
                random.choice(user_statuses)
            ))
        
        insert_user_query = """
            INSERT INTO users (name, email, username, password, date_birth, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(insert_user_query, users_data)
    
        print("Poblando vahiculos...")
        brands = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'Hyundai', 'BMW', 'Volkswagen', 'Mazda', 'Kia']
        vehicle_statuses = ['available', 'rented', 'maintenance', 'unavailable']
        vehicles_data = []
        for _ in range(100):#agregar 100 vehiculos
            vehicles_data.append((
                random.choice(brands),
                fake.word().capitalize(),
                random.randint(2015, 2024),
                random.choice(vehicle_statuses)
            ))
        
        insert_vehicles_query = """
            INSERT INTO vehicles (brand, model, year, status)
            VALUES (%s, %s, %s, %s):
        """
    
    #obtener ID reales de usarios y vehiculos para referencialos
        cursor.execute("SELECT id FROM users;")
        user_ids = [row[0] for row in cursor.fetchall()]
    
        cursor.execute("SELECT id FROM vehicles;")
        vehicle_ids = [row[0] for row in cursor.fetchall()]


        print("Poblando alquileres...")
        num_rentals = random.randint(50, 150)
        rentals_statuses = ['active', 'completed', 'cancelled']
        rentals_data = []
        for _ in range(num_rentals):
            rentals_data.append((
                random.choice(user_ids),
                random.choice(vehicle_ids),
                fake.date_time_this_year(),
                random.choice(rentals_statuses)
            ))
        
        insert_rentals_query = """
            INSERT INTO rentals (user_id, auto_id, rental_date, status)
            VALUES(%s, %s, %s, %s)
        """
    
        cursor.executemany(insert_rentals_query, rentals_data)
    
        conn.commit()
        print(f'Base de datos poblada exitosamente con 200 usuarios, 100 vehiculos, {num_rentals} alquileres')

    except Exception as error:
        if conn:
            conn.rollback()
        print(f"Error al poblar la base de datos: {error}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            
            
if __name__ == "__main__":
    seed_database()