from flask import Flask
from .extensions import db, migrate
from .routes import bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(bp)
    
    
    return app