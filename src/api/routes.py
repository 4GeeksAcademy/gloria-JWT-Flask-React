from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from .models import db,User
from flask import Blueprint
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

# Rutas de autenticación
@api.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User already exists'}), 400
    
    new_user = User(email=data['email'], password=data['password'], is_active=True)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required'}), 400
    
    user = User.query.filter_by(email=data['email'], password=data['password']).first()
    
    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity=user.email)
    return jsonify({'access_token': access_token}), 200

@api.route('/private', methods=['GET'])
@jwt_required()
def private():
    current_user = get_jwt_identity()
    return jsonify({'message': f'Hello {current_user}! This is a private route.'}), 200
    

# Define tus rutas aquí
@api.route('/hello', methods=['GET'])
def hello():
    return {"message": "Hello, world!"}, 200

@api.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    current_user = get_jwt_identity()
    return jsonify({"message": f"User {current_user} logged out (token should be deleted client-side)."}), 200
