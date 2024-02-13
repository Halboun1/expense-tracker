from flask import render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db
from app.models import User, Expense
from app.forms import RegistrationForm, LoginForm

@main_bp.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Implementation for user registration
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implementation for user login
    pass

@app.route('/logout')
@login_required
def logout():
    # Implementation for user logout
    pass


@app.route('/add_expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    # Implementation for adding expenses
    pass

@app.route('/view_expenses')
@login_required
def view_expenses():
    # Implementation for viewing expenses
    pass