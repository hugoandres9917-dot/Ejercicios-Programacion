#Hasheo de Contraseñas con MD5
# nombre de archivo password_generator.py

import hashlib

password = "mypassword123"
hashed_password = hashlib.md5(password.encode()).hexdigest()

print(hashed_password)  # 13b27e73be9e7348661087267dc31c1, por ejemplo