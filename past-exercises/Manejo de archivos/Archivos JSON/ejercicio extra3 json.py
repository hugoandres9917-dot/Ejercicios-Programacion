#Semana 8 JSON EXTRA 3

# MOSTRAR LAS ESTADIDISTICAS DE CADA POKEMON
#Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON de Pokémon
#Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)

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
    for poke in pokemon_list:
        name = poke.get("name", {}).get("english", "Desconocido")
        base = poke.get("base", {})
        attack = base.get("attack", "N/A")
        defense = base.get("defense", "N/A")
        speed = base.get("speed", "N/A")

        print(f" {name}")
        print(f"   Ataque: {attack}")
        print(f"   Defensa: {defense}")
        print(f"   Velocidad: {speed}\n")
        
        
def main():
        route= input("Ingrese la ruta del archivo JSON (por defecto: pokedex.json): ").strip()
        if not route:
            route = "pokedex.json"

        pokemons = load_pokemo_jsonfile(route)
        if pokemons:
            show_statistics(pokemons)
        else:
            print("No se pudo cargar la informacion de pokemon ")

if __name__=="__main__":
    main()
