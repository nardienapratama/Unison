from flask import Flask

appVar = Flask(__name__,
        static_folder='../public',
        template_folder='./src')

from app import routes
#route module needs to import appVar