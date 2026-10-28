#login_password
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app import db  
from app.models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    
    # 1. Buscamos al usuario en la base de datos por su email
    user = User.query.filter_by(email=email).first()
    
    # 2. Verificamos si el usuario existe y si la contraseña es correcta
    if not user or not user.check_password(password):
        return jsonify({"error": "Credenciales inválidas"}), 401
        
    # 3. Creamos los claims adicionales con el rol del usuario (Admin o User)
    additional_claims = {"role": user.role}
    
    # 4. Generamos los tokens utilizando RS256 (configurados previamente en Config)
    access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
    refresh_token = create_refresh_token(identity=str(user.id))
    
    # 5. Retornamos los tokens al cliente
    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    }), 200
    

# 6. Ruta de Registro para crear usuarios o administradores
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
# Por defecto será 'user' a menos que especifiques 'admin'
    role = data.get("role", "user")  
    
    if not username or not email or not password:
        return jsonify({"error": "El email y la contraseña son obligatorios"}), 400
        
    # Verificar si el usuario ya existe
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "El correo ya está registrado"}), 400
        
    try:
# Crear nuevo usuario (asumiendo que tu modelo hashea la contraseña automáticamente o usas set_password)
        new_user = User(
            username=username,
            email=email,
            role=role
        )
        new_user.set_password(password)  
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            "message": "Usuario registrado con Exito",
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "email": new_user.email,
                "role": new_user.role
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()
    user = User.query.get_or_404(current_user_id)
    return jsonify(user.serialize()), 200