from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.getenv('FLASK_APP_KEY')
    
    db.init_app(app)
    jwt.init_app(app)
    
    from .routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api')
    
    return app