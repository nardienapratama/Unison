from flask import Flask

appVar = Flask(__name__)

from app import routes
#route module needs to import appVar