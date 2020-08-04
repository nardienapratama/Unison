from flask import redirect, render_template, request, url_for, flash, Blueprint
from .models import Todo

home_blueprint = Blueprint(
    'home',
    __name__
)

@home_blueprint.route("/api")
def index():
    # Todo.objects().delete()
    # Todo(title="Simple todo A", text="12345678910").save()
    # Todo(title="Simple todo B", text="12345678910").save()
    # Todo.objects(title__contains="B").update(set__text="Hello world")
    # todos = Todo.objects().to_json()
    # return Response(todos, mimetype="application/json", status=200)
    return "api"
