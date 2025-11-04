# ejercicio extra leer csv

import csv

def read_videogames_csv(file_name="videogames.csv"):
    try:
        with open(file_name, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)
            print("Lista de videojuegos registrados'\n'")
            for  row in reader:
                print(f"Nombre: {row[0]}")
                print(f"Genero: {row[1]}")
                print(f"Desarrollador: {row[2]}")
                print(f"Clasificacion ESRB: {row[3]}")
                print("-")
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no fue encotrado.")
    except Exception as e:
        print(f"Ocurrio un error al leer el archivo: {e}")

if __name__ == "__main__":
    read_videogames_csv()