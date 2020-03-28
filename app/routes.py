from app import appVar

@appVar.route('/')
@appVar.route('/index')
def index():
    return "Hello, World!"