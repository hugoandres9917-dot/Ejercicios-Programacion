#product_routes.py RUTAS PARA CONSULTAS CRUD DE LOS PRODUCTOS 

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.product import Product
from app.decorators.decorators import admin_required
from datetime import datetime

product_bp = Blueprint("products", __name__)

# 1. Ruta publica todos los productos de la fruteria
@product_bp.route("/products", methods=["GET"])
def get_products():
    try:
        products = Product.query.all()
        # Convertimos los productos a un formato JSON 
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
        return jsonify(product_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 2. Ruta PROTEGIDA (Solo Admin): Crear un nuevo producto
@product_bp.route("/products", methods=["POST"])
@admin_required
def create_product():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")
    stock = data.get("stock")
    entry_date_str = data.get("entry_date") 
    
    # Validamos 
    if not name or price is None or stock is None or not entry_date_str:
        return jsonify({"error": "Faltan datos obligatorios (name, price, stock, entry_date)"}), 400
        
    try:
        # Convertimos el string "YYYY-MM-DD" a un objeto date real
        entry_date_obj = datetime.strptime(entry_date_str, "%Y-%m-%d").date()

        new_product = Product(
            name=name,
            price=price,
            stock=stock,
            entry_date=entry_date_obj #lo asignamos al modelo
        )
        db.session.add(new_product)
        db.session.commit()
        
        return jsonify({
            "message": "Producto creado con éxito",
            "product": {
                "id": new_product.id,
                "name": new_product.name,
                "price": new_product.price,
                "stock": new_product.stock,
                "entry_date": new_product.entry_date.strftime("%Y-%m-%d")
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
# 3. Ruta PÚBLICA: Ver un solo producto por ID
@product_bp.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.serialize()), 200

# 4. Ruta PROTEGIDA (Solo Admin): Actualizar un producto
@product_bp.route("/products/<int:id>", methods=["PUT"])
@admin_required
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    
    product.name = data.get("name", product.name)
    product.price = data.get("price", product.price)
    product.stock = data.get("stock", product.stock)
    
    if "entry_date" in data:
        product.entry_date = datetime.strptime(data["entry_date"], "%Y-%m-%d").date()
        
    db.session.commit()
    return jsonify({"message": "Producto actualizado con éxito", "product": product.serialize()}), 200

# 5. Ruta PROTEGIDA (Solo Admin): Eliminar un producto
@product_bp.route("/products/<int:id>", methods=["DELETE"])
@admin_required
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Producto eliminado con éxito"}), 200