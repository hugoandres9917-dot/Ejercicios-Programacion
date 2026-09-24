##Ejercicio  de SQL en Python.

#Tarea 1: Crear y popular la DB realido en postgres ejercicio_sql_postgres.sql
#Tarea 2: Pruebas básicas de la DB
#Tarea 3: Creación del API

##Rutas HTTP
##Las rutas quedan completamente limpias de SQL,
##limitándose a procesar peticiones y enviar respuestas HTTP.

from flask import Flask, request, jsonify
import psycopg2
from repositorio import UserRepository, VehicleRepository, RentalRepository

app = Flask(__name__)

DataBase_CONFIG = {
    "dbname": "lyfter_car_rental",
    "user": "postgres",
    "password": "Antonella60",
    "host": "localhost",
    "port": "5432"
}

def get_database_connection():
    conn = psycopg2.connect(**DataBase_CONFIG) #centralizamos la coneccion
    with conn.cursor() as cur:
        cur.execute("SET search_path TO lyfter_car_rental;")#usamos este SET para conectar, evita escribir en cada consulta ejem: lyfter_car_rental.users
    return conn

###################################################################################################
#usuarios // rutas  y metodos que tiene relacion con users
#####################################################################################

@app.route('/users', methods=['POST'])
def create_user():
    conn = get_database_connection()
    repo = UserRepository(conn)
    try:
        user = repo.create(request.get_json())
        conn.commit()
        return jsonify(user), 201
    except Exception as e:
        conn.rollback()# 
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()
        
        

@app.route('/users', methods=['GET'])
def list_users():
    conn = get_database_connection()
    repo = UserRepository(conn)
    try:
        users = repo.get_all(request.args)
        return jsonify(users), 200
    except Exception as  e:
        return jsonify({"Error": str(e)}), 400 
    finally:   
        conn.close()


@app.route('/users/<int:id>/status', methods=['PATCH'])
def change_user_status(id):
    conn = get_database_connection()
    repo = UserRepository(conn)
    try:
        data = request.get_json() or {}
        status = data.get('status')
        user = repo.update_status(id, status)
        if not user:
            return jsonify({"error": "No encontrado"}), 404
        conn.commit()
        return jsonify(user), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()
    
@app.route('/users/<int:id>/delinquent', methods=['PATCH'])
def flag_user_deliquent(id):
    conn = get_database_connection()
    repo = UserRepository(conn)
    try:
        # Se envía exactamente 'delinquent' que coincide con el ENUM status_users
        user = repo.update_status(id, 'delinquent')
        if not user:
            return jsonify({"error": "No encontrado"}), 404
        conn.commit()
        return jsonify(user), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()


##########################################################################################
        ##vehiculos // rutas que tiene relacion con vehicles
##########################################################################################        

@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    conn = get_database_connection()
    repo = VehicleRepository(conn)
    try:
        data = request.get_json()
        vehicle = repo.create(data)
        conn.commit()
        return jsonify(vehicle), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()
        
@app.route('/vehicles', methods=['GET'])
def list_vehicles():
    conn = get_database_connection()
    repo = VehicleRepository(conn)
    try:
        vehicles = repo.get_all(request.args)
        return jsonify(vehicles), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()
        
    
@app.route('/vehicles/<int:id>/status', methods=['PATCH'])# solo actualizamos un atributo espeficico
def change_vehicle_status(id):
    conn = get_database_connection()
    repo = VehicleRepository(conn)
    try:
        data = request.get_json() or {}
        status = data.get('status')
        vehicle = repo.update_status(id, status)
        if not vehicle:
            return jsonify({"error": "No encontrado"}), 404
        conn.commit()
        return jsonify(vehicle), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()
        
#################################################################################################
    ## alquileres rutas y metodos relacionados con rental
################################################################################################

@app.route('/rentals', methods=['POST'])
def create_rental():
    conn = get_database_connection()
    repo = RentalRepository(conn)
    try: 
        rental = repo.create(request.get_json())
        conn.commit()
        return jsonify(rental), 201
    except ValueError as ve:
        conn.rollback()
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        conn.rollback() ##si la segunda consulta falla usamos rollback para revertir la primer consulta
        return jsonify({"error": str(e)}), 400
    finally:## siempre cerrar el cursor y la conneccion al terminal
        conn.close()


@app.route('/rentals', methods=['GET'])
def list_rentals():
    conn = get_database_connection()
    repo = RentalRepository(conn)
    try:
        rentals = repo.get_all(request.args)
        return jsonify(rentals), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()


@app.route('/rentals/<int:id>/complete', methods=['PATCH'])
def complete_rental(id):
    conn = get_database_connection()
    repo = RentalRepository(conn)
    try:
        rental = repo.complete_rental(id)
        if not rental:
            return jsonify({"error": "alquiler no encontrado"}), 404
        return jsonify(rental)
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()

@app.route('/rentals/<int:id>/status', methods=['PATCH'])
def change_rental_status(id):
    conn = get_database_connection()
    repo = RentalRepository(conn)
    try:
        data = request.get_json() or {}
        status = data.get('status') 
        rental = repo.update_status(id, status)
        if not rental:
            return jsonify({"error": "No encontrado"}), 404
        conn.commit()
        return jsonify(rental), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()
        
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)



