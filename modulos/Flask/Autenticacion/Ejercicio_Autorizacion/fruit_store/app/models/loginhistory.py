#loginhistory 
#LoginHistory que guarde:
#ID del usuario
#Fecha y hora del login
#IP (puede simularse)
#Si el login fue exitoso o fallido

from datetime import datetime
from app import db #IMPORTAMOS LA INSTANCIA GLOBAL CORRECTA (Elimina db = SQLAlchemy())


class LoginHistory(db.Model):
    __tablename__ = "login_history"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)#Asocia con la tabla  Users
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ip_address = db.Column(db.String(45), nullable=False)  # Almacena IP 
    success = db.Column(db.Boolean, nullable=False) 

# Relacion inversa opcional para consultar el historial desde el usuario
    user = db.relationship("User", backref=db.backref("login_history", lazy=True))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "timestamp": self.timestamp.isoformat(),
            "ip_address": self.ip_address,
            "success": self.success,
        }