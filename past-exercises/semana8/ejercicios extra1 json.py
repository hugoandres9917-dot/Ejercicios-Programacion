#semana 8 ejercicios JSON EXTRA 1
# RECORRER , LEER,Y MOSTRAR LISTA DE POKEMONES EN ARCHIVO
import json

def show_pokemons(file_name="pokedex.json"):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            pokemons = json.load(file)

        print("\nLista Pokémon:\n")
        for pokemon in pokemons:
            try:
                name = pokemon["name"]["english"]
                types = ", ".join(pokemon["type"])
                hp = pokemon["base"]["HP"]
                print(f"- {name} | Tipo: {types} | HP: {hp} -\n")
            except Exception as e:
                print(f"Error al mostrar un Pokémon: {e}")
    except FileNotFoundError:
        print(f" El archivo '{file_name}' no fue encontrado.")
    except json.JSONDecodeError:
        print("Error en el formato del archivo JSON.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    show_pokemons()

