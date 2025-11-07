#Actions.py

def note_validation(message):
    while True:
        try:
            note = float(input(message))
            if 0 <= note <= 100:
                return note
            else:
                print("Nota invalida, debe estar entre 0 y 100.")
        except ValueError:
            print("entrada invalida. Debe ser un numero no datos")

def enter_students(students):
    try:
        n = int(input("Cuantos estudiantes desea ingresar"))
        for i in range(n):
            print(f"\nEstudiantes #{i+1}")
            name = input("Nombre completo").strip()
            section = input("Seccion (ej. 11B): ").strip()
            spanish = note_validation("Nota de Espanol: ")
            english = note_validation("Nota de Ingles: ")
            social_studies = note_validation("Nota de Estudios sociales: ")
            sciences = note_validation("Nota de Ciencias: ")

            student = {
                "Nombre": name,
                "Seccion": section,
                "Espanol": spanish,
                "Ingles": english,
                "Sociales": social_studies,
                "Ciencias": sciences,
                "Promedio": round((spanish + english + social_studies + sciences)/4, 2)
            }
            students.append(student)
            print("Estudiante agregado.")
    except ValueError:
        print("Debe de ingresar un numero entero. ")

def show_students(students):
    if not students:
        print("No hay estudiantes registrados aun. ")
    
    for est in students:
        print("\nNombre: {stud ['name']}")
        print(f"Seccion: {est['section']}")
        print(f"Notas - Espanol: {est['spanish']}, Ingles: {est['englis']}, Sociales: {est['social_studies']}, Ciencias: {est['sciences']}")
        print(f"Promedio: {est['promedio']}")

def show_top3_students(students):
    if len(students) < 1:
        print("No hay estudiantes registrados. ")
        return
    top = sorted(students, key=lambda x: x ['Promedio'], reverse=True)[:3]
    print("\n --- top 3 Estudiantes ---")
    for i, est in enumerate(top, 1):
        print(F"{i}. {est['Nombre']} | Promedio: {est['promedio']}")

def show_general_average_students(students):
    if not students:
        print("No hay estudiantes registrados. ")
        return
    total_average = sum(est["Promedio"] for est in students) / len(students)
    print(f"\nPromedio general de todos los estudiantes: {round(total_average, 2)}")
