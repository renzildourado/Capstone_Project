import flask, flask.views

app = flask.Flask(__name__)


@app.route('https://maliciousappdetector.azurewebsites.net/')
def hello_world():
    return "hello_world"

app.debug = True
app.run()