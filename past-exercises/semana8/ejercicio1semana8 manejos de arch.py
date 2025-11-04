#semana 8 ejercicio de manejos de archivos
# pasar lista de canciones de un archivo a otro ordenadas
def organizing_songs(Songs, Songs_Ordered):

    new_list_songs = []
    try:
        with open(Songs, 'r') as file_entry:
            for line in file_entry:
                new_list_songs.append(line.strip())
    except FileNotFoundError:
        print(f"El archivo con el nombre '{Songs}' no fue encontrado")
    except Exception as e:
        print(f"Error al leer el archivo {e}")
        return
    
    new_list_songs.sort()

    try:
        with open(Songs_Ordered,'w',encoding='utf-8') as file_out:
            for song in new_list_songs:
                file_out.write(song + '\n')
        print(f"Las canciones se han orgaizado alfabeticamente y guardadas en  '{Songs_Ordered}'.")
    except Exception as e:
        print(f'ha ocurrido un error al escribir el archivo saliente {e}')


songs_entry_names = "Songs.txt"
songs_ordered_out_names = "SONGS_ORDERED.txt"

organizing_songs(songs_entry_names, songs_ordered_out_names)


