import flask, flask.views
import ast
from flask import request
app = flask.Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def hello_world():
    return "The Server works"


@app.route("/predict", methods = ["GET", "POST"])
def get_permissions():

    received_json_object = request.get_json()
    permission_list_string = received_json_object["permissionList"]

    #Getting rid of [ and ] in the string [ "A", "B" ]
    permission_list_string = permission_list_string[1:len(permission_list_string)-1]

    #Turning the string into an actual python list
    permission_list = ast.literal_eval(permission_list_string)

    permission_list_string_return = "The Permissions are:\n"

    for permission in permission_list:
        permission_list_string_return += permission
        permission_list_string_return += "\n"

    return permission_list_string_return


if __name__ == '__main__':
    app.debug = True
    app.run()