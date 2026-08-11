
# Manejos de archivos

def read_songs(songs):

    songss = []
    try:
        with open(songs, 'r', encoding='utf-8') as file_entry:
            for line in file_entry:
                songss.append(line.strip())# .strip() para eliminar espacios en blanco
    except FileNotFoundError:
        print(f"El archivo con el nombre '{songs}' no fue encontrado")
    except Exception as e:
        print(f"Error al leer el archivo {e}")
        return songss

def write_songs(songs_ordered, songss):
    try:
        with open(songs_ordered,'w',encoding='utf-8') as file_out:
            for song in songss:
                file_out.write(song + '\n')# cada canción se escribe en una nueva línea con \n
        print(f"Las canciones se han organizado alfabeticamente y guardadas en  '{songs_ordered}'.")
    except Exception as e:
        print(f'ha ocurrido un error al escribir el archivo saliente {e}')

def main():
    songs_entry_names = "songs.txt"
    songs_ordered_out_names = "SONGS_ORDERED.txt"
    
    new_list = read_songs(songs_entry_names)
    if new_list:
        new_list.sort()
        write_songs(songs_ordered_out_names, new_list)
        
if __name__ == "__main__":
    main()
    