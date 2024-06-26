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

    with app.app_context():
        
        from app.models import Restaurant
        
        
        db.create_all()

        
        if not Restaurant.query.first():
            restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
            restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')
            db.session.add(restaurant1)
            db.session.add(restaurant2)
            db.session.commit()

    from app.routes import routes_bp
    app.register_blueprint(routes_bp)

    return app