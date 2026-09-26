#Seed script con faker

##generar al menos 200 usuarios y 100 automoviles falsos
##inserte estos datos automaticamente en las tablas usuarios y automoviles
##cree 50 y 150 registros aleatorios en la tabla alquileres, simulando un historico de alquileres

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
        conn = psycopg2.connect(**DB_CONF)
        cursor = conn.cursor()
        cursor.execute("SET search_path TO lyfter_car_rental;")
        
        
        print("Limpiando tablas...")
        cursor.execute("TRUNCATE TABLE rentals, vehicles, users RESTART IDENTITY CASCADE;")
        fake.unique.clear()## Limpiar el historial de valores unicos de Faker
    
        # Poblar usuarios
        print("Poblando usuarios...")
        users_data = []
        user_statuses = ['active', 'inactive', 'suspended', 'delinquent']
        for _ in range(200):  # Agregar 200 usuarios
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
    
        # Poblar vehiculos
        print("Poblando vehículos...")
        brands = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'Hyundai', 'BMW', 'Volkswagen', 'Mazda', 'Kia']
        vehicle_statuses = ['available', 'rented', 'maintenance', 'unavailable']
        vehicles_data = []
        for _ in range(100):  # Agregar 100 vehículos
            vehicles_data.append((
                random.choice(brands),
                fake.word().capitalize(),
                random.randint(2015, 2024),
                random.choice(vehicle_statuses)
            ))
        #insercion de 100 vehiculos
        insert_vehicles_query = """
            INSERT INTO vehicles (brand, model, year, status)
            VALUES (%s, %s, %s, %s)
        """
        cursor.executemany(insert_vehicles_query, vehicles_data) #CORRECCIÓN: Se ejecuta la consulta con executemany
        
    #Obtener IDs generados para relacionarlos con los alquileres  
        cursor.execute("SELECT id FROM users;") 
        user_ids = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT id FROM vehicles;")
        vehicle_ids = [row[0] for row in cursor.fetchall()]

        # 4. Poblar alquileres
        print("Poblando alquileres...")
        rentals_data = []
        rental_statuses = ['completed', 'active', 'cancelled']
        num_rentals = random.randint(50, 150)  # Rango de 50 a 150 alquileres

        for _ in range(num_rentals):
            rental_datetime = fake.date_time_between(start_date='-1y', end_date='now')
            rentals_data.append((
                random.choice(user_ids),
                random.choice(vehicle_ids),
                rental_datetime,
                random.choice(rental_statuses)
            ))

        insert_rentals_query = """
            INSERT INTO rentals (user_id, auto_id, rental_date, status)
            VALUES (%s, %s, %s, %s)
        """
        cursor.executemany(insert_rentals_query, rentals_data)

    #commit para confirmacion
        conn.commit()
        print("Base de datos poblada exitosamente con usuarios, vehículos y alquileres.")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error al poblar la base de datos: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

            
if __name__ == "__main__":
    seed_database()