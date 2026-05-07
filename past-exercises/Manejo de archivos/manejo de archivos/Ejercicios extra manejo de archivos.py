# ejercicios extra manejo de archivos

# 1.Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo

#correcciones
#En los ejercicios 1, 2 y 3, los nombres de archivo están escritos directamente en main().
#La regla transversal pide evitar hardcodeo;
#una opción es pedirle al usuario el nombre del archivo con input() al inicio de cada ejercicio.

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



#2.Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
#(Considere que las palabras están separadas por espacios y/o saltos de línea)

def read_file2(entry_file):
    try:
        with open(entry_file, 'r', encoding= 'utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: Archivo '{entry_file}' no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo '{entry_file}': {e}")
        return ""

def count_words(text):
    try:
        if not text:
            return 0
        words = text.split() # separa por salto de linea y espcacios 
        return len(words)
    except Exception as e:
        print(f"Error al contar las palabras: {e}")
        return 0

def show_result(word_count):
    try:
        print(f"El archivo contiene {word_count} palabras.")
    except Exception as e:
        print(f"Error al mostrar el resultado: {e}")
        
def main2():
    entry_file = input("Ingrese el nombre del archivo de entrada .txt: ").strip()
    text = read_file2(entry_file)
    total_words = count_words(text)
    show_result(total_words)
    

if __name__ == "__main__":
    main2()
        
    
    
    
#3.Cree un programa que:Lea un archivo línea por línea Convierta cada línea a mayúsculas
#Escriba el contenido en un nuevo archivo

#readlines() ya incluye el \n al final de cada línea.
#Si luego en write_file se agrega otro \n, 
# el archivo de salida tendrá líneas en blanco entre cada línea de contenido. 
# Puede solucionarlo usando line.strip().upper() antes de escribir, y luego agregar un solo \n.

def read_file3(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: Archivo '{input_file}' no encontrado.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo '{input_file}': {e}")
        return []


def convert_to_uppercase(lines):
    try:
        uppercase_lines = [line.strip().upper() for line in lines if line.strip()]# convertimos cada linea a mayusculas y eliminamos los saltos de linea
        return uppercase_lines
    except Exception as e:
        print(f"Error al convertir a mayusculas: {e}")
        return []

def write_file3(output_file, lines):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
                # escribimos cada linea en el nuevo archivo sin agregar un salto de linea adicional, ya que cada linea ya tiene su propio salto de linea al final
        print(f"Contenido convertido a mayusculas y guardado en '{output_file}' exitosamente.")
        print(f"Se han convertido {len(lines)} líneas a mayúsculas.")
    except Exception as e:
        print(f"Error al escribir el archivo '{output_file}': {e}")

def main3():
    input_file = input("Ingrese el nombre del archivo de entrada .txt: ").strip()
    output_file = input("Ingrese el nombre del archivo de salida .txt: ").strip()

    lines = read_file3(input_file)
    uppercase_lines = convert_to_uppercase(lines)
    write_file3(output_file, uppercase_lines)

if __name__ == "__main__":
    main3()
    
    
    
#Cree un programa que: Pida al usuario una línea de texto, Agregue esa línea al final de un archivo existente
#Si el archivo no existe, lo crea automáticamente


def append_line_to_file(file_name):
    try:
        new_line = input("Ingrese una linea de texto para agregar al archivo: ")
        with open(file_name, 'a', encoding='utf-8') as file:# modo apppend "a"
            file.write(new_line + '\n') # escribimos la nueva línea en el archivo con un salto de linea
        print(f"Linea agregada al archivo '{file_name}' exitosamente.")
    except Exception as e:
        print(f"Error al agregar la linea al archivo '{file_name}': {e}")

def main4():
    file_name = input("Ingrese el nombre del archivo al que desea agregar la linea .txt: ").strip()
    append_line_to_file(file_name)

if __name__ == "__main__":
    main4()
    
    