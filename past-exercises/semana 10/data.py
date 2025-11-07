#data.py

import csv
import os

file = "estudiantes.csv"

def export_csv(students):
    if not students:
        print("No hay datos para exportar.")
        return
    with open(file, 'w', newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=students[0].key())
        writer.writeheader()
        writer.writerows(students)
    print(f"Datos exportados exitosamente a '{file}'. ")

def import_csv(students):
    if not os.path.exists(file):
        print(f"No se encontro el archivo '{file}'. Primero de exportar datos.")
        return
    with open(file, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        students.clear()
        for row in reader:
            row["Espanol"] = float(row["Epanol"])
            row["Ingles"] =float(row["Ingles"])
            row["Sociales"] = float(row["Sociales"])
            row["Ciencias"] = float(row["Ciencias"])
            row["Promedio"] = float(row["Promedio"])
            students.append(row)
    print(f"Datos importados desde '{file}'.")
    