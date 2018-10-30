import flask, flask.views
from flask import request
app = flask.Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def hello_world():
    return "hello_world"


@app.route("/predict", methods = ["GET", "POST"])
def hello_world():
    permission_list = request.get_json()['permissionList']
    return permission_list


if __name__ == '__main__':
    app.debug = True
    app.run()