employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
# Diccionario para agrupar por departamento

employee_for_department = {}
# Recorrer la lista de empleados

for employee in employees:
     depart = employee['department']
     if depart not in employee_for_department:
        employee_for_department[depart] = []
        employee_for_department[depart].append(employee)

# Mostrar el resultado

for depart, list in employee_for_department.items():
       print(f"{depart}")
       for empl in list:
              print(f'-{empl["name"]} ({empl["email"]}')
              