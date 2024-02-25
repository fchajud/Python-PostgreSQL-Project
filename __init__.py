from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()

# Configuration of the database
DB_USER = 'postgres'
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'USER_MANAGEMENT'

URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the function to create the app
def create_app():
    app = Flask(__name__)

    # Initialize the application with the SQLAlchemy instance
    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config['SECRET_KEY'] = 'dtnls2024'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    try:
        db.init_app(app)
        with app.app_context():
            db.create_all()  # This line will attempt to connect to the database
    except OperationalError:
        print("Could not connect to the database. Please ensure your database service is running and the URI is correct.")


    # Import the routes
    from .routes import routes

    app.register_blueprint(routes, url_prefix='/')

    return app