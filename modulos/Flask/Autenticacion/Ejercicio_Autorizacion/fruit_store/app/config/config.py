
# config.py
import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:Antonella60@localhost:5432/fruteria_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
#Configuracion de JWT para usar RS256
    JWT_ALGORITHM = 'RS256'
    
    private_key_path = os.path.join(BASE_DIR, "keys", "private_key.pem")
    public_key_path = os.path.join(BASE_DIR, "keys", "public_key.pem")
    
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
    
    with open(private_key_path, "rb") as f:
        JWT_PRIVATE_KEY = f.read()
        
    with open(public_key_path, "rb") as f:
        JWT_PUBLIC_KEY = f.read()