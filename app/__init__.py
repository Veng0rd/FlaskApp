from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
manager = LoginManager(app)
db = SQLAlchemy(app)

with app.app_context():
    from app import models, views
    db.create_all()
