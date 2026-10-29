# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config.config import Config

# Instancias globales
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    
    # IMPORTANTE: Los blueprints se importan y registran AQUÍ ABABAJO, 
    # cuando 'db' y 'jwt' ya terminaron de crearse por completo.
    from app.routes.auth_routes import auth_bp
    from app.routes.product_routes import product_bp
    from app.routes.invoice_routes import invoice_bp
    from app.routes.contact_routes import contact_bp 
    
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(product_bp, url_prefix="/api")
    app.register_blueprint(invoice_bp, url_prefix="/api")
    app.register_blueprint(contact_bp, url_prefix="/api")  # Registrar el blueprint
    
    with app.app_context():
        from app.models.user import User
        from app.models.product import Product
        from app.models.invoice import Invoice          
        from app.models.invoice_detail import InvoiceDetail
        from app.models.contact import Contact # Importar el modelo Contact para que db.create_all() cree la tabla
        from app.models.loginhistory import LoginHistory
        
        db.create_all()
    
    return app