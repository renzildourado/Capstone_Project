import flask, flask.views

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return "hello_world"

app.debug = True
app.run()