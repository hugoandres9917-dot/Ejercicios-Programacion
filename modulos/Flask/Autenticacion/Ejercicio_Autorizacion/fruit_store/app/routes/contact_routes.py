#contact_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app import db
from app.models.contact import Contact

contact_bp = Blueprint("contacts", __name__)
@jwt_required
def get_contacts():
    current_user_id = int(get_jwt_identity())
    claims = get_jwt()
    role = claims.get("role")
    
#ojo si es admin, ve todos los contactos;
# si es usuario normal, solo sus contactos
    if role == "admin":
        contacts = Contact.query.all()
    else:
        contacts = Contact.query.filter_by(user_id=current_user_id).all()

    return jsonify([contact.serialize() for contact in contacts]), 200

###metodos
#crear contacto (POST)
@contact_bp.route("/contacts", methods=["POST"])
@jwt_required()
def create_contact():
    current_user_id = int(get_jwt_identity())
    data = request.get_json()
    
    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")
    
    if not name or not phone or not email:
        return jsonify({"error": "El nombre, el telefono y el correo son obligatorios"}), 400
    
    new_contact = Contact(
        name=name,
        phone=phone,
        email=email,
        user_id=current_user_id
    )
    
    db.session.add(new_contact)
    db.session.commit()
    
    return jsonify({
        "message": "Contacto creado con Exito",
        "contact": new_contact.serialize()
    }), 201


#ACTUALIZAR CONTACTO
@contact_bp.route("/contacts/<int:id>", methods=["PUT"])
@jwt_required()
def update_contact(id):
    current_user_id = int(get_jwt_identity())
    claims = get_jwt()
    role = claims.get("role")
    
    contact = Contact.query.get_or_404(id)
    # Validar permisos: Usuario normal solo edita lo suyo. Admin puede editar 
    if role != "admin" and contact.user_id != current_user_id:
        return jsonify({"error": "No tienes permisos para modificar este contacto"}), 403
    
    data = request.get_json()
    contact.name = data.get("name", contact.name)
    contact.phone = data.get("phone", contact.phone)
    contact.email = data.get("email", contact.email)

    db.session.commit()
    
    return jsonify({
        "message": "Contacto actualizado con Exito",
        "contact": contact.serialize()
    }), 200
    
#Eliminar contacto (DELETE)
@contact_bp.route("/contacts/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_contact(id):
    current_user_id = int(get_jwt_identity())
    claims = get_jwt()
    role = claims.get("role")

    contact = Contact.query.get_or_404(id)
    #Admin puede eliminar cualquiera, usuario solo los suyos
    if role != "admin" and contact.user_id != current_user_id:
        return jsonify({"error": "No tienes permisos para eliminar este contacto"}), 403

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "Contacto eliminado con Exito"}), 200