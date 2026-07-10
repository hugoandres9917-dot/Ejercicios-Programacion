#Semana 8 JSON ejercicio extra 2
#busqueda po tipo de Pokemon 

#Cree un programa que abra un archivo .json con la información de Pokémon 
#( en base al JSON que fue generado en el ejercicio 1) y::
#Lea el archivo JSON de Pokémon
#Pida al usuario un tipo de Pokémon
#Muestre todos los Pokémon que sean de ese tipo
#

import json

def load_pokemon_jsonfile(file_name="pokedex.json"):
    try:
        with open (file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no fue encontrado.")
        return[]
    except json.JSONDecodeError:
        print("Error: el archivo no tiene un formato JSON valido.")
        return[]

def show_pokemon_by_type(pokemon_list):
    search_type = input("Ingrese el tipo de Pokemon que desea buscar: ").strip().title()#.title() para convertir la primera letra en mayuscula y el resto en minuscula
    matches = [poke for poke in pokemon_list if search_type in poke.get("type", [])]#busca en la lista de pokemon aquellos que tengan el tipo buscado, usando get para evitar errores si no existe la clave "type" y devolviendo una lista vacia en ese caso

    if matches:
        print(f"\nPokemon de tipo '{search_type}':")
        for poke in matches:
            name = poke.get("name", {}).get("english", "Nombre desconocido")#busca el nombre en ingles del pokemon, usando get para evitar errores si no existe la clave "name" o "english" y devolviendo un mensaje por defecto en ese caso
            print(f"- {name}")
    
    else:
        print(f"\n No se encontraron Pokemon de tipo '{search_type}'.")


def main():
        route= input("Ingrese la ruta del archivo JSON (por defecto: pokedex.json): ").strip()
        if not route:
            route = "pokedex.json"

        pokemons = load_pokemon_jsonfile(route)
        if pokemons:
            show_pokemon_by_type(pokemons)
        else:
            print("No se pudo cargar la informacion de pokemon")

if __name__=="__main__":
    main()