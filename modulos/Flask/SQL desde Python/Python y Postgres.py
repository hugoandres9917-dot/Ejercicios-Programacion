#Python y Postgres

#instalar psycopg2 ##  pip3 install psycopg2-binary

#creamos la base de datos en postgres con el nombre de postgres
#CREATE TABLE lyfter_duad.users(
#	id SERIAL PRIMARY KEY,
#	full_name VARCHAR(30),
#	email VARCHAR(20),
#	password VARCHAR(20)
#);

#INSERT INTO lyfter_duad.users (full_name, email, password) values ('Manuel Vega', 'm.vega@gmail.com', 'A1SFA3!!');
#INSERT INTO lyfter_duad.users (full_name, email, password) values ('Carlos Antonio', 'c.antonio@yahoo.com', '2001_02_03'); # type: ignore
#INSERT INTO lyfter_duad.users (full_name, email, password) values ('Jose Mora', 'j.mora@gmail.com', 'password123');
#INSERT INTO lyfter_duad.users (full_name, email, password) values ('Alfred Lopez', 'alfredlo@hotmail.com', 'alfredLP.');


# conectarnos a la base de datos
import psycopg2


connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="Antonella60",
    dbname="postgres",
)
print("Connected to the database")

#crear un Cursor.
#Los cursores nos permiten ejecutar operaciones en la db y obtener resultados de uno en uno.
#cursor = connection.cursor()

cursor =  connection.cursor()

cursor.execute("SELECT version();")
print("Query executed")

#método del cursor: el fetchall()

results = cursor.fetchall()
print(results)

# resultados vienen en una lista de tuplas.


#Lectura de datos

import psycopg2


connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="123",
    dbname="postgres",
)
print("Connected to database!")

cursor = connection.cursor()

cursor.execute("SELECT id, full_name, email, password FROM lyfter_duad.users;")
print("Query executed")

results = cursor.fetchall()
print(results)

#Connected to database!
#Query executed
#[(1, 'Manuel Vega', 'm.vega@gmail.com', 'A1SFA3!!'),
# # (2, 'Carlos Antonio', 'c.antonio@yahoo.com', '2001_02_03'),
# (3, 'Jose Mora', 'j.mora@gmail.com', 'password123'),
# (4, 'Alfred Lopez', 'alfredlo@hotmail.com', 'alfredLP.')]

#podemos notar lo que mencionamos antes sobre la lista de tuplas.

#solución rápida es crear una pequeña función
# para convertir esta lista de tuplas en una lista de diccionarios:

def format_user(user_record):
    return {
        "id": user_record[0],
        "full_name": user_record[1],
        "email": user_record[2],
        "password": user_record[3],
    }

# (...)

results = cursor.fetchall()
formatted_results = [format_user(result) for result in results]
print(formatted_results)

#✅
#Connected to database!
#Query executed
#[{'id': 1, 'full_name': 'Manuel Vega', 'email': 'm.vega@gmail.com', 'password': 'A1SFA3!!'},
# {'id': 2, 'full_name': 'Carlos Antonio', 'email': 'c.antonio@yahoo.com', 'password': '2001_02_03'},
# {'id': 3, 'full_name': 'Jose Mora', 'email': 'j.mora@gmail.com', 'password': 'password123'},
# {'id': 4, 'full_name': 'Alfred Lopez', 'email': 'alfredlo@hotmail.com', 'password': 'alfredLP.'}]

#############
#Escritura de datos

#aplicar estos cambios podemos usar el método commit del connection.

import psycopg2


connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="123",
    dbname="postgres",
)
print("Connected to database!")

cursor = connection.cursor()

cursor.execute("INSERT INTO lyfter_duad.users (full_name, email, password) values ('Juan Jose Restrepo', 'juan.jo@hotmail.es', '1235');")
print("Query executed")

connection.commit()### COMMIT para guardar los cambios en la base de datos
print("Connection changes committed")

#SQL Injections

#solución rápida es crear una pequeña función

import psycopg2


# Endpoint hipotético

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="123",
    dbname="postgres",
)
print("Connected to database!")

request_body = {
    "full_name": "Juan Jose Restrepo', 'juan.jo@hotmail.es', '1235'); DELETE FROM lyfter_duad.users; --",
    "email": "juan.jo@hotmail.es",
    "password": "1235",
}

full_name = request_body.get("full_name")
email = request_body.get("email")
password = request_body.get("password")

cursor = connection.cursor()

cursor.execute(
    f"INSERT INTO lyfter_duad.users (full_name, email, password)
    values (%s, %s, %s);", (full_name, email, password,)# marcadores de posición para evitar SQL Injection
)
print("Query executed")

connection.commit()
print("Connection changes committed")


#Limpiando el código

#utilizando clases
#crear una clase que nos ayude a automatizar las preparaciones para ejecutar queries.
#Como la creación del connection, del cursor, y los commits.
#refactorizar la creación de la conexión y del cursor

#ANTES

import psycopg2


connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="123",
    dbname="postgres",
)
print("Connected to database!")

cursor = connection.cursor()

#DESPUES

import psycopg2


class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name= db_name
        self.user= user
        self.password = password
        self.host = host
        self.port = port
        
        self.connection = self.create_connection()
        if self.connection:
						print("Connected to database!")
            self.cursor = self.connection.cursor()
        
    def create_connection(self):
        try:
            connection = psycopg2.connect(
	            dbname=self.db_name,
	            user=self.user,
	            password=self.password,
	            host=self.host,
	            port=self.port,
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None

pg_manager = PgManager()

###

import psycopg2


class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name= db_name
        self.user= user
        self.password = password
        self.host = host
        self.port = port
        
        self.connection = self.create_connection(db_name, user, password, host, port)
        if self.connection:
            self.cursor = self.connection.cursor()
            print("Connection created succesfully")
        
    def create_connection(self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
	            dbname=db_name,
	            user=user,
	            password=password,
	            host=host,
	            port=port,
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None
            
   def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")
        
        
###cerrar la conexión al terminar de utilizarla.
#método que nos permitirá correr queries usando el cursor previamente creado.
#Podemos usar los *args (vistos en Parámetros infinitos)
# para pasarle como parámetros los valores del query y evitar así los SQL desde Python
# - Sección SQL Injections.

import psycopg2


class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name= db_name
        self.user= user
        self.password = password
        self.host = host
        self.port = port
        
        self.connection = self.create_connection(db_name, user, password, host, port)
        if self.connection:
            self.cursor = self.connection.cursor()
            print("Connection created succesfully")
        
    def create_connection(self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")
 
    def execute_query(self, query, *args):
        self.cursor.execute(query, args)
        result = self.cursor.fetchall()
        self.connection.commit()

        return result

#Resultado

from db import PgManager


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)

results = db_manager.execute_query("SELECT * FROM users;")
print(results)

db_manager.close_connection()

#l atributo description del cursor.

import psycopg2


class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.create_connection(db_name, user, password, host, port)
        if self.connection:
            self.cursor = self.connection.cursor()
            print("Connection created succesfully")

    def create_connection(self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port,
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")

    def execute_query(self, query, *args):
        self.cursor.execute(query, args)
        self.connection.commit()

        # Revisamos si el query devolvió algo
        if self.cursor.description:
            results = self.cursor.fetchall()
            return results
