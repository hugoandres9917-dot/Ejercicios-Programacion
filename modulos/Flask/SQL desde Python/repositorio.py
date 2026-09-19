# repositorio

# SQL Separado por clases segun su entidad
#flask no maneja logica de base de datos 

from psycopg2.extras import RealDictCursor

class BaseRepository:
    def __init__(self, conn): ## 
        self.conn = conn

    def filter_table(self, table, valid_columns, request_args, select_columns="*"):
        query = f"SELECT {select_columns} FROM {table}" ##Filtra registros de las columnas especificadas.
        cond = []
        values = []
        
        for key, val in request_args.items():
            if key in valid_columns:
                cond.append(f"{key} = %s")
                values.append(val)
                
        if cond:
            query += " WHERE " + " AND ".join(cond)
            
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, values)
            return cur.fetchall()


class UserRepository(BaseRepository):
    SAFE_COLUMNS = "id, name, email, username, date_birth, status" ## exclimos password las repuestas

    def create(self, data):
        query = f"""
            INSERT INTO users (name, email, username, password, date_birth, status)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING {self.SAFE_COLUMNS};
        """
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                query,
                (
                    data['name'], 
                    data['email'], 
                    data['username'], 
                    data['password'], 
                    data['date_birth'], 
                    data.get('status', 'active') 
                )
            )
            user = cur.fetchone()
            self.conn.commit()
            return user

    def update_status(self, user_id, status):
        query = f"UPDATE users SET status = %s WHERE id = %s RETURNING {self.SAFE_COLUMNS};"
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, (status, user_id))
            user = cur.fetchone()
            self.conn.commit()
            return user

    def get_all(self, args):
        valid_cols = ['id', 'name', 'email', 'username', 'date_birth', 'status']
        # Omitimos la columna 'password' al listar usuarios
        return self.filter_table('users', valid_cols, args, select_columns=self.SAFE_COLUMNS)


class VehicleRepository(BaseRepository):
    def create(self, data):
        query = "INSERT INTO vehicles (brand, model, year, status) VALUES (%s, %s, %s, %s) RETURNING *;"
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                query,
                (data['brand'], data['model'], data['year'], data.get('status', 'available'))
            )
            vehicle = cur.fetchone()
            self.conn.commit()
            return vehicle

    def update_status(self, vehicle_id, status):
        query = "UPDATE vehicles SET status = %s WHERE id = %s RETURNING *;"
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, (status, vehicle_id))
            vehicle = cur.fetchone()
            self.conn.commit()
            return vehicle

    def get_all(self, args):
        valid_cols = ['id', 'brand', 'model', 'year', 'status']
        return self.filter_table('vehicles', valid_cols, args)


class RentalRepository(BaseRepository):
    def create(self, data):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            # Corregido: Validación previa para evitar doble alquiler de un mismo auto
            cur.execute("SELECT status FROM vehicles WHERE id = %s;", (data['auto_id'],))
            vehicle = cur.fetchone()

            if not vehicle:
                raise ValueError("El vehículo especificado no existe.")
            if vehicle['status'] == 'rented':
                raise ValueError("El vehículo ya se encuentra alquilado.")

            cur.execute(
                "INSERT INTO rentals (user_id, auto_id, status) VALUES (%s, %s, 'active') RETURNING *;",
                (data['user_id'], data['auto_id'])
            )
            rental = cur.fetchone()
            cur.execute("UPDATE vehicles SET status = 'rented' WHERE id = %s;", (data['auto_id'],))
            
            self.conn.commit()
            return rental

    def complete_rental(self, rental_id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("UPDATE rentals SET status = 'completed' WHERE id = %s RETURNING *;", (rental_id,))
            rental = cur.fetchone()
            if not rental:
                return None
            cur.execute("UPDATE vehicles SET status = 'available' WHERE id = %s;", (rental['auto_id'],))
            self.conn.commit()
            return rental  # Corregido: Cambia el estado del alquiler a 'completed' y libera el auto a 'available'

    def update_status(self, rental_id, status):
        query = "UPDATE rentals SET status = %s WHERE id = %s RETURNING *;"
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, (status, rental_id))
            rental = cur.fetchone()
            self.conn.commit()
            return rental

    def get_all(self, args):
        valid_cols = ['id', 'user_id', 'auto_id', 'status']
        return self.filter_table('rentals', valid_cols, args)
    
    