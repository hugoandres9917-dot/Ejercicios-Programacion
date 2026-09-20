## validacion de conexion y salud de sistema

import psycopg2

# Configuración de la base de datos
DB_CONFIG = {
    "dbname": "postgres",  # Si tu base de datos principal se llama 'postgres', mantén 'postgres'. Si creaste una BD llamada 'lyfter_car_rental', cámbialo aquí.
    "user": "postgres",
    "password": "Antonella60",
    "host": "localhost",
    "port": "5432",
}

# Tablas requeridas (en español según los requerimientos de la actividad)
REQUIRED_TABLES = ["users", "vehicles", "rentals"]


def check_system_health():
    try:
        # Intentar conectar a la base de datos
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Configurar el esquema
        cursor.execute("SET search_path TO lyfter_car_rental;")

        # Verificar si las 3 tablas existen en el esquema
        cursor.execute(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'lyfter_car_rental';
            """
        )
        existing_tables = [row[0] for row in cursor.fetchall()]

        for table in REQUIRED_TABLES:
            if table not in existing_tables:
                print(f"DB ERROR. Falta la tabla '{table}' en la base de datos.")
                cursor.close()
                conn.close()
                return

        # Verificar si hay al menos 1 automóvil disponible
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM vehicles
            WHERE status = 'disponible';
            """
        )
        available_cars = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        # Mensajes finales de respuesta
        if available_cars >= 1:
            print("DB OK. Sistema operativo con normalidad")
        else:
            print("DB ERROR. No hay autos disponibles")

    except psycopg2.Error as e:
        # Se incluye 'as e' para poder imprimir el detalle real del error de conexión
        print(f"DB ERROR. No se pudo conectar a la base de datos: {e}")
    except Exception as e:
        print(f"DB ERROR. Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    check_system_health()