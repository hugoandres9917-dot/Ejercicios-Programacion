#Construcción del API

from pickle import GET

from flask import Flask


app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
    
    
##Paths / Endpoints

from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Hello, World!</h1>"
    
if __name__ == "__main__":
    app.run(host="localhost", debug=True)
    
    #agregar una ruta

@app.route("/information")
def information():
	return {
		"year": 2024,
		"description": "Esto es un endpoint secundario",
	}
 
##solicitudes en HTTP - Métodos (requests).

from flask import request


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()
    
##El objeto Request
##Al crear APIs, lo que principal 
# que hacemos es recaudar datos de la solicitud HTTP y
# utilizarlos para realizar nuestra lógica de negocio.

##l objeto request es fundamental para esto, ya que es el “paquete” 
# en donde vienen todos los datos de la solicitud hecha por el
# cliente que accese a cada endpoint.



##Parameters
##Path Parameters
@app.route("/user/<username>")
def profile(username):
	return f"{username}\'s profile"

##multiples path parameters

@app.route("/shop/<category>/<subcategory>/all")
def products_subcategory(category, subcategory):
    return f"Shopping category {category}, {subcategory}"

##Query Parameters
##(como vimos en HTTP - Query Parameters) Se obtienen del atributo args del objeto request.

from flask import request


shows_list = [
    {
        "title": "3 Body Problem",
        "genre": "Sci-Fi",
    },
    {
        "title": "Severance",
        "genre": "Thriller",
    },
    {
        "title": "Black Knight",
        "genre": "Sci-Fi",
    },
]


@app.route("/shows")
def shows():
    filtered_shows = shows_list
    genre_filter = request.args.get("genre")
    if genre_filter:
        filtered_shows = list(
            filter(lambda show: show["genre"] == genre_filter, filtered_shows)
        )

    return {"data": filtered_shows}

##Body (como vimos en HTTP - Body)atributo json o data del objeto request.

from flask import request


@app.route("/echo", methods=["POST"])
def echo():
    request_body = request.json
    return {"request_body": request_body}

#fORMS atributo form del objeto request

from flask import request, jsonify


comments_list = [
    "Genial video, entendí todo a la perfeccion!",
    "Me encantó el intro jajaja",
]


@app.route("/comment", methods=["POST"])
def post_comment():
    comment_content = request.form.get("comment_content")
    if not comment_content:
        return jsonify(message="no empty comments allowed"), 400

    comments_list.append(comment_content)
    return comments_list


##Validaciones onstruir endpoint que escriban datos 
#(con métodos como POST, PUT o PATCH) son las validaciones de estos datos en el request.

from flask import request, jsonify


users_list = [
	{
		"email": "action.bronson@gmail.com",
		"password": "123@a!",
	},
]


@app.route("/register", methods=["POST"])
def register_user():
    try:
        if "email" not in request.json:
            raise ValueError("email missing from the body")

        if "password" not in request.json:
            raise ValueError("password missing from the body")

        users_list.append(
            {
                "email": request.json["email"],
                "password": request.json["password"],
            }
        )
        return users_list
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
		    # enviar un mensaje por slack
        return jsonify(message=str(ex)), 500


#Headers útiles cuando necesitamos información extra del request
##atributo headers del objeto request.formato de diccionario, 
# así que se puede usar el método get de los diccionarios para obtener uno en específico.


from flask import request


@app.route('/view-token')
def view_token():
	token = request.headers.get('token', '')
	return token

##El objeto Response
##Equivalente al objeto request - 
##la clase Response nos permite crear el paquete de datos que se enviará como 
# respuesta al request que el cliente envió al API.
#datos primitivos de Python

@app.route("/hello")
def hello():
    return {"msg": "Hello World!"}, 200


##necesitamos usar clase Response manualmente si 
# necesitamos enviar respuestas más con información extra o headers específicos.

import json
from flask import Response


@app.route("/hello")
def hello():
    response_body = json.dumps({"msg": "Hello World!"})
    return Response(response_body, status=200, mimetype="application/json")


##sar la función jsonify

from flask import jsonify
from dataclasses import dataclass


@dataclass
class HelloResponse:
    msg: str


@app.route("/hello")
def hello():
    response = HelloResponse("Hello World!")
    return jsonify(response), 200

##Status Codes
##usamos la clase Response, podemos pasarlo como parámetro status de la misma


import json
from flask import Response


@app.route("/hello")
def hello():
    response_body = json.dumps({"msg": "Hello World!"})
    return Response(response_body, status=200, mimetype="application/json")

##Si hacemos return de datos primitivos o jsonify, podemos pasarlo al lado de 
# dichos datos separado por una coma (enviando así una tupla de (datos, status_code)):

@app.route('/hello')
def hello():
	return {"msg":"Hello World!"}, 200

##Manejo de errores
# La mejor práctica para esto es envolver toda la lógica
# de nuestros endpoints en un gran try - except.
# Un problema esperado sería que el cliente no envié un dato requerido en el request.
#En este caso, debemos retornar un status code: 400.
#Un problema inesperado sería que nuestro código que no valide cuando un usuario 
# se registre con un correo ya existente.
#En este caso, debemos retornar un status code: 500.


##la función abort Esta toma como parámetro 
# el código HTTP del error, y retorna un Response detrás de cámaras.


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
    
    
#Tambien podemos agregarle un body como parámetro 
# para especificar cual fue el error en concreto.


def throw_error(message, code):
    return abort(code, {"error" : message})


@app.route('/login')
def login():
		return throw_error("Missing parameters", 401)

 #  Para probar tu API de tareas en Postman,
  # asegúrate primero de que tu servidor Flask
  # esté ejecutándose en tu terminal (python app.py o python main.py).
  #Tu API estará escuchando por defecto en http://localhost:5000.

1. Obtener todas las tareas (GET)
Método: GET
URL: http://localhost:5000/tasks
Query Params (opcional):
Para filtrar por estado, ve a la pestaña Params e ingresa:
KEY: estado
VALUE: Por Hacer (o En Progreso / Completada)

2. Crear una nueva tarea (POST)
Método: POST
URL: http://localhost:5000/tasks
Pestaña Body:
Selecciona body.
Elige la opción raw.
En el menú desplegable de la derecha (donde dice Text), cambia a JSON.
JSON de ejemplo:
JSON
{
  "id": "1",
  "titulo": "Estudiar Flask",
  "descripcion": "Revisar los endpoints y validaciones de la tarea",
  "estado": "Por Hacer"
}
3. Actualizar una tarea (PUT)
Método: PUT

URL: http://localhost:5000/tasks/1 (donde 1 es el id de la tarea)

Pestaña Body: Selecciona raw -> JSON.

JSON de ejemplo:

JSON
{
  "titulo": "Estudiar Flask y Postman",
  "estado": "En Progreso"
}
4. Eliminar una tarea (DELETE)
Método: DELETE

URL: http://localhost:5000/tasks/1 (donde 1 es el id de la tarea)

Body: No requiere cuerpo de datos.