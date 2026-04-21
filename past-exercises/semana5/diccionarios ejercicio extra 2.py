employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
# Diccionario para agrupar por departamento

dept_employees = {}
# Recorrer la lista de empleados

for employee in employees:
    depart = employee['department']
    if depart not in dept_employees:
        dept_employees[depart] = []
    dept_employees[depart].append(employee)

# Mostrar el resultado

for depart, list in dept_employees.items():
    print(f"{depart}")
    for empl in list:
        print(f'-{empl["name"]} ({empl["email"]})')