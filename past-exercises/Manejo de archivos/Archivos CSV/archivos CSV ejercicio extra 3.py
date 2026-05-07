#archivos csv ejercicio extra 3

#Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
#Lea el archivo .csv con videojuegos
#Cuente cuántos videojuegos hay de cada género
#Muestre el resultado de forma ordenada

#Conteo por género no fue entregado
#El archivo del ejercicio 3 contiene la lógica del ejercicio 4 (búsqueda por desarrollador) en lugar del conteo por género. Lo que se necesita en ese ejercicio es leer el CSV, recorrer todos los registros y llevar la cuenta de cuántos videojuegos pertenecen a cada género, para luego mostrar el resultado ordenado. Una forma de hacerlo es usando un diccionario donde cada clave sea un género y el valor sea el contador de videojuegos de ese género.
#2. Bug en el archivo del ejercicio 3 – Acceso incorrecto al diccionario
#Además del punto anterior, hay una línea con un error que produciría un resultado incorrecto: gender = ["Genero"] crea una lista con el texto literal "Genero" en lugar de leer el valor del diccionario. La forma correcta de acceder al género de un registro es game["Genero"], igual a como se accede a los otros campos en ese mismo bloque.

import csv

def count_by_genre(file_name="videogames.csv"):
    try:
        genre_count = {}
        with open(file_name, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                genre = row["genre"].strip()
                genre_count[genre] = genre_count.get(genre, 0) + 1
        print("Conteo de videojuegos por género:")
        for genre, count in sorted(genre_count.items(), key=lambda item: item[1], reverse=True):
            print(f"- {genre}: {count}")
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no pudo ser encontrado.")
    except Exception as e:
        print(f"Ocurrio un error al procesar el archivo: {e}")

if __name__ == "__main__":
    count_by_genre()
    
    