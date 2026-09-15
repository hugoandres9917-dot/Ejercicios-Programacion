##Ejercicio  de SQL en Python.

#Tarea 1: Crear y popular la DB realido en postgres ejercicio_sql_postgres.sql
#Tarea 2: Pruebas básicas de la DB
#Tarea 3: Creación del API

from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor #desempaquetamos el diccionario

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

def filter_table(table, valid_column, request_args):# requerimeintos filtrar cualquier tabla por cualquier columna
    query = f"SELECT * FROM {table}"
    cond = []
    values = []
    
    for key, val in request_args.items():
        if key in valid_column:#validadcion del parametro
            cond.append(f"{key} = %s") #uso de marcadores// no concatenar
            values.append(val)# valores en lista
            
    if cond:
        query += " WHERE " + " AND ".join(cond)#
        
    return query, values


# creacion de usuario (POST)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute( 
            """ 
            INSERT INTO users (name, email, username, password, date_birth, status)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING *;b 
            """,
            (data['name'], data['email'], data['username'], 
            data['password'], data['date_birth'], data.get('status', 'activo'))
        )
        res = cur.fetchone() 
        return jsonify(res), 201
    except Exception as e:
        conn.rollback()# 
        return jsonify({"error": str(e)}), 400
    finally:
        cur.close()
        conn.close()

@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute(
            """
            INSERT INTO vehicles (brand, model, year, status)
            VALUES (%s, %s, %s, %s) RETURNING *;
            """,
            (data['brand'], data['model'], data['year'], 
            data.get('status', 'disponible'))
        )
        res = cur.fetchone()
        conn.commit()
        return jsonify(res), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cur.close()
        conn.close()

@app.route('/rentals', methods=['POST'])
def create_rental():
    data = request.get_json()
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)# devuelve dicc no tuplas para pasarlo a jsonify()
    try:  ###al alquilar el auto ocurren dos cosas: inserta la renta y  estado de auto a alquilado
        conn.commit()
        cur.execute( 
            "INSERT INTO rentals (user_id, auto_id, status) VALUES (%s, %s, 'activo') RETURNING *;",
            (data['user_id'], data['auto_id'])
        )
        rental = cur.fetchone()
        cur.execute("UPDATE vehicles SET status = 'alquilado' WHERE id = %s;", (data['auto_id'],))
        conn.commit()
        return jsonify(rental), 201
    except Exception as e:
        conn.rollback() ##si la segunda consulta falla usamos rollback para revertir la primer consulta
        return jsonify({"error": str(e)}), 400
    finally:## siempre cerrar el cursor y la conneccion al terminal
        cur.close()
        conn.close()

# modificaciones en estados de vehiculos (PATCH)


@app.route('/vehicles/<int:id>/status', methods=['PATCH'])# solo actualizamos un atributo espeficico
def change_vehicle_status(id):
    status = request.json.get('status')#
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("UPDATE vehicles SET status = %s WHERE id = %s RETURNING *;", (status, id))
    auto = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(auto) if auto else (jsonify({"error": "No encontrado"}), 404)

@app.route('/users/<int:id>/status', methods=['PATCH'])
def change_user_status(id):
    status = request.json.get('status')
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("UPDATE users SET status = %s WHERE id = %s RETURNING *;", (status, id))
    usuario = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(usuario) if usuario else (jsonify({"error": "No encontrado"}), 404)

@app.route('/rentals/<int:id>/completar', methods=['PATCH'])
def complete_rental(id):
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("UPDATE rentals SET status = 'completado' WHERE id = %s RETURNING *;", (id,))
        rent = cur.fetchone()
        if not rent:
            return jsonify({"error": "Alquiler no encontrado"}), 404
        cur.execute("UPDATE vehicles SET status = 'disponible' WHERE id = %s;", (rent['auto_id'],))
        conn.commit()
        return jsonify(rent)
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cur.close()
        conn.close()

@app.route('/rentals/<int:id>/status', methods=['PATCH'])
def change_rental_status(id):
    status = request.json.get('status') 
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("UPDATE rentals SET status = %s WHERE id = %s RETURNING *;", (status, id))## devuelve la fila actualizada en la misma consulta para asi ahorranos un SELECT extra de respuesta
    rent = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(rent) if rent else (jsonify({"error": "No encontrado"}), 404)

@app.route('/users/<int:id>/moroso', methods=['PATCH'])
def flag_user_deliquent(id):
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("UPDATE users SET status = 'moroso' WHERE id = %s RETURNING *;", (id,))
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(user) if user else (jsonify({"error": "No encontrado"}), 404)


# filtros con (GET)

@app.route('/users', methods=['GET'])
def list_users():
    columns = ['id', 'name', 'email', 'username', 'date_birth', 'status']
    query, values = filter_table('users', columns, request.args)
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, values)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(res)

@app.route('/vehicles', methods=['GET'])
def list_vehicles():
    columns = ['id', 'brand', 'model', 'year', 'status']
    query, values = filter_table('vehicles', columns, request.args)
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, values)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(res)

@app.route('/rentals', methods=['GET'])
def list_rentals():
    columns = ['id', 'user_id', 'auto_id', 'status']
    query, values = filter_table('rentals', columns, request.args)
    conn = get_database_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, values)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, port=5000)