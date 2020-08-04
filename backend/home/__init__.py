import datetime
import os
 
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {
#     'host': os.environ['MONGODB_HOST'],
#     'username': os.environ['MONGODB_USERNAME'],
#     'password': os.environ['MONGODB_PASSWORD'],
#     'db': 'webapp'
# }

db = MongoEngine()
db.init_app(app)

from .views import home_blueprint

app.register_blueprint(home_blueprint, url_prefix='/home')

# @app.route('/')
# def home():
#     return redirect(url_for('index'))



