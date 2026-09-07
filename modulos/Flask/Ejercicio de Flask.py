# Ejercicio de Flask: CRUD de Tareas con Persistencia en JSON

from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

data_file = "tasks.json"
valid_states = ["Por Hacer", "En Progreso", "Completada"]

#funciones adicionales para manejar el archivo JSON

def load_task():
    if os.path.exists(data_file): #dejar que el error se propague si el JSON no es valido, en lugar de retornar []
        with open(data_file, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_task(tasks):
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
        

#Endpont's para tareas

#GET /tasks?status=Por Hacer
@app.route("/tasks", methods=["GET"])
def get_tasks():
    status = request.args.get("status")## cambio de nombre clave query param
    tasks = load_task()
    if status:
        if status not in valid_states:
            return jsonify({"error": "Estado invalido. Los estados válidos son: Por Hacer, En Progreso, Completada."}), 400
        tasks = [task for task in tasks if task["status"] == status]
    return jsonify(tasks), 200 

#POST /tasks CREA
@app.route("/tasks", methods=["POST"])
def create_tasks():
    new_data = request.get_json() or {} # Si no se proporciona JSON, se asigna un diccionario vacío
    tasks = load_task()
    
#Validaciones para crear tareas

    if not new_data.get("id"):
        return jsonify({"error": "El identificador es obligatorio."}), 400
    if any(str(task["id"]) == str(new_data["id"]) for task in tasks):
        return jsonify({"error": "El identificador ya existe."}), 400
    if not new_data.get("title"):
        return jsonify({"error": "Debe incluir El título ."}), 400
    if not new_data.get("description"):
        return jsonify({"error": "Debe incluir la descripción."}), 400
    if not new_data.get("status"):
        return jsonify({"error": "Debe incluir el estado."}), 400
    if new_data["status"] not in valid_states:
        return jsonify({"error": "Estado invalido. Los estados válidos son: Por Hacer, En Progreso, Completada."}), 400


# se instancia un nuevo diccionario con los datos de la nueva tarea, y se agrega a la lista de tareas
    new_task = {
        "id": new_data["id"],
        "title": new_data["title"],## cambio de nombre de la clave
        "description": new_data["description"],
        "status": new_data["status"]
    }
    tasks.append(new_task)
    save_task(tasks)
    return jsonify(new_task), 201 # se retorna la nueva tarea creada con un código de estado 201 (Creado)

#PUT /tasks/<task_id> edita ya existente
@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    updated_data = request.get_json() or {} # Si no se proporciona JSON, se asigna un diccionario vacío
    tasks = load_task()
    
#Validaciones para actualizar tareas

    for task in tasks:
        if str(task["id"]) == str(task_id):
            if "title" in  updated_data:
                if not updated_data["title"]:
                    return jsonify({"error": "Debe incluir el título."}), 400
                task["title"] = updated_data["title"]
            if "description" in updated_data:
                if not updated_data["description"]:
                    return jsonify({"error": "Debe incluir la descripción."}), 400
                task["description"] = updated_data["description"]
            if "status" in updated_data:
                if updated_data["status"] not in valid_states:
                    return jsonify({"error": "Estado invalido.Estados válidos: Por Hacer, En Progreso, Completada."}), 400
                task["status"] = updated_data["status"]
                
            save_task(tasks)
            return jsonify(task), 200
        
    return jsonify({"error": "Tarea no encontrada."}), 404

#DELETE /tasks/<task_id> ELIMINA YA EXISTENTE
@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_task()
    new_tasks = [task for task in tasks if str(task["id"]) != str(task_id)] 
    if len(new_tasks) == len(tasks):
        return jsonify({"error": "Tarea no encontrada."}), 404
    
    save_task(new_tasks)
    return jsonify({"message": "Tarea eliminada exitosamente."}), 200

# MAIN
if __name__=="__main__":
    app.run(host="localhost", debug=True)


###################################################################################################################

    ##Crea un API con Flask de que permita un CRUD (Create, Read, Update, Delete) de tareas.
##Cada tarea debe tener:##Identificador##Título##Descripción##Estado (Por Hacer, En Progreso o Completada)
##El API debe tener endpoints para:##Obtener tareas.##Esta debe tener un query parameter opcional para filtrarlas por Estado.
##Crear tareas.
##Editar tareas.
##Eliminar tareas.
##Todos los datos deberán guardarse en un archivo JSON.
##Cada endpoint debe leer del archivo, y escribir en él (en caso de ser crear, editar o eliminar).
##Además, debe de validar que:
##No se puedan agregar tareas con identificadores ya existentes.
##No se puedan agregar tareas sin nombre.
##No se pueden agregar tareas sin descripción.
##No se puedan agregar tareas sin estado.
##No se puedan agregar tareas con un estado invalido.

########################################################################################################################
    
## puntos del archivo
## se usa task.json para persistencia de datos
##validadciones
## Endpoints para CRUD
##GET /tasks?status=Por Hacer
## POST /tasks CREA 
## PUT /tasks/<task_id> EDITA YA EXISTENTE
## Delete /tasks/<task_id> ELIMINA YA EXISTENTE


#######################################################################################################################
##cambios solicitados

#1. atribustos en ingles
#2. retorno del POST /tasks con status code 201
# create_task() retorna la nueva tarea creada con un código de estado 201 (Creado)
#3. manejo de errores en loadtask()
#eliminacion del bloque try except en load_task() para que el error se propague
# si el JSON no es válido, en lugar de retornar una lista vacía.


    