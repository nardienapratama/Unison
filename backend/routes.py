from backend import appVar
from flask import render_template

@appVar.route('/')
@appVar.route('/index')
def index():
    user = {'username': "Nardiena"}
    return render_template('app.js', title="MusicTrainer", user=user)