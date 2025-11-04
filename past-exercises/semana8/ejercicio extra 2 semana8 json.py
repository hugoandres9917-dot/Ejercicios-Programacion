#Semana 8 JSON ejercicio extra 2
#busqueda po tipo de Pokemon 
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
    search_type = input("Ingrese el tipo de Pokemon que desea buscar: ").strip().title()
    maches = [p for p in pokemon_list if search_type in p.get("type", [])]

    if maches:
        print(f"\nPokemon de tipo '{search_type}':")
        for p in maches:
            name = p.get("name", {}). get('english', "Desconocido")
            print(f"- {name}")
    
    else:
        print(f"\n No se encontraron Pokemon de tipo")


def main():
        route= input("Ingrese la ruta del archivo JSON (por defecto: pokedex.json): ").strip()
        if not route:
            route = "pokedex.jason"

        pokemons = load_pokemon_jsonfile(route)
        if pokemons:
            show_pokemon_by_type(pokemons)
        else:
            print("no se pudo cargar la informacion de pokemon")

if __name__=="__main__":
    main()