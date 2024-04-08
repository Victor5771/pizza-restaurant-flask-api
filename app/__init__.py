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

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        # Import models here to ensure they are in the app context
        from app.models import Restaurant
        
        # Create tables if they don't exist
        db.create_all()

        # Insert initial data if the restaurant table is empty
        if not Restaurant.query.first():
            restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
            restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')
            db.session.add(restaurant1)
            db.session.add(restaurant2)
            db.session.commit()

    from app.routes import routes_bp
    app.register_blueprint(routes_bp)

    return app