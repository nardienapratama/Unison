from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    appVar = Flask(__name__)

    appVar.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(appVar)

    from .routes import main
    appVar.register_blueprint(main)
    return appVar

#from backend import routes
#route module needs to import appVar