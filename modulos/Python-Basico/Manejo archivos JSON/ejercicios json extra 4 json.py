#semana 8 ejercicios json extra 4
#Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
# Calcule y muestre el **promedio de nivel** para cada tipo:
#Cree un programa que abra un archivo .json con la información de Pokémon 
# ( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON
#Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
#Calcule y muestre el promedio de nivel para cada tipo:


import json
from collections import defaultdict


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
    

def group_and_average_by_type(pokemon_list):
    level_by_level = defaultdict(list)
    for poke in pokemon_list:
        level = poke.get("level")
        if not isinstance(level, (int, float)):#verifica que el nivel sea un numero, si no lo es, lo ignora y pasa al siguiente pokemon
            continue
        for poke_type in poke.get("type", []):
            level_by_level[poke_type.title()].append(level)#agrega el nivel del pokemon a la lista correspondiente a su tipo, usando title() para estandarizar el formato del tipo
    print("\n Promedio de nivel por tipo:\n")
    for type, levels in level_by_level.items():#itera sobre cada tipo y su lista de niveles
        average = sum(levels) /len(levels)#calcula el promedio sumando los niveles y dividiendo por la cantidad de niveles
        print(f" {type}: Nivel promedio = {average:.2f}")#:.2f para mostrar el promedio con 2 decimales


def main():
    route= input("Ingrese la ruta del archivo JSON (por defecto: pokedex.json): ").strip()
    if not route:
        route = "pokedex.json"

    pokemons = load_pokemon_jsonfile(route)
    if pokemons:
        group_and_average_by_type(pokemons)
    else:
        print("No se pudo cargar la informacion de pokemon")

if __name__=="__main__":
    main()