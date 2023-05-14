from flask_wtf import FlaskForm, RecaptchaField, Recaptcha
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Неправильный формат!'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')
    recaptcha = RecaptchaField(validators=[Recaptcha(message='Please complete the captcha')])


class RegisterForm(FlaskForm):
    login = StringField('Login', validators=[InputRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Неправильный формат!'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    password_reply = PasswordField('Password reply', validators=[InputRequired(), Length(min=8, max=80)])
    recaptcha = RecaptchaField(validators=[Recaptcha(message='Please complete the captcha')])
