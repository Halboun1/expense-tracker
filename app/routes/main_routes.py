from flask import render_template, redirect, url_for, flash
from flask_login import login_user
from app.models import User  # Import your User model
from . import main_bp  # Import the main_bp Blueprint

@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Your login logic here
    user = User.query.filter_by(username=form.username.data).first()
    if user and user.check_password(form.password.data):
        login_user(user)
        flash('Login successful!', 'success')
        return redirect(url_for('main.index'))
    else:
        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)
