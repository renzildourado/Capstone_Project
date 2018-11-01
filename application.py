import flask, flask.views
from flask import request
app = flask.Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def hello_world():
    return "hello_world"


@app.route("/predict", methods = ["GET", "POST"])
def get_permissions():

    received_json_object = request.get_json()

    permission_list = received_json_object["permissionList"]
    print("PERMISSION LIST" +permission_list)
    print("*", received_json_object)
    return str(received_json_object)


if __name__ == '__main__':
    app.debug = True
    app.run()