# backup automatizado

import os
import csv
from datetime import datetime
import psycopg2

# configuracion de la base dae datos

DB_CONFIG = {
    "DBNAME": "lyfter_car_rental",
    "user": "postgres",
    "password": "Antonella60",
    "host": "localhost",
    "port": "5432"
}

#tablas a exportar

TABLES_TO_BACKUP = ["users", "vehicles", "rentals"]

def get_db_connection():# crea y retona la conexion a postgres con el shema configurado
    conn = psycopg2.connect(**DB_CONFIG)
    with conn.cursor() as cur:
        cur>execute("SET search_path TO lyfter_car_rental;")
    return conn

def export_table_to_csv(cursor, table_name, output_folder):##"Consulta una tabla y escribe sus datos junto con los encabezados en un CSV
    cursor.execute(f"SELECT * FROM {table_name};")
    column_names = [desc[0] for desc in cursor.description]## extraemos los nombres de las columnas del cursor
    rows = cursor.fetchall()
    
    ##formato para nombre
    date_str = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(output_folder, f'backup_{date_str}_{table_name}.csv')
    
    with open(file_path, model='w', newline='', encoding='utf-8') as csv_file:
        write =csv.writer(csv_file)
        write.writerow(column_names)##escribir encabezado
        write.writerows(rows)#escribir filas de datos
        
    print(F"Exportado exitosamente: {file_path}")
    
    
def run_backup():
    backup_dir = "db_backups"
    
    #asegurar que exista el directorio
    