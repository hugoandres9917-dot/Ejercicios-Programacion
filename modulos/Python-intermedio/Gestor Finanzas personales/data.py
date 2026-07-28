
#modulo de persistencia. formato JSON..

import json
import os

# Archivo de datos

DATA_FILE = "archivodata.json"

#funcion para cargar datos desde archivo JSON

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                categories = data.get("categories", [])
                movements = data.get("movements", [])
                return categories, movements
        except (json.JSONDecodeError, FileNotFoundError):
            return [], []
    return [], []

#funcion para guardar datos lista de categorias y lista de movimientos dicionarios

def save_data(categories, movements):
    data = {
        "categories": categories,
        "movements": []
    }
    for m in movements:
                if isinstance(m, dict):
                    data["movements"].append(m)
                else:
                    data["movements"].append({                
                        "Titulo": m.title,
                        "Monto": m.amount,
                        "Categoria": m.category.name,
                        "Tipo": m.type,
                        "Fecha": m.date.strftime("%Y-%m-%d %H:%M:%S"),
                        "Metodo de Pago": m.payment_method,
                        "Notas": m.notes
            }) 
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")   