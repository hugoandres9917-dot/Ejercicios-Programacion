# login_password.py
from app import db
from app.decorators.decorators import admin_required
from app.models.loginhistory import (LoginHistory,)
from app.models.user import User
from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    #Simulacion u obtencion de la IP del cliente
    client_ip = request.remote_addr or "127.0.0.1"

    #Buscamos al usuario en la base de datos por su email
    user = User.query.filter_by(email=email).first()

    #Verificamos si el usuario existe y si la contraseña es correcta
    if not user or not user.check_password(password):
        failed_record = LoginHistory(
            user_id=user.id if user else None,  # Maneja si user es None
            ip_address=request.remote_addr,
            success=False,
        ) 
    
        db.session.add(failed_record)
        db.session.commit()

        return jsonify({"error": "Credenciales invalidas"}), 401


    #SI EL LOGIN ES EXITOSO
    success_record = LoginHistory(user_id=user.id, ip_address=client_ip, success=True)
    db.session.add(success_record)
    db.session.commit()

    #Creamos los claims adicionales con el rol del usuario (Admin o User)
    additional_claims = {"role": user.role}

    #Generamos los tokens utilizando RS256
    access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
    refresh_token = create_refresh_token(identity=str(user.id))

    #Retornamos los tokens al cliente
    return (
        jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": {"id": user.id, "email": user.email, "role": user.role},
        }),
        200,
    )


    #Ruta de Registro para crear usuarios o administradores
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    #Por defecto user
    role = data.get("role", "user")

    if not username or not email or not password:
        return jsonify({"error": "El email y la contraseña son obligatorios"}), 400

    #Verificar si el usuario ya existe
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "El correo ya está registrado"}), 400

    try:
        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return (
            jsonify({
                "message": "Usuario registrado con Exito",
                "user": {
                    "id": new_user.id,
                    "username": new_user.username,
                    "email": new_user.email,
                    "role": new_user.role,
                },
            }),
            201,
        )

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()
    user = User.query.get_or_404(current_user_id)
    return jsonify(user.serialize()), 200

##### Endpoint Refresh-token (ejercicio extra 2.)
@auth_bp.route("/refresh-token", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user_id = get_jwt_identity()
    #Buscamos al usuario para asegurarnos de que sigue activo/existe
    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    #Creamos los claims
    additional_claims = {"role": user.role}
    #Generamos UN NUEVO Access Token
    new_access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)

    return jsonify({"access_token": new_access_token}), 200

### Endpoint Historial de Inicio de Sesión (Ejercicio Extra 3)
@auth_bp.route("/login-history", methods=["GET"])
@jwt_required()
@admin_required
def get_login_history():
    history = LoginHistory.query.all()
    return jsonify([h.serialize() for h in history]), 200