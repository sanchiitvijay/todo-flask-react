from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from .config import Config
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS
    CORS(app)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from .routes.auth import auth_bp
    from .routes.todos import todos_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(todos_bp, url_prefix='/todos')
    
    with app.app_context():
        from .models import User, ToDo
        db.create_all()

    return app
