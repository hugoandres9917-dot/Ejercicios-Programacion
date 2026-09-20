# backup automatizado

import os
import csv
from datetime import datetime
import psycopg2

# configuracion de la base dae datos

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Antonella60",
    "host": "localhost",
    "port": "5432"
}

#tablas a exportar

TABLES_TO_BACKUP = ["users", "vehicles", "rentals"] ##lista de tablas

def get_db_connection():# crea y retona la conexion a postgres con el shema configurado
    conn = psycopg2.connect(**DB_CONFIG)
    with conn.cursor() as cur:
        cur.execute("SET search_path TO lyfter_car_rental;")
    return conn

def export_table_to_csv(cursor, table_name, output_folder):##Consulta una tabla y escribe sus datos junto con los encabezados en un CSV
    cursor.execute(f"SELECT * FROM {table_name};")
    column_names = [desc[0] for desc in cursor.description]## extraemos los nombres de las columnas del cursor
    rows = cursor.fetchall()
    
    ##formato para nombre
    date_str = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(
        output_folder, f'backup_{date_str}_{table_name}.csv')
    
    with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        write =csv.writer(csv_file)
        write.writerow(column_names)##escribir encabezado
        write.writerows(rows)#escribir filas de datos
        
    print(F"Exportado exitosamente: {file_path}")
    print(f"Tabla {table_name}: {len(rows)} filas exportadas.")#cantidad de filas

    
def run_backup():
    backup_dir = "db_backups"
    
    #asegurar que exista el directorio
    os.makedirs(backup_dir, exist_ok=True)
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        for table in TABLES_TO_BACKUP:
            export_table_to_csv(cursor, table, backup_dir)
            
        cursor.close()
        conn.close()
        print("Backup finalizado con exito.")
        
    except Exception as e:
        print(f"Error durante el backup: {e}")
        
if __name__ == "__main__":##ejecutar aplicacion 
    run_backup()
    
    
            