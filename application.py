import flask, flask.views
from flask import request
app = flask.Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def hello_world():
    return "hello_world"


@app.route("/predict", methods = ["GET", "POST"])
def get_permissions():
    permission_list = request.args
    return "hey"


if __name__ == '__main__':
    app.debug = True
    app.run()