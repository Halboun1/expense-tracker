from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from .models import *

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'  # Specify the login view for unauthorized access



def create_app():
    app = Flask(__name__)

    # Other app configurations...

    # Register the blueprint
    from .routes import main_bp  # or your blueprint name
    app.register_blueprint(main_bp)

    # Initialize Flask-Login after registering the blueprint
    login_manager = LoginManager(app)

    # Define the user_loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Other app configurations...

    return app