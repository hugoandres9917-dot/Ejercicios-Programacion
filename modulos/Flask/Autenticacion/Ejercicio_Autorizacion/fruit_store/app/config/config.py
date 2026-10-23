# config.py

import os

class Config:
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:Antonella60@localhost:5432/fruteria_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #configuración de JWT para usar RS256
    JWT_ALGORITHM = 'RS256'
    #leemos las llaves rsa recien creadas
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    with open(os.path.join(BASE_DIR, "keys", "private.pem"), "r") as f:
        JWT_PRIVATE_KEY = f.read()
        
    with open(os.path.join(BASE_DIR, "keys", "public.pem"), "r") as f:
        JWT_PUBLIC_KEY = f.read()