import datetime
import os

from flask import Flask, Response, request
from flask_mongoengine import MongoEngine

# a simple Flask app using flask-mongoengine to connect to MongoDB

appVar = Flask(__name__)

appVar.config['MONGODB_SETTINGS'] = {
    'host' : os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': 'webapp'
}

db = MongoEngine()
db.init_app(appVar)

class Todo(db.Document):
    title = db.StringField(max_length=60)
    text = db.StringField()
    done = db.BooleanField(default=False)
    pub_date = db.DateTimeField(default=datetime.datetime.now)

@appVar.route("/api")
def index():
    Todo.objects().delete()
    Todo(title="Simple todo A", text="12345678910").save()
    Todo(title="Simple todo B", text="12345678910").save()
    Todo.objects(title__contains="B").update(set__text="Hello world")
    todos = Todo.objects().to__json()
    return Response(todos, mimetype="application/json"), status=200)

if __name__ == "__main__":
    appVar.run(debug=True, port=5000)