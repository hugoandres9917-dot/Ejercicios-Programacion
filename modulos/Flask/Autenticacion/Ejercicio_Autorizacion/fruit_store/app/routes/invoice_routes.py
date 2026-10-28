#invoice_routes.py RUTAS DE FACTURAS Y COMPRAS 

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.product import Product
from app.models.invoice import Invoice
from app.models.invoice_detail import  InvoiceDetail
from sqlalchemy.orm import selectinload


invoice_bp = Blueprint("invoices", __name__)

# 1. Realizar una compra (Descuenta stock y crea factura)
@invoice_bp.route("/buy", methods=["POST"])
@jwt_required()
def buy_product():
# Obtenemos el ID del usuario logueado por el token
    current_user_id = get_jwt_identity() 
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    
    if not product_id or not quantity or quantity <= 0:
        return jsonify({"error": "Se requiere 'product_id' y una 'quantity' válida"}), 400
        
    product = Product.query.get_or_404(product_id)
    
    # Validamos que haya suficiente stock
    if product.stock < quantity:
        return jsonify({"error": f"Stock insuficiente. Stock disponible: {product.stock}"}), 400
        
    try:
        # Descontamos el stock
        product.stock -= quantity
        
        # Calculamos el total
        total = product.price * quantity
        
        # Creamos la factura
        new_invoice = Invoice(
            user_id=current_user_id,
            total_amount=total
        )
        db.session.add(new_invoice)
    # Para obtener el ID de la factura recién creada
        db.session.flush() 
        
        # Creamos el ítem de la factura
        detail = InvoiceDetail(
            invoice_id=new_invoice.id,
            product_id=product.id,
            quantity=quantity,
            unit_price=product.price
        )
        db.session.add(detail)
        db.session.commit()
        
        return jsonify({
            "message": "Compra realizada con Exito",
            "invoice": new_invoice.serialize()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# 2. Consultar las facturas del cliente autenticado
@invoice_bp.route("/invoices", methods=["GET"])
@jwt_required()
def get_user_invoices():
    current_user_id = get_jwt_identity()
    
# Buscamos las facturas de este usuario
    invoices = Invoice.query.options(
    selectinload(Invoice.invoice_details)
).filter_by(user_id=int(current_user_id)).all()
    
    return jsonify([invoice.serialize() for invoice in invoices]), 200