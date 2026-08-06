
#modulo de persistencia. formato JSON..

import json
import os
from logica import Movement, Category

# Archivo de datos

DATA_FILE = "archivodata.json"

#funcion para cargar datos desde archivo JSON
def load_data(file_path: str = DATA_FILE):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                categories = data.get("categories", [])
                movements_dicts = data.get("movements", [])
                movements = []
                for md in movements_dicts:
                    try:
                        category_name = md.get("Categoria")
                        if category_name not in categories:
                            continue  # Ignorar movimientos con categorías no válidas
                        category = Category(category_name)
                        movement = Movement(
                            title=md.get("Titulo", ""),
                            amount=float(md.get("Monto", 0)),
                            category=category,
                            is_income=(md.get("Tipo") == "Ingreso"),
                            payment_method=md.get("Metodo de Pago", "Efectivo"),
                            notes=md.get("Notas", ""),
                            date=md.get("Fecha")
                        )
                        if "Id" in md:
                            movement.id = md["Id"]
                        movements.append(movement)
                    except ValueError:
                        continue  # Ignorar movimientos con datos no válidos   
                return categories, movements
        except (json.JSONDecodeError, FileNotFoundError):
            return [], []
    return [], []   

#funcion para guardar datos lista de categorias y lista de movimientos dicionarios
def save_data(categories, movements, file_path: str = DATA_FILE):
    data = {
        "categories": categories,
        "movements": []
    }
    for m in movements:
        data["movements"].append({
            "Id": m.id, #  identifivador unico del movimiento
            "Titulo": m.title,
            "Monto": m.amount,
            "Categoria": m.category.name,
            "Tipo": m.type,
            "Fecha": m.date.strftime("%Y-%m-%d %H:%M:%S"),
            "Metodo de Pago": m.payment_method,
            "Notas": m.notes
            }) 
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")   