# ejercicio extra leer csv

#1. Cree un programa que abra un archivo `.csv` con la información de videojuegos
# (el que fue generado en el ejercicio 1) y:
#- Lea cada línea usando `csv.reader()`
#- Muestre el contenido en pantalla de forma legible, línea por línea


import csv

def read_videogames_csv(file_name="videogames.csv"):
    try:
        with open(file_name, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)
            print("Encabezados del archivo CSV:", headers)
            print("Lista de videojuegos registrados:'\n'")
            for  row in reader:
                if len(row) >= 4:
                    print(f"Nombre: {row[0]}")
                    print(f"Genero: {row[1]}")
                    print(f"Desarrollador: {row[2]}")
                    print(f"Clasificacion ESRB: {row[3]}")
                    print("-")
                else:
                    print("Fila incompleta encontrada", row)
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no fue encotrado.")
    except Exception as e:
        print(f"Ocurrio un error al leer el archivo: {e}")

if __name__ == "__main__":
    read_videogames_csv()