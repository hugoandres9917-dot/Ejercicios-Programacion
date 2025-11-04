#semana 8 ejercicio extra 4

import csv

def games_by_developer(file_name="videogames.csv"):
    try:
        developer = input("Ingrese el nombre del Desarrollador (e.g. 'Ubisoft'): ").strip().lower()
        found_games = []

        with open(file_name, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row["Desarrollador"].strip().lower() == developer:
                    found_games.append(row)

        if found_games:
            print(f"\n🎮 Video juego Desarrollado por: {developer.title()}:\n")
            for game in found_games:
                name = game["Nombre"]
                clasification = game["Clasificacion ESRB"]
                genre = game["Genero"]
                print(f"- {name} (clasificacion: {clasification}, Genero: {genre})")
        else:
            print(f"Desarrollador de videojuegos no encontrado '{developer.title()}'.")
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no fue encotrado.")
    except Exception as e:
        print(f"Error no fue posible leer el archivo: {e}")

if __name__ == "__main__":
    games_by_developer()