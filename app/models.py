from flask_wtf import FlaskForm
from flask_login import UserMixin

from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

from app import db, manager


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')


class RegisterForm(FlaskForm):
    login = StringField('Login', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Неправильный формат!'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
