from flask import Flask, blueprints
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    bootstrap.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)

    from .views import main
    app.register_blueprint(main)

    with app.app_context():
        from app import models, views
        db.create_all()

    return app
