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
    print("PERMISSION LIST")
    permission_list_string = "The Permissions are:\n"

    for permission in permission_list:
        permission_list_string += permission
        permission_list_string += "\n"

    return permission_list_string


if __name__ == '__main__':
    app.debug = True
    app.run()