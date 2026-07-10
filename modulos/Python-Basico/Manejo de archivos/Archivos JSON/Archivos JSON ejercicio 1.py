#semana 8 ejercicios JSON
#LA POKEDEX

#Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON 
# (ipsum:lesson/python-bsico/manejo-de-json)
#Debe leer el archivo para importar los Pokémones existentes.
#Luego debe pedir la información del Pokémon a agregar.
#Finalmente debe guardar el nuevo Pokémon en el archivo.
#
import json

def load_pokemon_data(file_name="pokedex.json"):
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Archivo '{file_name}' no encontrado. se creara un archivo nuevo.")
        return[]
    except json.JSONDecodeError:
        print("Error formato JSON invalido. ")
        return[]
    

def save_pokemon_data(pokemon_list, file_name="pokedex.json"):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(pokemon_list, file, indent=4, ensure_ascii=False)
            print(f"El Pokemon fue registrado en la: '{file_name}'. ")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


def add_new_pokemon():
    print("Ingrese los datos del nuevo Pokemon: ")
    name = input("Nombre: ").strip().title()
    if not name:
        print("El nombre no puede estar vacío.")
        return None

    types = [t.strip().title() for t in input("Tipo o tipos, separados por comas(ej. fuego, volador)").split(",") if t.strip()]
    if not types:
        print("Debe ingresar al menos un tipo.")
        return None
    try:
        base = {
            "hp": int(input("HP: ")),
            "attack": int(input("Ataque: ")),
            "defense": int(input("Defensa: ")),
            "attack_spc": int(input("Ataque Sp: ")),
            "defense_spc": int(input("Defensa Sp:")),
            "speed": int(input("Velocidad: "))
        }
    except ValueError:
        print("Los valores deben ser numeros enteros.")
        return None

    return{
        "name": {"english": name},
        "type": [t.strip().title() for t in types if t.strip()],
        "base": base
    }
if __name__ == "__main__":
    file_name = input("Ingrese el nombre del archivo JSON para la pokedex (ej. pokedex.json): ").strip()
    file_name = file_name if file_name else "pokedex.json"
    pokemons = load_pokemon_data(file_name)
    new_pokemon = add_new_pokemon()

    if new_pokemon:
        pokemons.append(new_pokemon)
        save_pokemon_data(pokemons, file_name)
    else:
        print("No fue posible agregar el Pokemon a la pokedex")
        