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

from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

data_file = "tasks.json"
valid_states = ["Por Hacer", "En Progreso", "Completada"]

#funciones adicionales para manejar el archivo JSON

def load_task():
    if os.path.exists(data_file):
        try:
            with open(data_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_task(tasks):
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
        

#Endpont's para tareas

#GET /tasks?estado=Por Hacer
@app.route("/tasks", methods=["GET"])
def get_tasks():
    state = request.args.get("estado")
    tasks = load_task()
    if state:
        if state not in valid_states:
            return jsonify({"error": "Estado invalido. Los estados válidos son: Por Hacer, En Progreso, Completada."}), 400
        tasks = [task for task in tasks if task["estado"] == state]
    return jsonify(tasks)

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
    if not new_data.get("titulo"):
        return jsonify({"error": "Debe incluir El título ."}), 400
    if not new_data.get("descripcion"):
        return jsonify({"error": "Debe incluir la descripción."}), 400
    if not new_data.get("estado"):
        return jsonify({"error": "Debe incluir el estado."}), 400
    if new_data["estado"] not in valid_states:
        return jsonify({"error": "Estado invalido. Los estados válidos son: Por Hacer, En Progreso, Completada."}), 400

    tasks.append({
        "id": new_data["id"],
        "titulo": new_data["titulo"],
        "descripcion": new_data["descripcion"],
        "estado": new_data["estado"]
    })
    save_task(tasks)
    return jsonify({"message": "Tarea creada exitosamente."}), 201

#PUT /tasks/<task_id> EDITA YA EXISTENTE
@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    updated_data = request.get_json() or {} # Si no se proporciona JSON, se asigna un diccionario vacío
    tasks = load_task()
    
#Validaciones para actualizar tareas

    for task in tasks:
        if str(task["id"]) == str(task_id):
            if "titulo" in  updated_data:
                if not updated_data["titulo"]:
                    return jsonify({"error": "Debe incluir el título."}), 400
                task["titulo"] = updated_data["titulo"]
            if "descripcion" in updated_data:
                if not updated_data["descripcion"]:
                    return jsonify({"error": "Debe incluir la descripción."}), 400
                task["descripcion"] = updated_data["descripcion"]
            if "estado" in updated_data:
                if updated_data["estado"] not in valid_states:
                    return jsonify({"error": "Estado invalido.Estados válidos: Por Hacer, En Progreso, Completada."}), 400
                task["estado"] = updated_data["estado"]
                
            save_task(tasks)
            return jsonify({"message": "Tarea actualizada exitosamente."}), 200
        
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
    
## puntos del archivo
## se usa task.json para persistencia de datos
##validadciones
## Endpoints para CRUD
##GET /tasks?estado=Por Hacer
## POST /tasks CREA 
## PUT /tasks/<task_id> EDITA YA EXISTENTE
## Delete /tasks/<task_id> ELIMINA YA EXISTENTE



    