#Repository Pattern     

#busca encapsular y abstraer todo lo necesario
#para acessar, modificar o eliminar datos 
#Clases faciles de utilizar
#4 OOP

#como implementar

#pasos de preparacion, el pgManager es el que se encarga de la conexion a la base de datos
# ejecutar el query consultas
#formatear los resultados de la consulta


from db import PgManager


def format_user(user_record):
    return {
        "id": user_record[0],
        "full_name": user_record[1],
        "email": user_record[2],
        "password": user_record[3],
    }


db_manager = PgManager(
    db_name="postgres", user="postgres", password="postgres", host="localhost"
)

results = db_manager.execute_query(
    "SELECT id, full_name, email, password FROM lyfter_duad.users;"
)
formatted_results = [format_user(result) for result in results]

print(formatted_results)

db_manager.close_connection()

#creamos clase que llamaremos UserRepository,contega lo necesario para recuperar, modificar y eliminar datos de la tabla users

#1. metodo get_all que ejecuta el query y formatea los resultados
#2. Como necesitamos esa instancia del PgManager (llamada db_manager en el código),
# podemos agregarlo como dependencia de UserRepository en su constructor.
# Esto debido a que nunca es bueno instanciar clases dentro de otras clases.


class UserRepository:# clase reutilizable que abstrae todo lo necesario para acceder a la tabla users
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):# _ identificador de metodo privado, no se puede acceder desde fuera de la clase
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "password": user_record[3],
        }

    def get_all(self):
        results = self.db_manager.execute_query(
            "SELECT id, full_name, email, password FROM users;"
        )
        formatted_results = [self._format_user(result) for result in results] 
        return formatted_results
    
#buena practica es envolver el metodo en un try-except

class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record[0], 
            "full_name": user_record[1],
            "email": user_record[2],
            "password": user_record[3],
        }

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, full_name, email, password FROM lyfter_duad.users;"
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False
        

#podemos intaciar la clase UserRepository y llamar al metodo get_all para obtener todos los usuarios
# de la tabla users si saber que sucede dentro de la clase, solo sabemos que nos devuelve una lista de diccionarios con los datos de los usuarios

#se necesita una instancia de Pgmanager para poder instanciar la clase UserRepository, por lo que podemos crear una funcion que nos devuelva una instancia
# de UserRepository con la instancia de PgManager ya creada


from db import PgManager
from repositories import UserRepository


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)
users_repo = UserRepository(db_manager)
formatted_results = users_repo.get_all()

print(formatted_results)

#codigo mas limpio y escalable, ya que si necesitamos cambiar la forma en que accedemos
# a la base de datos, solo necesitamos cambiar la clase PgManager y no el resto del codigo

#ANTES

from db import PgManager


def format_user(user_record):
    return {
        "id": user_record[0],
        "full_name": user_record[1],
        "email": user_record[2],
        "password": user_record[3],
    }


db_manager = PgManager(
    db_name="postgres", user="postgres", password="postgres", host="localhost"
)

results = db_manager.execute_query(
    "SELECT id, full_name, email, password FROM lyfter_duad.users;"
)
formatted_results = [format_user(result) for result in results]

print(formatted_results)

db_manager.close_connection()

#DESPUES

from db import PgManager
from repositories import UserRepository


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)
users_repo = UserRepository(db_manager)
formatted_results = users_repo.get_all()

print(formatted_results)

##EL CRUD
#al usar repository pattern, podemos crear metodos para cada una de las operaciones del CRUD
# (Create, Read, Update, Delete) en la clase UserRepository

#CREATE
#tenemos que ejecutar la consulta de INSERT a la base de datos

# ...

def create(self, full_name, email, password):
    try:
        self.db_manager.execute_query(
            "INSERT INTO lyfter_duad.users (full_name, email, password) VALUES (%s, %s, %s)",
            (full_name, email, password),
        )
        print("User inserted successfully")
        return True
    except Exception as error:
        print("Error inserting a user into the database: ", error)
        return False
    
    #READ
    #metodo get_all , pero para casos mas especificos
    #podemos usar get_by_id, get_by_email, etc. para obtener un usuario especifico de la tabla users
    
    # ...

def get_by_id(self, _id):
    try:
        results = self.db_manager.execute_query(
            "SELECT id, full_name, email, password FROM lyfter_duad.users WHERE id = %s;",
            (_id,),
        )
        formatted_result = self._format_user(results[0])
        return formatted_result
    except Exception as error:
        print("Error getting a user from the database: ", error)
        return False
    
    #UPDATE
    #metodo update, para actualizar un usuario especifico de la tabla users
    #depende de si que funcione con un put o un patch, si es un put, se actualizan todos los campos,.
    # si es un patch, se actualizan solo los campos que se envian en la peticion

# ...

def update(self, _id, full_name, email, password):
    try:
        self.db_manager.execute_query(
            "UPDATE lyfter_duad.users SET (full_name, email, password) = (%s, %s, %s) WHERE ID = %s",
            (full_name, email, password, _id),
        )
        print("User updated successfully")
        return True
    except Exception as error:
        print("Error updating a user from the database: ", error)
        return False
    

#DELETE
#metodo delete, para eliminar un usuario especifico de la tabla users

# ...

def delete(self, _id):
    try:
        self.db_manager.execute_query(
            "DELETE FROM lyfter_duad.users WHERE id = (%s)", (_id,)# NUNCA OLVIDAR EL WHERE, SI NO SE PONE, SE ELIMINAN TODOS LOS REGISTROS DE LA TABLA
        )
        print("User deleted successfully")
        return True
    except Exception as error:
        print("Error deleting a user from the database: ", error)
        return False
    
    
    
#################################################################################################
    #RESULTADO FINAL
    
class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "password": user_record[3],
        }

    def create(self, full_name, email, password):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_duad.users (full_name, email, password) VALUES (%s, %s, %s)",
                (full_name, email, password),
            )
            print("User inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, full_name, email, password FROM lyfter_duad.users;"
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, full_name, email, password FROM lyfter_duad.users WHERE id = %s;",
                (_id,),
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False

    def update(self, _id, full_name, email, password):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_duad.users SET (full_name, email, password) = (%s, %s, %s) WHERE ID = %s",
                (full_name, email, password, _id),
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False

    def delete(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_duad.users WHERE id = (%s)", (_id,)
            )
            print("User deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False
        

#MULTIPLES TABLAS
#tener multiples tablas en una base de datos,
# cada tabla debería de tener su propio repository.

#OJO
#un endpoint que necesite accesar o
#modificar varias tablas necesita instancear cada uno de los repositorios necesarios.

@app.route("/register", methods=["POST"])
def register():
    users_repo = UserRepository(db_manager)
    user_profiles_repo = UserProfileRepository(db_manager)
    addresses_repo = UserAddressRepository(db_manager)
    
    users_repo.create(**request["credentials"])
    user_profiles_repo.create(**request["profile"])
    addresses_repo.create(**request["address"])
    
    return "ok", 201


