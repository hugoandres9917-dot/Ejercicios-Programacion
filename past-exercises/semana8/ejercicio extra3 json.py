#Semana 8 JSON EXTRA 3

# MOSTRAR LAS ESTADIDISTICAS DE CADA POKEMON

import json

def load_pokemo_jsonfile(file_name="pokedex.json"):
    try:
        with open (file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no fue encontrado.")
        return[]
    except json.JSONDecodeError:
        print("Error: el archivo no tiene un formato JSON valido.")
        return[]
def show_statistics(pokemon_list):
    print("\nEstadísticas principales de cada Pokémon:\n")
    for p in pokemon_list:
        name = p.get("name", {}).get("english", "Desconocido")
        base = p.get("base", {})
        atack = base.get("Ataque", "N/A")
        defen = base.get("Defensa", "N/A")
        speed = base.get("Velocidad", "N/A")

        print(f" {name}")
        print(f"   Ataque: {atack}")
        print(f"   Defensa: {defen}")
        print(f"   Velocidad: {speed}\n")
def main():
        route= input("Ingrese la ruta del archivo JSON (por defecto: pokedex.json): ").strip()
        if not route:
            route = "pokedex.jason"

        pokemons = load_pokemo_jsonfile(route)
        if pokemons:
            show_statistics(pokemons)
        else:
            print("no se pudo cargar la informacion de pokemon")

if __name__=="__main__":
    main()
