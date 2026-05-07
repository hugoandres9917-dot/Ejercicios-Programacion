#semana 8 ejercicios JSON EXTRA 1
# RECORRER , LEER,Y MOSTRAR LISTA DE POKEMONES EN ARCHIVO

#Cree un programa que abra un archivo .json con la información de Pokémon
#( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON de Pokémon
#Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel 
#(o cualquier otro atributo definido)

# separar logica en funciones
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

def show_pokemons(file_name="pokedex.json"):
    pokemons = load_pokemon_jsonfile(file_name)
    for pokemon in pokemons:
        try:
            name = pokemon["name"]["english"]
            types = ", ".join(pokemon["type"])
            hp = pokemon["base"]["hp"]
            print(f"- {name} | Tipo: {types} | HP: {hp} -\n")
        except Exception as e:
            print(f"Error al mostrar un Pokémon: {e}")

        print("\nLista Pokémon:\n")
        for pokemon in pokemons:
            try:
                name = pokemon["name"]["english"]
                types = ", ".join(pokemon["type"])
                hp = pokemon["base"]["hp"]
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

