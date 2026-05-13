
# semana 8 archivos csv con tsv

import csv


def add_videogame():
    try:
        name = input("ingrese el nombre del video juego: ")
        gender = input("ingrese el genero del video juego: ")
        developer = input('ingrese el nombre del Desarrollador: ')
        clasification = input("ingrese la Clasificacion ESRB: ")
        return {
            "Nombre": name,
            "Genero": gender,
            "Desarrollador": developer,
            "Clasificacion ESRB": clasification,
        }
    except Exception as e:
        print(f'Error al ingresar los datos solicitados, debe ser mas especifico: {e}')
        return None


def save_in_tsv(videogames_list, file_name ="videogames.tsv"):
    try:
        with open(file_name, 'w', newline='', encoding= 'utf-8') as tsv_file:
            filenames = ['Nombre','Genero','Desarrollador','Clasificacion ESRB']
            writer_csv = csv.DictWriter(tsv_file, fieldnames=filenames, delimiter='\t')
            writer_csv.writeheader()
            writer_csv.writerows(videogames_list)
        print(f"datos guardados en el archivo '{file_name}'")
    except Exception as e:
        print(f"No fue posible guardar su archivo TSV: {e}")

if __name__ == "__main__":
    videogames = []
    try:
        while True:
            respond = input("Desea agregar un nuevo videojuego? (yes/no): ")
            if respond == 'yes':
                video_game= add_videogame()
                if video_game is not None:
                    videogames.append(video_game)
                else:
                    print("No se agregaron registros. Error en los datos")
            elif respond == 'no':
                break
            else:
                print("Entrada no valida. debe usar 'yes' o 'no'.")
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")

    videogames = [v for v in videogames if v is not None]
    if videogames:
        save_in_tsv(videogames)
        print("Finalizo el registro de videojuegos.")
    else:
        print("No ha ingresado ninguna infomacion para guardar.")
