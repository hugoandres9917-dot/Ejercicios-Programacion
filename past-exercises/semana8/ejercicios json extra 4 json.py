#semana 8 ejercicios json extra 4
#Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
# Calcule y muestre el **promedio de nivel** para cada tipo:

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
    for p in pokemon_list:
        level = p.get("level")
        if not isinstance(level, (int, float)):
            continue
        for type in p.get("type", []):
            level_by_level[type.title()].append(level)
    print("\n Promedio de nivel por tipo:\n")
    for type, levels in level_by_level.items():
        average = sum(levels) /len(levels)
        print(f" {type}: Nivel promedio = {average:.2f}")


def main():
    route= input("Ingrese la ruta del archivo JSON (por defecto: pokedex.json): ").strip()
    if not route:
        route = "pokedex.json"

    pokemons = load_pokemon_jsonfile(route)
    if pokemons:
        group_and_average_by_type(pokemons)
    else:
        print("no se pudo cargar la informacion de pokemon")

if __name__=="__main__":
    main()