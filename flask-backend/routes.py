from app import appVar
from flask import render_template

@appVar.route('/')
@appVar.route('/index')
def index():
    return render_template('index.html', token="Hello Flask+React
    
    app.run(debug=True)