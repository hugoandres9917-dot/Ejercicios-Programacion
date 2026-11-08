#product_routes.py 
# RUTAS PARA CONSULTAS CRUD DE LOS PRODUCTOS 

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.product import Product
from app.decorators.decorators import admin_required
from app.redis_helper import RedisCacheHelper
from datetime import datetime
from sqlalchemy.exc import IntegrityError

product_bp = Blueprint("products", __name__)

#Ruta publica todos los productos de la fruteria /// con cache
@product_bp.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    try:
        # Intentamos obtener los productos desde el cache de Redis
        cached_products = RedisCacheHelper.get_cache("fruits_all")
        if cached_products:
            return jsonify(cached_products), 200
        
        # Si no hay cache, obtenemos los productos desde la base de datos
        products = Product.query.all()
    #Convertimos los productos a un formato JSON 
        product_list = [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "stock": p.stock,
                "entry_date": p.entry_date.strftime("%Y-%m-%d") if p.entry_date else None
            }
            for p in products
        ]
        
        # Guardamos los productos en el cache de Redis por 5 minutos (300 segundos)
        RedisCacheHelper.set_cache("fruits_all", product_list, expiration=300)
        
        return jsonify(product_list), 200
    except Exception as e:
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500
    
    # GET: Obtener un solo producto por ID (Con Cache Especifico) ---
@product_bp.route("/products/<int:id>", methods=["GET"])
@jwt_required()
def get_product_by_id(id):
    try:
        cache_key = f"fruit:{id}"
        
        # 1. Intentar obtener del cache especifico
        cached_product = RedisCacheHelper.get_cache(cache_key)
        if cached_product:
            return jsonify(cached_product), 200

        # 2. Consultar la Base de Datos
        product = Product.query.get_or_404(id)
        result = product.serialize()
        
        # 3. Guardar en caché específico
        RedisCacheHelper.set_cache(cache_key, result, 300)
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": "Producto no encontrado o error en servidor", "details": str(e)}), 404

#Ruta PROTEGIDA (Solo Admin): Crear un nuevo producto
@product_bp.route("/products", methods=["POST"])
@admin_required
def create_product():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Cuerpo de la peticion vacio"}), 400
    
    name = data.get("name")
    price = data.get("price")
    stock = data.get("stock")
    entry_date_str = data.get("entry_date") 
    
    # Validamos los datos obligatorios
    if not name or price is None or stock is None or not entry_date_str:
        return jsonify({"error": "Faltan datos obligatorios (name, price, stock, entry_date)"}), 400
        
    try:
        # Convertimos el string "YYYY-MM-DD" a un objeto date real
        entry_date_obj = datetime.strptime(entry_date_str, "%Y-%m-%d").date()

        new_product = Product(
            name=name,
            price=price,
            stock=stock,
            entry_date=entry_date_obj 
        )
        db.session.add(new_product)
        db.session.commit()
        
        #invalidar el cache general ya que la lista de productos ha cambiado
        RedisCacheHelper.invalidate_fruit_caches()
        
        return jsonify({
            "message": "Producto creado con Exito",
            "product": new_product.serialize()
        }), 201
        
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Utilice YYYY-MM-DD"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Conflicto: Ya existe un producto con ese nombre"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500

# 4. Ruta PROTEGIDA (Solo Admin): Actualizar un producto
@product_bp.route("/products/<int:id>", methods=["PUT"])
@admin_required
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return jsonify({"error": "Cuerpo de la peticion vacio"}), 400
    
    try:
        if "name" in data:
            product.name = data["name"]
        if "price" in data:
            product.price = data["price"]
        if "stock" in data:
            product.stock = data["stock"]
        
        if "entry_date" in data:
            product.entry_date = datetime.strptime(data["entry_date"], "%Y-%m-%d").date()
        
        db.session.commit()
        # Invalidar cache específico y lista general
        RedisCacheHelper.invalidate_fruit_caches(fruit_id=id)  
        return jsonify({"message": "Producto actualizado con Exito", "product": product.serialize()}), 200
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Utilice YYYY-MM-DD"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Conflicto: El nombre del producto ya está en uso"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500

# 5. DELETE: Eliminar un producto (Solo Admin) - Invalida Caché Específico y General
@product_bp.route("/products/<int:id>", methods=["DELETE"])
@admin_required
def delete_product(id):
    product = Product.query.get_or_404(id)
    try:
        db.session.delete(product)
        db.session.commit()
        
        # INVALIDAR CACHÉ: Limpiamos la lista general y la fruta eliminada
        RedisCacheHelper.invalidate_fruit_caches(fruit_id=id)
        
        return jsonify({"message": "Producto eliminado con Éxito"}), 200
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Conflicto: No se puede eliminar el producto porque está asociado a facturas existentes"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500