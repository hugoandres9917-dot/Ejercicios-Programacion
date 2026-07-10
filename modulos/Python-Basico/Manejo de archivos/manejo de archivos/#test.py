#
def read_file(input_file):
    try:
        lines = [] # lista vacia para almacenar las lineas del archivo
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())# elimna saltos y spacios extra
    
    except FileNotFoundError:
        print(f"Error: Archivo '{input_file}' no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo '{input_file}': {e}")

    return lines

def process_lines(lines):
    try:
        return ' '.join(lines) #Une las lineas con un espacio entre ellas
    except Exception as e:
        print(f"Error al procesar las lineas: {e}")
        return ""

def write_file(output_file, content):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content) #escribe el contenido procesado en el nuevo archivo
        print(f"Contenido escrito en '{output_file}' exitosamente.")
    except Exception as e:
        print(f"Error al escribir el archivo '{output_file}': {e}")   

def main():
    input_file = input("Ingrese el nombre del archivo de entrada .txt: ").strip()
    output_file = input("Ingrese el nombre del archivo de salida .txt: ").strip()
    
    lines = read_file(input_file)
    result = process_lines(lines)
    write_file(output_file, result)
    

if __name__ == "__main__":
    main()

