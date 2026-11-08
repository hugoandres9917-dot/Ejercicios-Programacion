# helper para manejar el cache de redis

import json
import app.redis_client as redis_client


class RedisCacheHelper:
    @staticmethod
    def get_cache(key):
        # Obtener datos del cache de Redis
        try:
            cached_data = redis_client.get(key)
            if cached_data:
                return json.loads(cached_data)
        except Exception:
            pass# en caso que falle caonsulta la base de datos
        return None
    
    @staticmethod
    def set_cache(key, data, expiration=300):
        # Guardar datos en el cache de Redis
        try:
            redis_client.setex(key, expiration, json.dumps(data))
        except Exception:
            pass  # en caso que falle no hace nada
        
    @staticmethod
    def delete_cache(key):
        # Eliminar datos del cache de Redis
        try:
            redis_client.delete(key)
        except Exception:
            pass  
        
    @staticmethod
    def invalidate_fruit_caches(fruit_id=None):
        RedisCacheHelper.delete_cache("fruits_all")
        if fruit_id:
            RedisCacheHelper.delete_cache(f"fruit:{fruit_id}")                