#data.py

import csv
import os

students_data = "estudiantes.csv"

def export_csv(students):
    if not students:
        print("\nNo hay datos para exportar.")
        return
    with open(students_data, 'w', newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)
    print(f"\nDatos exportados exitosamente a '{students_data}'. ")

def import_csv(students):
    if not os.path.exists(students_data):
        print(f"\nNo se encontro el archivo '{students_data}'. Primero de exportar datos.")
        return
    with open(students_data, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        students.clear()
        for row in reader:
            row["Espanol"] = float(row["spanish"])
            row["Ingles"] =float(row["english"])
            row["Sociales"] = float(row["social_studies"])
            row["Ciencias"] = float(row["sciences"])
            row["Promedio"] = float(row["average_grade"])
            students.append(row)
    print(f"\nDatos importados desde '{students_data}'.")
    