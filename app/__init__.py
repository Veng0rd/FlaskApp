from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd5fb8c4fa8bd46638dadc4e751e0d68d'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)
with app.app_context():
    # Your code here, for example:
    db.create_all()
bootstrap = Bootstrap(app)
