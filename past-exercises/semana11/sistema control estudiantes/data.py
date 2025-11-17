#data

import csv
import os
from student import Student

students_data = "estudiantes.csv"

def export_csv(students):
    if not students:
        print("\nNo hay datos para exportar. ")
        return
    with open(students_data, 'w', newline="", encoding="utf-8") as file:
        fieldnames = ['name', 'section', 'spanish', 'english', 'social_studies', 'sciences', 'average_grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student.to_dictionary())
    print(f"\nDatos exportados exitosamente a '{students_data}'.")

def import_csv(students):
    if not os.path.exists(students_data):
        print(f"\nNo se encontro el archivo '{students_data}'. Primero exporte los datos.")
        return
    with open(students_data, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        students.clear()
        for row in reader:
            try:
                student = Student(
                name=row['name'],
                section=row['section'],
                spanish=float(row['spanish'].strip()),
                english=float(row['english'].strip()),
                social_studies=float(row['social_studies'].strip()),
                sciences=float(row['sciences'].strip())
                )
                students.append(student)
            except ValueError as e:
                print(f"Error al importar estudiante: {row['name']}. verifica que las notas sean numericas.")

    print(f"\nDatos importados desde '{students_data}'.")    