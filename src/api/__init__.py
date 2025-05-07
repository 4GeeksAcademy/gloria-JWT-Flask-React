# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_jwt_extended import JWTManager
# import os

# db = SQLAlchemy()
# migrate = Migrate()
# jwt = JWTManager()

# def init_app():
#     app = Flask(__name__)
    
#     # Configuración
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
#     app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hora
    
#     # Inicializar extensiones
#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)
    
#     # Importar y registrar blueprints/rutas
#     from .routes import init_app as init_routes
#     init_routes(app)
    
#     # return app