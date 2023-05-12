from flask import render_template

from app import app, db
from .models import LoginForm, RegisterForm, User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(login=form.login.data, email=form.email.data, password=form.password.data)

        db.session.add(new_user)
        db.session.commit()

        return "<h1> Создан </h1>"
    return render_template('signup.html', form=form)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
