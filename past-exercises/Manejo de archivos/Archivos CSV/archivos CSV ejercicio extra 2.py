# archivos csv ejercicio extra 2 
# leer y organizar por clasificacion o cualquier otra opcion

import csv

def filter_by_class(file_name="videogames.csv"):
    try:
        with open(file_name, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                found = False
                print(f"\n Video juegos con Clasificacion ESRB '{esrb_input}':\n")
                for row in reader:
                    if row["clasification"].strip().upper() == esrb_input:
                        print(f"Nombre: {row['name']}")
                        print(f"Genero: {row['gender']}")
                        print(f"Desarrollador: {row['developer']}")
                        print(f"Clasificacion ESRB: {row['clasification']}")
                        print("-")
                        found = True
                if not found:
                    print("No se encontraron video juegos con esa clasificacion.")
    except FileNotFoundError:
        print(f"No se encotraron videojuegos con esa clasficicacion")
    except Exception as e:
        print(f'Ocurrio un error al procesar el archivo: {e}')
        
def main():
    esrb_input = input("ingrese la clasificicacion ESRB que desea buscar (ejemplo: E, T, M):").strip().upper()
    filter_by_class(esrb_input)

if __name__ == "__main__":
    main()
    
    