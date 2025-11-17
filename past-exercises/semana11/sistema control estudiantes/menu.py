#menu.py

from actions import(
    enter_students,
    show_students, 
    show_top3_students,
    show_general_average_students

)
from data import export_csv, import_csv

def show_menu(students):
    while True:
        print("\n--- Menu Principal ---")
        print("1. Ingresar informacion de estudiantes")
        print("2. Ver informacion de todos los estudiantes")
        print("3. Top 3 mejores promedios de todos los estudiantes")
        print("4. Promedio general de todos los estudiantes")
        print("5. Exportar todos los datos a un archivo CSV")
        print("6. Importar datos desde un archivo CSV")
        print("0. SALIR")

        option = input("Seleccione una opcion:  ")

        if option == "1":
            enter_students(students)
        elif option == "2":
            show_students(students)
        elif option == "3":
            show_top3_students(students)
        elif option == "4":
            show_general_average_students(students)
        elif option == "5":
            export_csv(students)
        elif option == "6":
            import_csv(students) 
        elif option == "0":
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalidad. Vuelva a intentar")
            
        