#generate_keys.py

#este script se ejecuta una sola vez para generar las llaves privadas y publicas que se utilizaran para firmar y verificar los tokens JWT

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_keys():
# generar claves privadas
    private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# serializar y guardar la llave privada en formato PEM
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )   
    with open("private_key.pem", "wb") as f:
        f.write(private_pem)
    
# generar y guardar la llave publica
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo  
    )

    with open("public_key.pem", "wb") as f:
        f.write(public_pem)
    
    print("Llaves privadas y publicas generadas y guardadas en 'private_key.pem' y 'public_key.pem' respectivamente.")

if __name__ == "__main__":
    generate_keys()
    
    