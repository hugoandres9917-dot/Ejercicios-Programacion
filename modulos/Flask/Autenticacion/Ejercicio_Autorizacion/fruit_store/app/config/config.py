
# config.py
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:tu_password@localhost:5432/fruteria_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
# Configuración de JWT para usar RS256
    JWT_ALGORITHM = 'RS256'
    
    private_key_path = os.path.join(BASE_DIR, "keys", "private_key.pem")
    public_key_path = os.path.join(BASE_DIR, "keys", "public_key.pem")
    
    with open(private_key_path, "r", encoding="utf-8") as f:
        JWT_PRIVATE_KEY = f.read()
        
    with open(public_key_path, "r", encoding="utf-8") as f:
        JWT_PUBLIC_KEY = f.read()