import flask, flask.views
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
    permission_list = process_permissions(permission_list_string)

    permission_list_string_return = "The Permissions are:\n"

    for permission in permission_list:
        permission_list_string_return += permission
        permission_list_string_return += "\n"

    return permission_list_string_return

def process_permissions(permission_string):
    permission_list_string = permission_string.split(",")
    permission_list = []

    for word in permission_list_string:
        permission_list.append(word[1:len(word)-1])     #stripping "" from "ABC"

    return permission_list



if __name__ == '__main__':
    app.debug = True
    app.run()