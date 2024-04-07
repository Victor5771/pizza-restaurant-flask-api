# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.models import db
    db.init_app(app)

    from app.routes import routes_bp
    app.register_blueprint(routes_bp)

    return app
