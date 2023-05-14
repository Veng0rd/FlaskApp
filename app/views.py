from flask import render_template, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user

from markupsafe import Markup
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db
from .models import User
from .forms import LoginForm, RegisterForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        remember = True if form.remember.data else False

        if user is None or not user.password or not check_password_hash(user.password, form.password.data):
            flash(Markup('Email or password is incorrect, please try again'))
            return redirect(url_for('login'))

        login_user(user, remember=remember)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Проверка есть ли с таким email

        if user:
            flash(Markup('User with this email already exists. Go to <a href="login.html }}">login page</a>.'))
            return redirect(url_for('signup'))  # Переадресация на эту же страницу, чтобы flash отобразился

        if form.password.data != form.password_reply.data:
            flash('Passwords are different!')
            return redirect(url_for('signup'))  # Переадресация на эту же страницу, чтобы flash отобразился

        new_user = User(login=form.login.data,
                        email=form.email.data,
                        password=generate_password_hash(form.password.data, method='scrypt'))

        db.session.add(new_user)
        db.session.commit()

        return render_template('index.html')
    return render_template('signup.html', form=form)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.login)




@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
