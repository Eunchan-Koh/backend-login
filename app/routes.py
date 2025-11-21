from flask import Flask, request, jsonify, render_template, Blueprint, current_app, make_response
from sqlalchemy import create_engine, text
from .extensions import db, User, MAX_ID_LENGTH

import jwt
from .utils import hashing, check_password, create_access_token


bp = Blueprint('main', __name__)


# testing for practice
@bp.route('/testing', methods=['GET'])
def testing():
    return jsonify({'message': f'testing!'})

@bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')


#log in process
@bp.route('/login', methods=['POST'])
def login():
    id = request.form['user_id']
    pw = request.form['user_pw']
    user = User.query.filter_by(iden=id).first()
    
    if user and check_password(user.pw, pw):
        # create jwt token
        token = create_access_token(id)
        # create cookie, and insert token as access_token
        resp = make_response("access granted!")
        resp.set_cookie("access_token", token, httponly=True, secure=True, samesite='Strict')
        return resp
    else:
        return jsonify({'msg': 'typed in wrong id or password.'}), 400
    

# registration process
@bp.route('/create', methods=['POST'])
def create():
    id = request.form['user_id']
    if len(id) > MAX_ID_LENGTH:
        return f'id length must be shorter than {MAX_ID_LENGTH}'
    pw = request.form['user_pw']
    user = User.query.filter_by(iden=id).first()
    if user:
        return jsonify({'msg': 'The username already exist! Did you forget your password?'}), 409
    else:
        pw = hashing(pw)
        user = User(iden=id, pw=pw)
        db.session.add(user)
        db.session.commit()
        return f'registered!'
    
@bp.route('/add', methods=['GET'])
def add():
    a = request.args.get('user_id')
    b = request.args.get('user_pw')
    result = a+b
    return jsonify({'msg':f'Result is {result}.'}), 200 

@bp.route('/protected')
def protected():
    access_token = request.cookies.get("access_token")
    if not access_token:
        return jsonify({'error':'no token'}), 401
    
    try:
        decode = jwt.decode(access_token,current_app.config['JWT_SECRET_KEY'],algorithms=current_app.config['JWT_ALGORITHM'])
        
        return jsonify({'msg':f'hello, {decode['user']}! accepted!'})
    except jwt.ExpiredSignatureError:
        return jsonify({'msg': 'token expired.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'msg': 'invalid token'}), 401