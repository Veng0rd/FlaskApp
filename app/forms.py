# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField
# from wtforms.validators import InputRequired, Email, Length
# from flask_sqlalchemy import SQLAlchemy
# from app import db
#
#
# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
#     password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
#     remember = BooleanField('Remember me')
#
#
# class RegisterForm(FlaskForm):
#     email = StringField('Email', validators=[InputRequired(), Email(message='Неправильный формат!'), Length(max=50)])
#     username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
#     password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))
