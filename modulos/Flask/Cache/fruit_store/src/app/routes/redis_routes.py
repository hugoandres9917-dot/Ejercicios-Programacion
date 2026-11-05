#cache 
#rutas con Redis 

import json
from flask import Blueprint, jsonify, request
from app import db
from app.models.product import Product
from app.redis_client import redis_client # 

redis_fruit_bp = Blueprint('redis_fruit_bp', __name__)

#metodo GET: Listar todas las frutas/productos (Caché general) 
@redis_fruit_bp.route('/fruits', methods=['GET'])
def get_fruits():
    try:
        cached_fruits = redis_client.get("fruits_all")
        if cached_fruits:
            return jsonify(json.loads(cached_fruits)), 200

        products = Product.query.all()
        result = [product.serialize() for product in products]
        
        # Guardar en cache por 5 minutos (300 segundos)
        redis_client.setex("fruits_all", 300, json.dumps(result))
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500

#metoddo GET: Obtener una fruta ID (Cache especifico)
@redis_fruit_bp.route('/fruits/<int:fruit_id>', methods=['GET'])
def get_fruit_by_id(fruit_id):
    try:
        cache_key = f"fruit:{fruit_id}"
        cached_fruit = redis_client.get(cache_key)
        
        if cached_fruit:
            return jsonify(json.loads(cached_fruit)), 200

        # Consulta mediante ORM
        product = Product.query.get(fruit_id)
        if not product:
            return jsonify({"error": "Fruta no encontrada"}), 404

        result = product.serialize()
        # Guardar en cache especifico de esta fruta
        redis_client.setex(cache_key, 300, json.dumps(result))
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500

#metodo POST: Crear una fruta (Invalida la lista general)
@redis_fruit_bp.route('/fruits', methods=['POST'])
def create_fruit():
    try:
        body = request.get_json()
        if not body or 'name' not in body or 'price' not in body or 'stock' not in body:
            return jsonify({"error": "Datos invalidos (se requiere name, price, stock, entry_date)"}), 400

        from datetime import datetime
        entry_date = datetime.strptime(body.get('entry_date'), "%Y-%m-%d").date() if 'entry_date' in body else datetime.today().date()

        new_product = Product(
            name=body['name'],
            price=body['price'],
            stock=body['stock'],
            entry_date=entry_date
        )
        db.session.add(new_product)
        db.session.commit()

        # Invalidar el cache de la lista general
        redis_client.delete("fruits_all")

        return jsonify(new_product.serialize()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500

#metodo PUT: Actualizar una fruta(Invalida cache específico y lista general)
@redis_fruit_bp.route('/fruits/<int:fruit_id>', methods=['PUT'])
def update_fruit(fruit_id):
    try:
        product = Product.query.get(fruit_id)
        if not product:
            return jsonify({"error": "Fruta no encontrada"}), 404

        body = request.get_json()
        if not body:
            return jsonify({"error": "Cuerpo de la peticion vacio"}), 400

        if 'name' in body:
            product.name = body['name']
        if 'price' in body:
            product.price = body['price']
        if 'stock' in body:
            product.stock = body['stock']
        
        db.session.commit()

        # Invalidacion específica de la fruta actualizada y de la lista general
        redis_client.delete(f"fruit:{fruit_id}")
        redis_client.delete("fruits_all")

        return jsonify(product.serialize()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500

#metodo DELETE: Eliminar una fruta(Invalida cache específico y lista general)   
@redis_fruit_bp.route('/fruits/<int:fruit_id>', methods=['DELETE'])
def delete_fruit(fruit_id):
    try:
        product = Product.query.get(fruit_id)
        if not product:
            return jsonify({"error": "Fruta no encontrada"}), 404

        db.session.delete(product)
        db.session.commit()

        # Invalidacion especifica de la fruta eliminada y de la lista general
        redis_client.delete(f"fruit:{fruit_id}")
        redis_client.delete("fruits_all")

        return jsonify({"message": "Fruta eliminada exitosamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500