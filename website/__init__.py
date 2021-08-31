from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdasdadas dsdasd'
    # setup location of the database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # initialize the database to this app

    # import the variable views/auth(blueprint) from the module .views/.auth(file)
    from .views import views
    from .auth import auth

    # Register the blueprint variable on the app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
