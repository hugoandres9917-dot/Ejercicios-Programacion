#semana 8 ejercicios JSON
#LA POKEDEX

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

    types = input("Tipo o tipos, separados por comas(ej. fuego, volador)").strip().split(",")

    try:
        base = {
            "HP": int(input("HP: ")),
            "Ataque": int(input("Ataque: ")),
            "Defensa": int(input("Defensa: ")),
            "Ataque Sp.": int(input("Ataque Sp: ")),
            "Defensa Sp.": int(input("Defensa Sp:")),
            "Velocidad": int(input("Velocidad: "))
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
    pokemons = load_pokemon_data()
    new_pokemon = add_new_pokemon()

    if new_pokemon:
        pokemons.append(new_pokemon)
        save_pokemon_data(pokemons)
    else:
        print("No fue posible agregar el Pokemon a la pokedex")
        