#decorators

#control de roles middleware personalizado 
#decorador para verificar si el usuario tiene el rol adecuado para acceder a una función específica.

from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt, verify_jwt_in_request

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #verifica que venga un token válido en la solicitud
        verify_jwt_in_request()
        claims = get_jwt()
        # vemos si el claim ' role' es igual a 'admin'
        if claims.get('role') != 'admin':
            return jsonify({"error": "Acceso denegado. Se requiere rol de administrador."}), 403
        
        return fn(*args, **kwargs)
    return wrapper


        