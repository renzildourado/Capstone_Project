import flask, flask.views
app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    return "hello_world"


if __name__ == '__main__':
    app.debug = True
    app.run()