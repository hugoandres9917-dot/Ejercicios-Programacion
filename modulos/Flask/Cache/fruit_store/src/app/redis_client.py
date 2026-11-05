#redis_client
#Ejercicio de Caché

import os
import redis

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "PLACEHOLDER"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    password=os.getenv("REDIS_PASSWORD", "PLACEHOLDER"),
    decode_responses=True  # Recomendado para trabajar directamente con strings en JSON
)
#probar la conexion
def test_redis_connection():
    try:
        connection_status = redis_client.ping()
        if connection_status:
            print("Conectado a Redis")
            return True
        else:
            print("La conexion a Redis fue rechazada")
            return False
    except redis.ConnectionError as ex:
        print("un error occurrio al conectar a Redis: ", ex)
        return False