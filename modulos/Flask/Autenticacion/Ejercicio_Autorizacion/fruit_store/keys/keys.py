#Keys

from flask_extended import create_acces_token, create_refresh_token

#dentro de tu ruta/login/ register

additional_claims = {"role": user.role}
access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
refresh_token = create_refresh_token(identity=str(user.id))
