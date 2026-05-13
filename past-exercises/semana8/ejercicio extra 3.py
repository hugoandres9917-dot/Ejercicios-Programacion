#semana 8 ejercicio extra 3

import csv

def filter_by_developer(file_name="videogames.csv"):
    try:
        developer_input = input("ingrese el nombre del desarrollador que desea buscar: ").strip().lower()

        with open(file_name, 'r', encoding='utf-8') as csv_file:     
            reader = csv.DictReader(csv_file)
            found_games = []
            for row  in reader:
                if row["Desarrollador"].strip().lower() == developer_input:
                    found_games.append(row)
        if found_games:
            print(f"\n Video juegos desarrollados por {developer_input.title()}:\n")
            for game in found_games:
                name = game["Nombre"]
                clasification = game["Clasificacion ESRB"]
                gender = ["Genero"]
                print(f"- {name} (Clasificacion: {clasification}, Genero; {gender})")
        else:
            print("No se encontraron videojuegos para ese desarrollador.")
    except FileNotFoundError:
        print(f"El archivo '{game}' no pudo ser encontrado.")        
    except Exception as e:
        print(f"Ocurrio un error al procesar el archivo: {e}")

if __name__=="__main__":
    filter_by_developer()
