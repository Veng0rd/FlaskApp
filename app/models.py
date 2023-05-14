from flask_login import UserMixin

from app import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    login = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
