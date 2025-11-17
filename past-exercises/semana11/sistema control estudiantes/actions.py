#Actions.py

from student import Student

def note_validation(message):
    while True:
        try:
            note = float(input(message))
            if 0 <= note <= 100:# valida cada nota ingresada que su valor se valido
                return note
            else:
                print("Nota invalida, debe estar entre 0 y 100.")
        except ValueError:
            print("entrada invalida. Debe ser un numero no datos")

def enter_students(students):
    try:
        n = int(input("Cuantos estudiantes desea ingresar? "))
        for i in range(n):
            print(f"\nEstudiantes #{i+1}")
            name = input("Nombre completo. ").strip()
            section = input("Seccion (ej. 11B): ").strip()
            spanish = note_validation("Nota de Espanol: ")
            english = note_validation("Nota de Ingles: ")
            social_studies = note_validation("Nota de Estudios sociales: ")
            sciences = note_validation("Nota de Ciencias: ")

            student = Student(name, section, spanish, english, social_studies, sciences)
            students.append(student)#agrega el estudiante y la informacion a la lista student
            print("Estudiante agregado.")
    except ValueError:
        print("Debe de ingresar un numero entero. ")

def show_students(students):
    if len(students) < 1:
        print("\nNo hay estudiantes registrados aun. ")
        return
    for student in students:
        print(student)

def show_top3_students(students):
    if len(students) < 1:
        print("\nNo hay estudiantes registrados. ")
        return
    top = sorted(students, key=lambda s: s.average_grade, reverse=True)[:3]
    print("\n --- top 3 Estudiantes ---")
    for i, student in enumerate(top, 1):
        print(f"{i}. {student.name} | Promedio: {student.average_grade}")

def show_general_average_students(students):
    if not students:
        print("\nNo hay estudiantes registrados. ")
        return
    total_average = sum(s.average_grade for s in students) / len(students)
    print(f"\nPromedio general de todos los estudiantes: {round(total_average, 2)}")
