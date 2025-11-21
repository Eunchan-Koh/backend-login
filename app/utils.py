from flask_bcrypt import Bcrypt
from datetime import datetime, timezone, timedelta
import jwt
from flask import current_app, make_response

bcrypt = Bcrypt()

def hashing(value: str):
    # add hash, salt, key change
    hashed = bcrypt.generate_password_hash(value).decode('utf-8')
    return hashed

def check_password(hased_pw, pw):
    return bcrypt.check_password_hash(hased_pw, pw)

def create_access_token(id: str):
    payload = {
                "user": id,
                "exp": datetime.now(timezone.utc) + timedelta(seconds=15)
            }
            
    token = jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm=current_app.config['JWT_ALGORITHM'])
    return token

def create_access_cookie(token: str):
    resp = make_response("access granted!")
    resp.set_cookie("access_token", token, httponly=True, secure=True, samesite='Strict')
    return resp