
#Modulo de lógica  gestor financiero personal.
#valida todas las entradas y procesa datos.

#validar nombre de categoria

def validate_category(name):
    name = name.strip()
    if not name:
        return False, "Debe ingresar un nombre válido"
    return True, name

#agregar nueva categoria si no existe

def add_category(categories, name):
    valid, message = validate_category(name)
    if not valid:
        return False, message
    
    if name in categories:
        return False, "La categoría ya existe"
    
    categories.append(name)
    return True, "Categoría agregada exitosamente"
#validar datos de movimientos
def validate_movement(amount_str, category):
    try:
        amount = float(amount_str)
        if amount <= 0:
            return False, None, None, "El monto debe ser mayor que cero"
    except ValueError:
        return False, None, None, "El monto debe ser un número válido"
    
    if not category:
        return False, None, None, "Debe seleccionar una categoría"

    return True, amount, category, None

#crear diccionario de movimiento

def create_movement(amount, category, is_income):
    movement_type = "Ingreso" if is_income else "Gasto"
    return {
        "Monto": amount,
        "Categoria": category,
        "Tipo": movement_type
    }

#convertir movimiento a formato de fila para tabla

def convert_movement_to_row(movement):
    return [movement["Monto"], movement["Categoria"], movement["Tipo"]]